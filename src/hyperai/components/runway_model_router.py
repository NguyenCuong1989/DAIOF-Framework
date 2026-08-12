"""Runway Model Router adapter.

Supports routed video, image, and audio generation through one stable
configuration ID. Credentials are read from the environment and are never
included in logs or returned by this adapter.
"""

from __future__ import annotations

import os
import time
from typing import Any, Dict, Optional

import requests


class RunwayConfigurationError(ValueError):
    """Raised when the Runway router configuration is invalid."""


class RunwayTaskError(RuntimeError):
    """Raised when a Runway generation task fails."""


class RunwayModelRouter:
    """HTTP adapter for Runway Model Router generation endpoints."""

    DEFAULT_BASE_URL = "https://api.dev.runwayml.com"
    DEFAULT_API_VERSION = "2024-11-06"
    DEFAULT_CONFIG_ID = "aivideorunway"

    ENDPOINTS = {
        "video": "/v1/generate/video",
        "image": "/v1/generate/image",
        "audio": "/v1/generate/audio",
    }

    TERMINAL_STATUSES = {"SUCCEEDED", "FAILED", "CANCELLED"}

    def __init__(
        self,
        api_secret: Optional[str] = None,
        config_id: Optional[str] = None,
        base_url: Optional[str] = None,
        api_version: Optional[str] = None,
        session: Optional[requests.Session] = None,
    ) -> None:
        self.api_secret = api_secret or os.getenv("RUNWAYML_API_SECRET")
        self.config_id = config_id or os.getenv(
            "RUNWAY_MODEL_ROUTER_CONFIG_ID", self.DEFAULT_CONFIG_ID
        )
        self.base_url = (base_url or os.getenv("RUNWAY_API_BASE_URL", self.DEFAULT_BASE_URL)).rstrip("/")
        self.api_version = api_version or os.getenv(
            "RUNWAY_API_VERSION", self.DEFAULT_API_VERSION
        )
        self.session = session or requests.Session()

        if not self.api_secret:
            raise RunwayConfigurationError(
                "RUNWAYML_API_SECRET is required; credential values must not be hard-coded."
            )
        if not self.config_id:
            raise RunwayConfigurationError("RUNWAY_MODEL_ROUTER_CONFIG_ID is required.")

    def _headers(self) -> Dict[str, str]:
        return {
            "Authorization": "Bearer " + self.api_secret,
            "Content-Type": "application/json",
            "X-Runway-Version": self.api_version,
        }

    def _post(self, modality: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        if modality not in self.ENDPOINTS:
            raise ValueError("Unsupported Runway modality: %s" % modality)

        response = self.session.post(
            self.base_url + self.ENDPOINTS[modality],
            json=payload,
            headers=self._headers(),
            timeout=60,
        )
        response.raise_for_status()
        return response.json()

    def dry_run(self, modality: str, input_payload: Dict[str, Any]) -> Dict[str, Any]:
        """Validate routing without generating or charging credits."""
        payload = {
            "configId": self.config_id,
            "dryRun": True,
            "input": input_payload,
        }
        return self._post(modality, payload)

    def create_task(self, modality: str, input_payload: Dict[str, Any]) -> Dict[str, Any]:
        """Create a live generation task and return the provider response."""
        payload = {
            "configId": self.config_id,
            "input": input_payload,
        }
        return self._post(modality, payload)

    def get_task(self, task_id: str) -> Dict[str, Any]:
        """Retrieve task status/output from Runway."""
        response = self.session.get(
            self.base_url + "/v1/tasks/" + task_id,
            headers=self._headers(),
            timeout=60,
        )
        response.raise_for_status()
        return response.json()

    def wait_for_task_output(
        self,
        task_id: str,
        poll_interval: float = 2.0,
        timeout: float = 900.0,
    ) -> Dict[str, Any]:
        """Poll until the task reaches a terminal state."""
        started = time.monotonic()
        while True:
            task = self.get_task(task_id)
            status = str(task.get("status", "")).upper()

            if status in self.TERMINAL_STATUSES:
                if status != "SUCCEEDED":
                    raise RunwayTaskError(
                        "Runway task %s ended with status %s" % (task_id, status)
                    )
                return task

            if time.monotonic() - started >= timeout:
                raise TimeoutError("Runway task %s exceeded %.1fs timeout" % (task_id, timeout))

            time.sleep(poll_interval)

    def generate(
        self,
        modality: str,
        input_payload: Dict[str, Any],
        *,
        wait: bool = True,
        poll_interval: float = 2.0,
        timeout: float = 900.0,
    ) -> Dict[str, Any]:
        """Create a routed generation and optionally wait for completion."""
        task = self.create_task(modality, input_payload)
        if not wait:
            return task

        task_id = task.get("id") or task.get("taskId")
        if not task_id:
            raise RunwayTaskError("Runway create response did not contain a task id.")
        return self.wait_for_task_output(
            str(task_id), poll_interval=poll_interval, timeout=timeout
        )

    def generate_video(self, prompt_text: str, **input_options: Any) -> Dict[str, Any]:
        payload = dict(input_options)
        payload["promptText"] = prompt_text
        return self.generate("video", payload)

    def generate_image(self, prompt_text: str, **input_options: Any) -> Dict[str, Any]:
        payload = dict(input_options)
        payload["promptText"] = prompt_text
        return self.generate("image", payload)

    def generate_audio(
        self,
        prompt_text: str,
        audio_type: str = "speech",
        **input_options: Any,
    ) -> Dict[str, Any]:
        payload = dict(input_options)
        payload["type"] = audio_type
        payload["promptText"] = prompt_text
        return self.generate("audio", payload)

from hyperai.components.runway_model_router import RunwayModelRouter


class FakeResponse:
    def __init__(self, payload):
        self.payload = payload

    def raise_for_status(self):
        return None

    def json(self):
        return self.payload


class FakeSession:
    def __init__(self):
        self.posts = []
        self.gets = []
        self.polls = [
            {"id": "task-1", "status": "PENDING"},
            {"id": "task-1", "status": "SUCCEEDED", "output": ["https://example.test/output"]},
        ]

    def post(self, url, json, headers, timeout):
        self.posts.append((url, json, headers, timeout))
        return FakeResponse({"id": "task-1"})

    def get(self, url, headers, timeout):
        self.gets.append((url, headers, timeout))
        return FakeResponse(self.polls.pop(0))


def test_router_uses_config_id_and_all_modalities():
    session = FakeSession()
    router = RunwayModelRouter(
        api_secret="test-secret",
        config_id="aivideorunway",
        session=session,
    )

    router.create_task("video", {"promptText": "test video"})
    router.create_task("image", {"promptText": "test image"})
    router.create_task("audio", {"type": "speech", "promptText": "test audio"})

    assert [entry[0] for entry in session.posts] == [
        "https://api.dev.runwayml.com/v1/generate/video",
        "https://api.dev.runwayml.com/v1/generate/image",
        "https://api.dev.runwayml.com/v1/generate/audio",
    ]
    assert all(entry[1]["configId"] == "aivideorunway" for entry in session.posts)
    assert all(entry[2]["X-Runway-Version"] == "2024-11-06" for entry in session.posts)


def test_router_waits_for_successful_task():
    session = FakeSession()
    router = RunwayModelRouter(api_secret="test-secret", session=session)

    result = router.wait_for_task_output("task-1", poll_interval=5, jitter=0)

    assert result["status"] == "SUCCEEDED"
    assert result["output"] == ["https://example.test/output"]
    assert len(session.gets) == 2

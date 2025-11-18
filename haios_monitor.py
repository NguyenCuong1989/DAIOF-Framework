#!/usr/bin/env python3
"""
HAIOS Runtime Monitor Service
Monitors HAIOS system health and logs audit events
"""

import time
import sys
import os

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    import haios_runtime
    from pathlib import Path

    print('🧬 HAIOS Runtime Monitor Started')
    runtime = haios_runtime.HAIOS()

    while True:
        try:
            # Check system health via metrics
            metrics = runtime.get_metrics()
            health_status = "HEALTHY" if metrics['success_rate'] > 0.8 else "WARNING"
            print(f'✅ HAIOS Health: {health_status} (Success Rate: {metrics["success_rate"]:.2f})')
            
            # Log to audit via execute method
            runtime.execute(
                action_type="health_check",
                action_payload={
                    "metrics": metrics,
                    "status": health_status,
                    "autonomous": True
                }
            )
            
            time.sleep(60)  # Check every minute
        except Exception as e:
            print(f'❌ HAIOS Monitor Error: {e}')
            time.sleep(30)

except ImportError as e:
    print(f'❌ Import Error: {e}')
    print('Available modules:', [m for m in sys.modules.keys() if 'haios' in m])
    sys.exit(1)
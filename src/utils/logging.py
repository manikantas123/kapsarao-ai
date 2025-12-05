import json
from datetime import datetime
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# ---------------------------------------------------------
# Generic logger
# ---------------------------------------------------------
def _write_jsonl(file_path: Path, payload: dict):
    with file_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(payload) + "\n")

# ---------------------------------------------------------
# Agent-level logging
# ---------------------------------------------------------
def log_agent_event(agent_name: str, message: str, extra=None):
    if extra is None:
        extra = {}

    record = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "agent": agent_name,
        "message": message,
        "extra": extra,
    }

    file_path = LOG_DIR / f"{agent_name}.log.jsonl"
    _write_jsonl(file_path, record)

# ---------------------------------------------------------
# Orchestrator-level logging
# ---------------------------------------------------------
def log_orchestrator_event(message: str, extra=None):
    if extra is None:
        extra = {}

    record = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "agent": "orchestrator",
        "message": message,
        "extra": extra,
    }

    file_path = LOG_DIR / "orchestrator.log.jsonl"
    _write_jsonl(file_path, record)


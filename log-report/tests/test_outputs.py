import json
from pathlib import Path

REPORT = Path("/app/report.json")


def test_report_saved():
    """Criterion: 'Save your findings so they can be reviewed' — report.json exists and is valid JSON."""
    assert REPORT.exists(), "report.json not found"
    data = json.loads(REPORT.read_text())
    assert isinstance(data, dict), "report.json is not a JSON object"


def test_total_requests():
    """Criterion: 'how many requests there were' — total_requests must equal 6."""
    data = json.loads(REPORT.read_text())
    assert data["total_requests"] == 6, f"expected 6, got {data.get('total_requests')}"


def test_unique_ips():
    """Criterion: 'the clients involved' — unique_ips must equal 3."""
    data = json.loads(REPORT.read_text())
    assert data["unique_ips"] == 3, f"expected 3, got {data.get('unique_ips')}"


def test_top_path():
    """Criterion: 'which pages were popular' — top_path must be /index.html."""
    data = json.loads(REPORT.read_text())
    assert data["top_path"] == "/index.html", f"expected /index.html, got {data.get('top_path')}"

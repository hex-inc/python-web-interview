from typing import Callable
from flask import Flask, jsonify, request
from flask_cors import CORS
from models import Project
import json
import os
import traceback
from pathlib import Path

# Wrap candidate-edited module imports so a syntax error doesn't kill the
# Werkzeug reloader (its parent process exits when the child exits with a
# non-restart code, and there is nothing to bring it back).
_pagination_error: str | None = None
try:
    from pagination import get_page, get_page_filtered
except Exception:
    _pagination_error = traceback.format_exc()
    get_page = None  # type: ignore[assignment]
    get_page_filtered = None  # type: ignore[assignment]

app = Flask(__name__)

CORS(app)

data_dir = Path(__file__).parent.parent / "src" / "api" / "data"


# Example usage in app.py:
def create_user_filter(user_id: int) -> Callable[[Project], bool]:
    """Creates a filter function for projects by user ID"""
    return lambda project: project.creatorId == user_id


def load_json(filename):
    with open(data_dir / filename, "r") as f:
        return json.load(f)


@app.route("/api/users", methods=["GET"])
def get_users():
    return jsonify(load_json("users.json"))


@app.route("/api/projects", methods=["GET"])
def get_projects():
    if get_page is None:
        return jsonify({"error": f"pagination module failed to load:\n{_pagination_error}"}), 500

    projects = load_json("projects.json")

    # Handle pagination using startAfterId
    start_after = None
    start_after_id = request.args.get("startAfterId")
    if start_after_id:
        start_after_id = int(start_after_id)
        start_idx = next(
            (i for i, p in enumerate(projects) if p["id"] == start_after_id), -1
        )
        if start_idx != -1:
            start_after = Project(**projects[start_idx])

    try:
        page_size = int(request.args.get("pageSize", 10))
    except ValueError:
        page_size = 10

    # Filter by userId if provided
    user_id = request.args.get("userId")
    if user_id:
        user_id = int(user_id)
        page = get_page_filtered(page_size, create_user_filter(user_id), start_after)
    else:
        page = get_page(page_size, start_after)

    return jsonify(page)


if __name__ == "__main__":
    port = int(os.environ.get("API_PORT") or 5000)
    # Watch all .py files in the api/ directory so the reloader picks up fixes
    # to files that failed to import (and therefore aren't in sys.modules).
    api_dir = Path(__file__).parent
    extra = [str(p) for p in api_dir.glob("*.py")]
    app.run(port=port, debug=True, extra_files=extra)

from typing import Callable
from flask import Flask, jsonify, request
from flask_cors import CORS
from pagination import get_page, get_page_filtered
from models import Project
import json
import os
from pathlib import Path

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
    port = int(os.environ.get("API_PORT", 5000))
    app.run(port=port, debug=True)

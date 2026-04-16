# Python Web Interview

## Overview

Welcome to the Hex Coding Interview! During the interview session, you'll implement two functions this repository to fix an application. All changes will be made to `api/pagination.py`.

Before the session starts, please clone this repository and run `npm install` and `uv sync` in the root to install dependencies. You can also add any other dependencies that you think that you may want to use, but there is no need to write any code or do anything else ahead of time to prepare for the session.

## Running the app

1) Install JS dependencies with `npm install`.
2) Install Python dependencies with `uv sync`. If `uv` is unavailable, first run `pip install uv`.
3) Run `npm run start`. You should be able to view the app at [http://localhost:3000/](http://localhost:3000/). It will hot reload as you make changes.

**A note on the API port**
The API will attempt to run on port 5000.
If 5000 is already in use, the next available port is used automatically (logged to the terminal on startup).
You can pin the API_PORT if needed (rare): `API_PORT=5010 npm start`.

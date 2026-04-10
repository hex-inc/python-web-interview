#!/bin/bash
trap 'kill 0' EXIT

# Find a free port for the API and share it with the frontend.
# Prefer 5000 for consistency; fall back to a random port if taken.
export API_PORT=$(python3 -c "
import socket
s = socket.socket()
try:
    s.bind(('127.0.0.1', 5000))
except OSError:
    s.bind(('127.0.0.1', 0))
print(s.getsockname()[1])
s.close()
")
export REACT_APP_API_PORT=$API_PORT

npm run start-api &
npm run start-frontend

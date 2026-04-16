#!/bin/bash
trap 'kill 0' EXIT

# Find a free port for the API, starting from 5000.
# Override: API_PORT=5010 npm start
if [ -z "$API_PORT" ]; then
  API_PORT=$(python3 -c "
import socket, sys
for port in range(5000, 5020):
    s = socket.socket()
    try:
        s.bind(('127.0.0.1', port))
        print(port)
        s.close()
        sys.exit(0)
    except OSError:
        s.close()
print('ERROR: no free port in 5000-5019', file=sys.stderr)
sys.exit(1)
") || exit 1
fi

export API_PORT
export REACT_APP_API_PORT=$API_PORT

echo ""
echo "  API port: $API_PORT  (override with API_PORT=<port> npm start)"
echo ""

npm run start-api &
npm run start-frontend

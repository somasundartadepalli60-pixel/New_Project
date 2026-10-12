"""Development entry point for the LDICA Master Learning Hub.

For local development, set FLASK_DEBUG=1 in the environment if a debugger is
needed. Debug mode is disabled by default to avoid exposing a debugger in a
misconfigured deployment.
"""
import os
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG", "0").strip() == "1")

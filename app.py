"""Simple Flask application for demonstrating CI/CD in GitHub Codespaces."""
from datetime import datetime
import os
import sys

from flask import Flask, jsonify

app = Flask(__name__)


def build_home_payload() -> dict:
    """Return the payload for the home endpoint."""
    return {
        "message": "CI/CD Demo API",
        "version": "1.1.0",
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }


def detect_codespaces_environment() -> bool:
    """Determine whether the app is running inside GitHub Codespaces."""
    return bool(os.getenv("CODESPACES") or os.getenv("CODESPACE_NAME"))


@app.route("/")
def home():
    """Provide general information about the demo service."""
    return jsonify(build_home_payload())


@app.route("/health")
def health():
    """Basic health check endpoint."""
    return jsonify({"status": "healthy"}), 200


@app.route("/products")
def products():
    """Return a list of sample products."""
    return jsonify(
        [
            {"id": 1, "name": "Laptop", "price": 999},
            {"id": 2, "name": "Phone", "price": 599},
        ]
    )


@app.route("/environment")
def environment():
    """Expose basic environment details useful when running in Codespaces."""
    workspace = os.getenv("GITHUB_WORKSPACE", "local-development")
    return jsonify(
        {
            "codespaces": detect_codespaces_environment(),
            "workspace": workspace,
            "python_version": sys.version.split()[0],
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

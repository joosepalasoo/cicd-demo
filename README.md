# CI/CD Demo Python App

This repository contains a small Flask application that is ready to run inside [GitHub Codespaces](https://github.com/features/codespaces). It is intentionally lightweight so you can focus on experimenting with dev containers, automated tests, and deployment workflows.

## Application overview

The service exposes a few simple endpoints:

| Endpoint | Description |
| --- | --- |
| `/` | Returns metadata such as the current API version and a timestamp. |
| `/health` | Provides a basic health check useful for monitoring probes. |
| `/products` | Serves a static list of demo products. |
| `/environment` | Shows whether the app is running in Codespaces and displays workspace metadata. |

The `/environment` endpoint inspects GitHub-specific environment variables, making it easy to verify that your Codespace is configured as expected.

## Getting started in Codespaces

1. Create a new Codespace for this repository (use the "Code" menu and select **Create codespace on main**).
2. Once the Codespace finishes building, open a terminal and install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the Flask development server:

   ```bash
   flask --app app run --host 0.0.0.0 --port 5000
   ```

4. Use the forwarded port panel to open the running application in your browser. You should see the JSON payload from the `/` endpoint.

## Running tests

Run the automated test suite with `pytest`:

```bash
pytest
```

The tests include an example of using `monkeypatch` to emulate the Codespaces environment variables when exercising the `/environment` endpoint.

## Container usage

A `Dockerfile` is provided so you can build and run the application in a container that mimics the Codespaces environment:

```bash
docker build -t cicd-demo .
docker run -p 5000:5000 cicd-demo
```

This is helpful for validating the application locally before pushing to a branch that triggers your CI/CD pipeline.

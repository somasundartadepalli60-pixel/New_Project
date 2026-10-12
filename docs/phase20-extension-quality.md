# Phase 20 — Extension Framework & Quality Engineering

## Trusted extension registry

`app.plugins.PluginSpec` defines metadata, capabilities and an optional initialisation callback. `PluginRegistry` rejects duplicate names, validates metadata and produces a stable sorted inventory. Extensions are registered explicitly in trusted Python code with `register_plugin(app, spec)`. The application does **not** dynamically import modules based on request parameters, scan writable directories, or execute uploaded code.

Example:

```python
from app.plugins import PluginSpec, register_plugin

register_plugin(app, PluginSpec(
    name="custom-formulas",
    version="1.0.0",
    description="Additional local formula tools",
    capabilities=("formula-evaluation",),
))
```

## Deployment diagnostics

Run `python scripts/check_deployment.py` from the project root. It checks database connectivity/integrity, instance-directory writability, session-secret length, and secure-cookie configuration. It deliberately never prints secret values or raw database exception text. A warning for secure cookies is expected on local HTTP development; enable `SESSION_COOKIE_SECURE=True` when deployed behind HTTPS.

## Quality checks

Install dependencies, then run:

```bash
pytest
python scripts/check_deployment.py
python -m compileall -q app scripts tests
```

The new tests cover registry ordering, duplicate rejection, validation, lifecycle callback registration, safe database diagnostics, and writable-directory checks. The suite must be run in the target environment; syntax checks alone do not establish runtime correctness.

## Extension boundaries and limitations

- Plugins are trusted in-process Python code and have the same permissions as the application; do not install unreviewed extensions.
- Capabilities are descriptive metadata, not a security sandbox or permission system.
- The registry is in-memory and must be populated during application setup; it is not a marketplace or persistent plugin manager.
- Deployment checks are basic diagnostics, not a full security audit, load test, or production-readiness certification.

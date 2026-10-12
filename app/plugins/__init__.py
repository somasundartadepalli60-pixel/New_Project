"""Small, explicit extension registry for optional LDICA modules.

Plugins are registered by Python code during app setup; this package never imports
arbitrary modules from user input or scans writable directories for executable code.
"""
from dataclasses import dataclass, field
from typing import Callable, Optional


@dataclass(frozen=True)
class PluginSpec:
    """Metadata and optional lifecycle callbacks for one trusted extension."""
    name: str
    version: str
    description: str
    initialise: Optional[Callable] = None
    capabilities: tuple[str, ...] = field(default_factory=tuple)

    def validate(self):
        if not self.name or not self.name.replace("-", "").replace("_", "").isalnum():
            raise ValueError("Plugin name must contain only letters, numbers, '_' or '-'.")
        if not self.version or not self.description.strip():
            raise ValueError("Plugin version and description are required.")
        if len(set(self.capabilities)) != len(self.capabilities):
            raise ValueError("Plugin capabilities must be unique.")
        return self


class PluginRegistry:
    """Deterministic registry; duplicate names are rejected instead of overwritten."""
    def __init__(self):
        self._plugins: dict[str, PluginSpec] = {}

    def register(self, plugin: PluginSpec, app=None) -> PluginSpec:
        plugin.validate()
        if plugin.name in self._plugins:
            raise ValueError(f"Plugin already registered: {plugin.name}")
        if app is not None and plugin.initialise is not None:
            plugin.initialise(app)
        self._plugins[plugin.name] = plugin
        return plugin

    def get(self, name: str) -> Optional[PluginSpec]:
        return self._plugins.get(name)

    def list(self) -> list[dict]:
        return [
            {"name": p.name, "version": p.version, "description": p.description,
             "capabilities": list(p.capabilities)}
            for p in sorted(self._plugins.values(), key=lambda item: item.name)
        ]

    def __len__(self):
        return len(self._plugins)


def register_plugin(app, plugin: PluginSpec) -> PluginSpec:
    """Register a trusted plugin against an application instance."""
    registry = app.extensions.get("ldica_plugin_registry")
    if registry is None:
        registry = PluginRegistry()
        app.extensions["ldica_plugin_registry"] = registry
    return registry.register(plugin, app)

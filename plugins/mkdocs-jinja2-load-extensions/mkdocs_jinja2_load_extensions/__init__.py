import mkdocs
from mkdocs import plugins
from logging import getLogger

logger = getLogger("mkdocs")

class Jinja2LoadExtensionPlugin(plugins.BasePlugin):

    config_scheme = (
        ('extensions', mkdocs.config.config_options.Type(list, default=[])),
    )

    def on_env(self, env, config, files):
        extensions = self.config.get("extensions")
        for ext in extensions:
            logger.info(f"Loading Jinja2 extension <{ext}>.")
            env.add_extension(ext)


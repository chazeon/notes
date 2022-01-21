from setuptools import setup

setup(
    name="mkdocs-jinja2-load-extensions",
    version="0.0.1",
    packages=["mkdocs_jinja2_load_extensions"],
    entry_points={
        'mkdocs.plugins': [
            'jinja2_load_extensions = mkdocs_jinja2_load_extensions:Jinja2LoadExtensionPlugin',
        ]
    },
    requires=[
        "mkdocs",
    ]
)
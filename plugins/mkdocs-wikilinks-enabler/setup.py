from setuptools import setup, find_packages

setup(
    name="mkdocs-wikilinks-enabler",
    version="0.0.1",
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'mkdocs_wikilinks_enabler = mkdocs_wikilinks_enabler:WikiLinksEnablerPlugin',
        ]
    },
    install_requires=[
        "mkdocs",
    ]
)
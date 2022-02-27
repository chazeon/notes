from setuptools import setup, find_packages

setup(
    name="mkdocs-blogging",
    version="0.0.1",
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'mkdocs_blogging = mkdocs_blogging:BloggingPlugin',
        ]
    },
    install_requires=[
        "mkdocs",
    ]
)
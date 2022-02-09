from setuptools import setup, find_packages

setup(
    name="mkdocs-subpages",
    version="0.0.1",
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'mkdocs_subpages = mkdocs_subpages:MkdocsSubpagesPlugin',
        ]
    },
    install_requires=[
        "mkdocs",
    ]
)
from setuptools import setup, find_packages

setup(
    name="mkdocs-compile-sass",
    version="0.0.1",
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'compile_sass = mkdocs_compile_sass:CompileSASSPlugin',
        ]
    },
    requires=[
        "mkdocs",
        "libsass"
    ]
)
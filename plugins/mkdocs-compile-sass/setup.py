from setuptools import setup

setup(
    name="mkdocs-compile-sass",
    version="0.0.1",
    packages=["mkdocs_compile_sass"],
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
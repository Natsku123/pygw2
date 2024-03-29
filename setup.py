from setuptools import setup

setup(
    name="pygw2",
    version="0.0.1",
    description="Python wrapper for Guild Wars 2 API.",
    license="MIT",
    packages=[
        "pygw2",
        "pygw2.api",
        "pygw2.core",
        "pygw2.core.models",
    ],
    install_requires=["requests", "pydantic"],
    author="Max Mecklin",
    author_email="max@meckl.in",
    keywords=["api", "python", "guild", "wars", "2", "gw2"],
    url="https://github.com/Natsku123/pygw2",
)

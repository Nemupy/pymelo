import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymelo",
    version="0.0.1",
    author="Nemupy",
    author_email="nemu.otoyume@gmail.com",
    description="Wrapper for DiscordPomeloAPI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nemupy/pymelo",
    packages=setuptools.find_packages()
)

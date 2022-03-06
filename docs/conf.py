import re

project = "discord.py-ipc"
author = "Sn1F3rt"
copyright = "2022, Sn1F3rt"


with open("../discord/ext/ipc/__init__.py") as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
    ).group(1)

release = version

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx_rtd_theme",
    "sphinxcontrib_trio",
]


autodoc_typehints = "none"

intersphinx_mapping = {
    "aiohttp": ("https://docs.aiohttp.org/en/stable/", None),
    "python": ("https://docs.python.org/3", None),
    "discord": ("https://discordpy.readthedocs.io/en/latest", None),
}

highlight_language = "python3"
html_theme = "sphinx_rtd_theme"
master_doc = "index"
pygments_style = "friendly"
source_suffix = ".rst"

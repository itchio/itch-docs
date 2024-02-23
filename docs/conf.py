# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Itch.io App"
copyright = (
    "2024, Amos Wenger, [leafo](https://github.com/leafo) and the community on GitHub"
)
author = "Amos Wenger, [leafo](https://github.com/leafo) and the community on GitHub"
release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser", "sphinx_tippy"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]
html_title = "Itch.io App"

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#8E3737",
        "color-brand-content": "#8E3737",
    },
    "dark_css_variables": {
        "color-brand-primary": "#ea4d4d",
        "color-brand-content": "#ea4d4d",
    },
}

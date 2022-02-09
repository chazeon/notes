import jinja2
from logging import getLogger
from mkdocs.plugins import BasePlugin
from mkdocs.structure.pages import Page

logger = getLogger("mkdocs")

def subpages(page: Page) -> list:
    subpages = []
    for child in page.ancestors[0].children:
        if child.is_page:
            subpages.append(child)
        else:
            subpages.append(child.children[0])
    return subpages

class MkdocsSubpagesPlugin(BasePlugin):

    def on_env(self, env, config, files):
        env.filters["subpages"] = subpages
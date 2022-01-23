from mkdocs import plugins
from logging import getLogger
import difflib
from mkdocs.utils import normalize_url

from markdown.extensions.wikilinks import WikiLinkExtension, WikiLinksInlineProcessor


logger = getLogger("mkdocs")


class CustomWikiLinkExtension(WikiLinkExtension):
    '''Wiki link extension but with a more permissive wikilinks regex expression.'''

    def extendMarkdown(self, md):

        self.md = md

        # append to end of inline patterns
        WIKILINK_RE = r'\[\[(.+?)\]\]'
        wikilinkPattern = WikiLinksInlineProcessor(WIKILINK_RE, self.getConfigs())
        wikilinkPattern.md = md
        md.inlinePatterns.register(wikilinkPattern, 'wikilink', 75)


class WikiLinksEnablerPlugin(plugins.BasePlugin):

    def __init__(self) -> None:
        super().__init__()
        self.docs = None
        self.index = None
        self.curr_page = None

    def build_url(self, label, base, end):

        if self.index == None:
            for doc in self.docs:
                page = doc.page
                if page.title is None:
                    page.read_source(self.config)

            self.index = dict([ 
                (doc.page.title.lower(), doc.url) for doc in self.docs
            ])

        matches = difflib.get_close_matches(label, self.index.keys())
        if len(matches) == 0:
            logger.warning(f"Cannot create wikilink for <{label}>")
            return ""

        url = "/" + self.index[matches[0]]
        url = normalize_url(url[1:], self.curr_page)
        logger.info(f"Wikilink <{label}> on <{self.curr_page.title}> -> <{url}>")
        return url

    def on_config(self, config):
        config["markdown_extensions"].insert(0, CustomWikiLinkExtension(
            build_url=lambda label, base, end: self.build_url(label, base, end)
        ))

        self.config = config

    def on_files(self, files, config):
        self.docs = files.documentation_pages()
    
    def on_pre_page(self, page, config, files):
        self.curr_page = page
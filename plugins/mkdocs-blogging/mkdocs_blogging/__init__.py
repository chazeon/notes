from mkdocs import plugins
from logging import getLogger
from datetime import datetime
from pathlib import Path

logger = getLogger("mkdocs")

class BloggingPlugin(plugins.BasePlugin):

    def __init__(self) -> None:
        super().__init__()

    def on_page_markdown(self, markdown, page, config, files):
        if "date" not in "page.meta":
            stat = Path(page.file.abs_src_path).stat()
            mtime = datetime.fromtimestamp(stat.st_mtime)
            page.meta["date"] = mtime.strftime(r"%Y-%m-%d")
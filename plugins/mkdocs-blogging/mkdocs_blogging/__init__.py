from datetime import date, datetime
from pathlib import Path
from subprocess import run

from mkdocs import plugins


class BloggingPlugin(plugins.BasePlugin):
    def on_page_markdown(self, markdown, page, config, files):
        if "date" in page.meta:
            return

        path = Path(page.file.abs_src_path)
        git_date = run(
            ["git", "-C", path.parent, "log", "-1", "--format=%cs", "--", path.name],
            capture_output=True,
            text=True,
        ).stdout.strip()

        page.meta["date"] = (
            date.fromisoformat(git_date)
            if git_date
            else datetime.fromtimestamp(path.stat().st_mtime).date()
        )

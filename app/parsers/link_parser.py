"""
Link Parser

Purpose:
Extract Obsidian links from Markdown content.
"""

import re
from typing import List


class LinkParser:

    LINK_PATTERN = r"\[\[(.*?)\]\]"

    def extract_links(self, content: str) -> List[str]:

        return re.findall(
            self.LINK_PATTERN,
            content
        )
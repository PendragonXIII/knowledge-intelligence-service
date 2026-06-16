# ######################################
# Link Parser
# ######################################

# Zweck:
# Extrahiert Obsidian-Links aus Markdown-Dateien.

import re
from typing import List


class LinkParser:

    LINK_PATTERN = r"\[\[(.*?)\]\]"

    def extract_links(self, content: str) -> List[str]:

        return re.findall(
            self.LINK_PATTERN,
            content
        )
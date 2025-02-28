import re
from enum import Enum


def markdown_to_blocks(markdown: str):
    return [block.strip() for block in markdown.split("\n\n") if block]


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block: str):
    def is_ordered_list(block_text: str):
        lines = block_text.strip().split("\n")

        if not lines:
            return False

        expected_number = 1

        for line in lines:
            expected_prefix = f"{expected_number}. "
            if not line.startswith(expected_prefix):
                return False
            expected_number += 1

        return True

    heading_pattern = re.compile(r"^#{1,6} .+")
    code_block_pattern = re.compile(r"^`{3}\n(.*)\n`{3}$", re.DOTALL)

    if heading_pattern.match(block) is not None:
        return BlockType.HEADING

    if code_block_pattern.match(block.strip()) is not None:
        return BlockType.CODE

    lines = block.strip().split("\n")

    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    if is_ordered_list(block):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

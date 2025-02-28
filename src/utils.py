import re

from text_node import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text.count(delimiter) % 2 != 0:
            raise ValueError(f"invalid node {node}: unclosed delimeter")

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        for idx, words in enumerate(node.text.split(delimiter)):
            if words:
                if idx % 2 == 0:
                    new_nodes.append(TextNode(words, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(words, text_type))

    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[([\w\s]+)\]\(([\w:/.]+)\)"
    # pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)


def extract_markdown_links(text):
    pattern = r"\[([\w\s]+)\]\(([\w:/.@]+)\)"
    # pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)

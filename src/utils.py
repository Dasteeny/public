import re
from typing import Callable

from text_node import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
):
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


def extract_markdown_images(text: str):
    pattern = r"!\[([\w\s]+)\]\(([\w:/.]+)\)"
    # pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)


def extract_markdown_links(text: str):
    # pattern = r"(?<!!)\[([\w\s]+)\]\(([\w:/.@]+)\)"
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)


def split_nodes_image(old_nodes: list[TextNode]):
    new_nodes = split_nodes_by_functor(old_nodes, extract_markdown_images)
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]):
    new_nodes = split_nodes_by_functor(old_nodes, extract_markdown_links)
    return new_nodes


def split_nodes_by_functor(
    old_nodes: list[TextNode], functor: Callable[[str], list[tuple[str, str]]]
):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        matches = functor(old_node.text)
        if not matches:
            new_nodes.append(old_node)
            continue

        text_to_process = old_node.text
        for match in matches:
            alt_text = match[0]
            img_url = match[1]

            if functor == extract_markdown_images:
                split_pattern = f"![{alt_text}]({img_url})"
                new_node_type = TextType.IMAGE
            else:
                split_pattern = f"[{alt_text}]({img_url})"
                new_node_type = TextType.LINK

            new_node_text, text_to_process = text_to_process.split(
                split_pattern, maxsplit=1
            )
            if new_node_text:
                new_nodes.append(TextNode(new_node_text, TextType.TEXT))
            new_nodes.append(TextNode(alt_text, new_node_type, img_url))
        if text_to_process:
            new_nodes.append(TextNode(text_to_process, TextType.TEXT))

    return new_nodes


def text_to_textnodes(text: str):
    nodes = [TextNode(text, TextType.TEXT)]
    for text_type, delimiter in [
        (TextType.BOLD, "**"),
        (TextType.CODE, "`"),
        (TextType.ITALIC, "_"),
    ]:
        nodes = split_nodes_delimiter(nodes, delimiter, text_type)

    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes

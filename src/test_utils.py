import unittest

from text_node import TextNode, TextType
from utils import extract_markdown_images, extract_markdown_links, split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_base_case(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_two_delimited_parts(self):
        node = TextNode("This is **text** with a **bold words**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with a ", TextType.TEXT),
                TextNode("bold words", TextType.BOLD),
            ],
        )

    def test_three_delimited_parts(self):
        node = TextNode("This *is* text *with a* italic *words*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This ", TextType.TEXT),
                TextNode("is", TextType.ITALIC),
                TextNode(" text ", TextType.TEXT),
                TextNode("with a", TextType.ITALIC),
                TextNode(" italic ", TextType.TEXT),
                TextNode("words", TextType.ITALIC),
            ],
        )

    def test_three_old_nodes(self):
        node_1 = TextNode(
            "This is first text with a `first code block` word", TextType.TEXT
        )
        node_2 = TextNode(
            "This is second text with a `second code block` word", TextType.TEXT
        )
        node_3 = TextNode(
            "This is third text with a `third code block` word", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node_1, node_2, node_3], "`", TextType.CODE)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is first text with a ", TextType.TEXT),
                TextNode("first code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
                TextNode("This is second text with a ", TextType.TEXT),
                TextNode("second code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
                TextNode("This is third text with a ", TextType.TEXT),
                TextNode("third code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_no_text_type(self):
        node = TextNode("This is bold text", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(new_nodes, [TextNode("This is bold text", TextType.BOLD)])

    def test_unclosed_delimiter(self):
        node = TextNode("This is text with a `code block word", TextType.TEXT)

        with self.assertRaises(ValueError) as err:
            split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            str(err.exception), f"invalid node {repr(node)}: unclosed delimeter"
        )


class TestExtractMarkdownLinks(unittest.TestCase):
    def test_two_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(
            extract_markdown_links(text),
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
        )


class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_two_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(
            extract_markdown_images(text),
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
        )


if __name__ == "__main__":
    unittest.main()

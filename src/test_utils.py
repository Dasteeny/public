import unittest

from text_node import TextNode, TextType
from utils import split_nodes_delimiter


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


if __name__ == "__main__":
    unittest.main()

import unittest

from text_node import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")

    def test_repr_w_url(self):
        node = TextNode("This is a text node", TextType.CODE, "http://www.boot.dev")
        self.assertEqual(
            repr(node), "TextNode(This is a text node, code, http://www.boot.dev)"
        )

    def test_text_node_to_html_code_text_type(self):
        text_node = TextNode("Normal text", TextType.TEXT)
        self.assertEqual(text_node_to_html_node(text_node).to_html(), "Normal text")

    def test_text_node_to_html_code_bold_type(self):
        text_node = TextNode("Bold text", TextType.BOLD)
        self.assertEqual(
            text_node_to_html_node(text_node).to_html(), "<b>Bold text</b>"
        )

    def test_text_node_to_html_code_italic_type(self):
        text_node = TextNode("Italic text", TextType.ITALIC)
        self.assertEqual(
            text_node_to_html_node(text_node).to_html(), "<i>Italic text</i>"
        )

    def test_text_node_to_html_code_code_type(self):
        text_node = TextNode("Code text", TextType.CODE)
        self.assertEqual(
            text_node_to_html_node(text_node).to_html(), "<code>Code text</code>"
        )

    def test_text_node_to_html_code_link_type(self):
        text_node = TextNode("Link text", TextType.LINK, "http://boot.dev")
        self.assertEqual(
            text_node_to_html_node(text_node).to_html(),
            '<a href="http://boot.dev">Link text</a>',
        )

    def test_text_node_to_html_code_img_type(self):
        text_node = TextNode("Image text", TextType.IMAGE, "http://boot.dev")
        self.assertEqual(
            text_node_to_html_node(text_node).to_html(),
            '<img src="http://boot.dev" alt="Image text"></img>',
        )


if __name__ == "__main__":
    unittest.main()

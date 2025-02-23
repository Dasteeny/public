import unittest

from leaf_node import LeafNode
from parent_node import ParentNode


class TestParentNode(unittest.TestCase):
    def test_no_children(self):
        parent_node = ParentNode("b", None)
        self.assertRaises(ValueError, parent_node.to_html)

    def test_no_tag(self):
        parent_node = ParentNode(None, None)
        self.assertRaises(ValueError, parent_node.to_html)

    def test_to_html_only_children_no_props(self):
        parent_node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            parent_node.to_html(),
            "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>",
        )

    def test_to_html_only_children_w_props(self):
        parent_node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text"),
            ],
            {"text-indent": "30px", "style": "uppercase"},
        )
        self.assertEqual(
            parent_node.to_html(),
            '<p text-indent="30px" style="uppercase"><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>',
        )

    def test_to_html_only_children_w_parent(self):
        parent_node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                    ],
                ),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            parent_node.to_html(),
            "<p><b>Bold text</b>Normal text<p><b>Bold text</b>Normal text</p><i>Italic text</i>Normal text</p>",
        )

    def test_to_html_div_w_props(self):
        parent_node = ParentNode(
            "div",
            [
                LeafNode("h1", "ParentNode"),
                LeafNode("p", "i heard you like recursion."),
                ParentNode(
                    "p",
                    [
                        LeafNode(None, "The new "),
                        LeafNode("code", "Parent Node"),
                        LeafNode(
                            None,
                            " class will handle the nesting of HTML nodes inside of one another. Any HTML node that's not 'leaf' node (i.e. it ",
                        ),
                        LeafNode("em", "has"),
                        LeafNode(None, " children) is a 'parent' node."),
                    ],
                ),
            ],
            {"class": "viewer p-4"},
        )
        self.assertEqual(
            parent_node.to_html(),
            "<div class=\"viewer p-4\"><h1>ParentNode</h1><p>i heard you like recursion.</p><p>The new <code>Parent Node</code> class will handle the nesting of HTML nodes inside of one another. Any HTML node that's not 'leaf' node (i.e. it <em>has</em> children) is a 'parent' node.</p></div>",
        )


if __name__ == "__main__":
    unittest.main()

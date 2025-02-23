import unittest

from leaf_node import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_does_not_accept_children(self):
        with self.assertRaises(TypeError):
            LeafNode(tag="p", value="Lorem Ipsum", children=[], props={"color": "blue"})

    def test_to_html_no_value(self):
        leaf_node = LeafNode(tag="p", value="Lorem Ipsum", props={"color": "blue"})
        leaf_node.value = None
        self.assertRaises(ValueError, leaf_node.to_html)

    def test_to_html_no_tag(self):
        leaf_node = LeafNode(tag="p", value="Lorem Ipsum", props={"color": "blue"})
        leaf_node.tag = None
        self.assertEqual(leaf_node.to_html(), "Lorem Ipsum")

    def test_to_html_no_props(self):
        leaf_node = LeafNode(tag="p", value="Lorem Ipsum")
        self.assertEqual(leaf_node.to_html(), "<p>Lorem Ipsum</p>")

    def test_to_html_w_props(self):
        leaf_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            leaf_node.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )


if __name__ == "__main__":
    unittest.main()

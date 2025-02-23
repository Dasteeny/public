import unittest

from html_node import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_rerp(self):
        html_node = HTMLNode(
            tag="p",
            value="Lorem Ipsum",
            children=[HTMLNode(value="Child1"), HTMLNode(value="Child2")],
            props={"color": "black"},
        )
        self.assertEqual(
            repr(html_node),
            "HTMLNode(p, Lorem Ipsum, children: [HTMLNode(None, Child1, children: None, None), HTMLNode(None, Child2, children: None, None)], {'color': 'black'})",
        )

    def test_to_html(self):
        html_node = HTMLNode(
            tag="p",
            value="Lorem Ipsum",
            props={"color": "black"},
        )
        self.assertRaises(NotImplementedError, html_node.to_html)

    def test_props_to_html(self):
        html_node = HTMLNode(
            tag="a",
            value="Lorem Ipsum",
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        props_as_html = html_node.props_to_html()
        self.assertEqual(
            props_as_html,
            ' href="https://www.google.com" target="_blank"',
        )

    def test_props_to_html_no_props(self):
        html_node = HTMLNode(
            tag="p",
            value="Lorem Ipsum",
        )
        props_as_html = html_node.props_to_html()
        self.assertEqual(props_as_html, "")


if __name__ == "__main__":
    unittest.main()

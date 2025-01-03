import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("This is a text node", "p")
        node2 = HTMLNode("This is a text node", "p")
        self.assertEqual(node, node2)

    def test_no_props(self):
        node = HTMLNode("This is a text node", "p")
        self.assertEqual(node.props, {})

    def test_repr(self):
        node = HTMLNode("This is a text node", "p")
        self.assertEqual(repr(node), "HTMLNode(p, This is a text node, [], {})")

    def test_repr_with_props(self):
        node = HTMLNode("This is a text node", "p", props={"class": "text"})
        self.assertEqual(
            repr(node), "HTMLNode(p, This is a text node, [], {'class': 'text'})"
        )


class TestLeadNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("This is a text node", "p")
        node2 = LeafNode("This is a text node", "p")
        self.assertEqual(node, node2)

    def test_no_props(self):
        node = LeafNode("This is a text node", "p")
        self.assertEqual(node.props, {})


class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode("div", [LeafNode("This is a text node", "p")])
        node2 = ParentNode("div", [LeafNode("This is a text node", "p")])
        self.assertEqual(node, node2)

    def test_no_tag_should_raise_error(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("This is a text node", "p")])

    def test_no_children_should_raise_error(self):
        with self.assertRaises(ValueError):
            ParentNode("div", [])

    def test_nested_parents(self):
        node = ParentNode(
            "div", [ParentNode("div", [LeafNode("This is a text node", "p")])]
        )
        self.assertEqual(
            node.to_html(), "<div ><div ><p >This is a text node</p></div></div>"
        )

    def tree_of_tested_nodes_with_two_children_each(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "div",
                    [
                        LeafNode("This is a text node", "p"),
                        LeafNode("This is a text node", "p"),
                    ],
                ),
                ParentNode(
                    "div",
                    [
                        LeafNode("This is a text node", "p"),
                        LeafNode("This is a text node", "p"),
                    ],
                ),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<div ><div ><p ></p><p ></p></div><div ><p ></p><p ></p></div></div>",
        )


if __name__ == "__main__":
    unittest.main()

import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_no_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, "")

    def test_repr(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(repr(node), "TextNode(This is a text node, TextType.ITALIC, )")

    def test_repr_with_url(self):
        node = TextNode("This is a text node", TextType.LINK, "https://example.com")
        self.assertEqual(
            repr(node),
            "TextNode(This is a text node, TextType.LINK, https://example.com)",
        )

    def test_paragraph_to_html_node(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        self.assertEqual(node.to_html_node().to_html(), "<p >This is a text node</p>")

    def test_bold_to_html_node(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        self.assertEqual(node.to_html_node().to_html(), "<b >This is a bold node</b>")

    def test_italic_to_html_node(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        self.assertEqual(
            node.to_html_node().to_html(), "<i >This is an italic node</i>"
        )

    def test_code_to_html_node(self):
        node = TextNode("This is a code node", TextType.CODE)
        self.assertEqual(
            node.to_html_node().to_html(), "<code >This is a code node</code>"
        )

    def test_image_to_html_node(self):
        node = TextNode("This is an image node", TextType.IMAGE, "https://example.com")
        self.assertEqual(
            node.to_html_node().to_html(),
            '<img src="https://example.com" alt="This is an image node">',
        )

    def test_link_to_html_node(self):
        node = TextNode("This is a text node", TextType.LINK, "https://example.com")
        self.assertEqual(
            node.to_html_node().to_html(),
            '<a href="https://example.com">This is a text node</a>',
        )

    def test_no_link_should_raise_error(self):
        with self.assertRaises(ValueError):
            TextNode("This is a text node", TextType.LINK)

    def test_no_image_should_raise_error(self):
        with self.assertRaises(ValueError):
            TextNode("This is a text node", TextType.IMAGE)

    def test_invalid_text_type_should_raise_error(self):
        with self.assertRaises(ValueError):
            TextNode("This is a text node", "invalid")


if __name__ == "__main__":
    unittest.main()

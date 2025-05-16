import unittest
from textnode import TextNode, TextType, text_node_to_html_node



class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)


    def test_not_eq(self):
        node1 = TextNode("This is a 2nd text node", TextType.ITALIC)
        node2 = TextNode("This is a 2nd text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)


    def test_url_eq_none(self):
        node1 = TextNode("This is a 3rd text node", TextType.ITALIC)
        node2 = TextNode("This is a 3rd text node", TextType.ITALIC)
        self.assertEqual(node1.url, None)


    def test_eq_url(self):
        node1 = TextNode("This is a 4th text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a 4th text node", TextType.BOLD, "https://www.boot.dev")
        self.assertEqual(node1, node2)


    def test_repr(self):
        node = TextNode("This is a 5th text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual("TextNode(This is a 5th text node, text, https://www.boot.dev)", repr(node))
        


class TestTxttoHtmlNode(unittest.TestCase):

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")






if __name__ == "__main__":
    unittest.main() 

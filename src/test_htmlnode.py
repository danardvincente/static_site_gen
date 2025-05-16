import unittest

from htmlnode import HtmlNode



class TestHtmlNode(unittest.TestCase):

    def test_props_to_html(self):
        html = HtmlNode(props={"href" : "https://www.google.com", "target" : "_blank",})
        self.assertEqual(html.props_to_html(), ' href="https://www.google.com" target="_blank"')


    def test_props_to_html2(self):
        html = HtmlNode(props={"src" : "image.jpg", "alt" : "This is an image",})
        self.assertEqual(html.props_to_html(), ' src="image.jpg" alt="This is an image"')


    def test_propr_to_html3(self):
        html = HtmlNode(props={"color" : "green", "font-size" : "1 rem",})
        self.assertEqual(html.props_to_html(), ' color="green" font-size="1 rem"')


    def test_values(self):

        html_node = HtmlNode(tag="div", value="Some text here")

        self.assertEqual(html_node.tag, "div")
        self.assertEqual(html_node.value, "Some text here")
        self.assertEqual(html_node.props, None)
        self.assertEqual(html_node.childern, None)


    def test_repr(self):
        html_node = HtmlNode(tag="p", 
                             value="This is a paragraph", 
                             childern=None, 
                             props={"text-align" : "center", "color" : "grey",}
                             )

        self.assertEqual(html_node.__repr__(), 
                        "HtmlNode(p, This is a paragraph, childern: None, {'text-align': 'center', 'color': 'grey'})")


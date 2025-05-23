
import unittest
from htmlnode import ParentNode, LeafNode


class Test_ParentNode(unittest.TestCase):

    def test_to_html_with_childern(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    
    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )


    
    def test_to_html_with_props(self):
        node = ParentNode("p", [LeafNode("b", "Bold text"), 
                                LeafNode("a", "Link text", {"href" : "https://www.google.com"}),
                                ])
        self.assertEqual(node.to_html(), '<p><b>Bold text</b><a href="https://www.google.com">Link text</a></p>')



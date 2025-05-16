
import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, World!")
        self.assertEqual(node.to_html(), "<p>Hello, World!</p>")

    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click Me!", {"href" : "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click Me!</a>')


    def test_leaf_no_tag(self):
        node = LeafNode(None, "Some texts")
        self.assertEqual(node.to_html(), "Some texts")


    #def test_leaf_no_value(self):
        #node = LeafNode("p", "")
        #self.assertEqual(node.to_html(), "Must have value")



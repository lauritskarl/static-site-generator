import unittest

from htmlnode import LeafNode, ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        tag = "p"
        leaf1 = LeafNode(tag="p", value="Just some text.")
        children = [leaf1]
        node = ParentNode(tag, children)
        self.assertEqual(node.to_html(), '<p><p>Just some text.</p></p>')

    def test_to_html_many_children(self):
        tag = "p"
        leaf1 = LeafNode(tag="p", value="Just some text.")
        leaf2 = LeafNode(tag="p", value="Just some text.")
        leaf3 = LeafNode(tag="p", value="Just some text.")
        children = [leaf1, leaf2, leaf3]
        node = ParentNode(tag, children)
        self.assertEqual(node.to_html(), '<p><p>Just some text.</p><p>Just some text.</p><p>Just some text.</p></p>')

    def test_to_html_different_children(self):
        tag = "p"
        leaf1 = LeafNode(tag="p", value="This is a paragraph of text.")
        leaf2 = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        leaf3 = LeafNode(value="This is a paragraph of text.")
        children = [leaf1, leaf2, leaf3]
        node = ParentNode(tag, children)
        self.assertEqual(node.to_html(), '<p><p>This is a paragraph of text.</p><a href="https://www.google.com">Click me!</a>This is a paragraph of text.</p>')

    def test_to_html_with_props(self):
        tag = "a"
        leaf1 = LeafNode(tag="p", value="Just some text.")
        leaf2 = LeafNode(tag="p", value="Just some text.")
        leaf3 = LeafNode(tag="p", value="Just some text.")
        children = [leaf1, leaf2, leaf3]
        props = {"href": "https://www.google.com"}
        node = ParentNode(tag, children, props)
        self.assertEqual(node.to_html(), '<a href="https://www.google.com"><p>Just some text.</p><p>Just some text.</p><p>Just some text.</p></a>')

    def test_to_html_children_with_props(self):
        tag = "p"
        leaf1 = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        leaf2 = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        leaf3 = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        children = [leaf1, leaf2, leaf3]
        node = ParentNode(tag, children)
        self.assertEqual(node.to_html(), '<p><a href="https://www.google.com">Click me!</a><a href="https://www.google.com">Click me!</a><a href="https://www.google.com">Click me!</a></p>')

    def test_to_html_parent_and_children_with_props(self):
        tag = "a"
        leaf1 = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        leaf2 = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        leaf3 = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        children = [leaf1, leaf2, leaf3]
        props = {"href": "https://www.google.com"}
        node = ParentNode(tag, children, props)
        self.assertEqual(node.to_html(), '<a href="https://www.google.com"><a href="https://www.google.com">Click me!</a><a href="https://www.google.com">Click me!</a><a href="https://www.google.com">Click me!</a></a>')

    def test_to_html_parent_in_parent_node(self):
        parent = ParentNode(tag="p", children=[LeafNode(tag="p", value="Just some text.")])
        node = ParentNode(tag="p", children=[parent])
        self.assertEqual(node.to_html(), '<p><p><p>Just some text.</p></p></p>')

    def test_to_html_no_tag(self):
        leaf1 = LeafNode(tag="p", value="Just some text.")
        children = [leaf1]
        node = ParentNode("", children)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_no_children(self):
        tag = "p"
        node = ParentNode(tag, [])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_no_tag_and_no_children(self):
        node = ParentNode("", [])
        with self.assertRaises(ValueError):
            node.to_html()

        
if __name__ == "__main__":
    unittest.main()

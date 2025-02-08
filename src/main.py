from src.extract_markdown import extract_markdown_images, extract_markdown_links
from textnode import TextType, TextNode
from htmlnode import LeafNode


def main():
    text = "This is a text node"
    text_type = TextType.BOLD
    url = "https://www.boot.dev"
    text_node = TextNode(text, text_type, url)
    print(text_node)


def text_node_to_html_node(text_node: TextNode):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(value=text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode(tag="b", value=text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="i", value=text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode(
            tag="img", value="", props={"src": text_node.url, "alt": text_node.text}
        )
    raise Exception("TextNode is none of predefined types")


if __name__ == "__main__":
    main()

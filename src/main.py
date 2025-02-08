from textnode import TextType, TextNode
from htmlnode import LeafNode
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link


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


def text_to_textnodes(text):
    input_nodes = [TextNode(text, TextType.TEXT)]
    bold_split = split_nodes_delimiter(input_nodes, "**")
    italic_split = split_nodes_delimiter(bold_split, "*")
    code_split = split_nodes_delimiter(italic_split, "`")
    image_split = split_nodes_image(code_split)
    link_split = split_nodes_link(image_split)
    return link_split


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = [block.strip() for block in blocks if block.strip()]
    return filtered_blocks


def block_to_block_type(block):
    if block.startswith("#"):
        splits = block.split(" ")
        if splits[0].count("#") <= 6:
            return "heading"
    elif block.startswith("```") and block.endswith("```"):
        return "code"
    elif block.startswith(">"):
        if all(line.startswith(">") for line in block.split("\n")):
            return "quote"
    elif block.startswith("* ") or block.startswith("- "):
        if all(line.startswith("* ") or line.startswith("- ") for line in block.split("\n")):
            return "unordered_list"
    elif all(len(line.split('. ', 1)) > 1 and line.split('. ', 1)[0].isdigit() for line in block.split("\n")):
        return "ordered_list"
    return "paragraph"


if __name__ == "__main__":
    main()

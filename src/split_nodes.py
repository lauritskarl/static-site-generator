from textnode import TextType, TextNode
from extract_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        elif old_node.text.count(delimiter) != 2:
            raise Exception("Invalid Markdown syntax")
        else:
            old_node_parts = []
            old_node_text_parts = old_node.text.split(delimiter)
            old_node_parts.append(TextNode(old_node_text_parts[0], TextType.TEXT))
            if delimiter == "**":
                old_node_parts.append(TextNode(old_node_text_parts[1], TextType.BOLD))
            elif delimiter == "*":
                old_node_parts.append(TextNode(old_node_text_parts[1], TextType.ITALIC))
            elif delimiter == "`":
                old_node_parts.append(TextNode(old_node_text_parts[1], TextType.CODE))
            old_node_parts.append(TextNode(old_node_text_parts[2], TextType.TEXT))
            new_nodes.extend(old_node_parts)
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        current_text = old_node.text
        matches = extract_markdown_images(current_text)

        if not current_text:
            continue
        if not matches:
            new_nodes.append(old_node)
            continue
        for match in matches:
            image_alt, image_link = match
            image_markdown = f"![{image_alt}]({image_link})"
            parts = current_text.split(image_markdown, 1)

            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))

            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))

            if len(parts) > 1:
                current_text = parts[1]
            else:
                current_text = ""

        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        current_text = old_node.text
        matches = extract_markdown_links(current_text)

        if not current_text:
            continue
        if not matches:
            new_nodes.append(old_node)
            continue
        for match in matches:
            link_text, link = match
            link_markdown = f"[{link_text}]({link})"
            parts = current_text.split(link_markdown, 1)

            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))

            new_nodes.append(TextNode(link_text, TextType.LINK, link))

            if len(parts) > 1:
                current_text = parts[1]
            else:
                current_text = ""

        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))

    return new_nodes

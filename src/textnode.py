from enum import Enum


class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"


class TextNode:

    def __init__(
        self,
        text: str,
        text_type: TextType,
        url: str = "",
    ):
        if isinstance(text_type, str):
            try:
                text_type = TextType(text_type)
            except ValueError:
                raise ValueError("Invalid text_type provided.")
        self.text = text
        self.text_type = text_type
        self.url = url if url else ""

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return (
                self.text == other.text
                and self.text_type == other.text_type
                and self.url == other.url
            )
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

from typing import Sequence


class HTMLNode:
    def __init__(
        self,
        tag: str = "",
        value: str = "",
        children: Sequence["HTMLNode"] = (),
        props: dict[str, str] = {},
    ):
        self.tag = tag if tag else ""
        self.value = value if value else ""
        self.children = list(children)
        self.props = props if props else {}

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props:
            return " ".join([f'{prop}="{value}"' for prop, value in self.props.items()])
        return ""

    def __repr__(self):
        return f"HTMLNode: {self.tag}, {self.value}, {self.children}, {self.props}"


class LeafNode(HTMLNode):
    def __init__(
        self,
        value: str,
        tag: str = "",
        props: dict[str, str] = {},
    ):
        super().__init__(
            tag=tag if tag else "",
            value=value,
            props=props if props else {},
        )

    def __eq__(self, other):
        if isinstance(other, LeafNode):
            return (
                self.tag == other.tag
                and self.value == other.value
                and self.props == other.props
            )
        return False

    def to_html(self):
        if not self.value:
            raise ValueError
        if not self.tag:
            return self.value
        if not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: Sequence["HTMLNode"],
        props: dict[str, str] = {},
    ):
        super().__init__(tag=tag, children=children, props=props if props else {})

    def to_html(self):
        if not self.tag:
            raise ValueError("Missing tag parameter")
        if not self.children:
            raise ValueError("Missing children parameter")
        result = ""
        for child in self.children:
            result += child.to_html()
        if not self.props:
            return f"<{self.tag}>{result}</{self.tag}>"
        return f"<{self.tag} {self.props_to_html()}>{result}</{self.tag}>"

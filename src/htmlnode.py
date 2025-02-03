class HTMLNode:
    def __init__(
        self,
        tag: str = None,
        value: str = None,
        children: list["HTMLNode"] = None,
        props: dict[str: str] = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

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
        tag: str = None,  # Optional
        value: str = None,  # Required
        props: dict[str: str] = None  # Optional
    ):
        super().__init__(
            tag=tag,
            value=value,
            props=props,
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
            return f'<{self.tag}>{self.value}</{self.tag}>'
        return f'<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>'


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,  # Required
        children: list["HTMLNode"],  # Required
        props: dict[str: str] = None  # Optional
    ):
        super().__init__(
            tag=tag,
            children=children,
            props=props
        )

    def to_html(self):
        if not self.tag:
            raise ValueError("Missing tag parameter")
        if not self.children:
            raise ValueError("Missing children parameter")
        result = ""
        for child in self.children:
            result += child.to_html()
        if not self.props:
            return f'<{self.tag}>{result}</{self.tag}>'
        return f'<{self.tag} {self.props_to_html()}>{result}</{self.tag}>'

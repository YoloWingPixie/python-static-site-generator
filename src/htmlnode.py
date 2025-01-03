from typing import Optional


class HTMLNode:
    def __init__(
        self,
        value: Optional[str] = None,
        tag: Optional[str] = None,
        children: Optional[list["HTMLNode"]] = None,
        props: Optional[dict] = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        return " ".join([f'{key}="{value}"' for key, value in self.props.items()])

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, other: "HTMLNode") -> bool:
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )


class LeafNode(HTMLNode):
    def __init__(
        self,
        value: str = None,
        tag: Optional[str] = None,
        props: Optional[dict] = None,
    ):
        super().__init__(value=value, tag=tag, children=[], props=props)

        if self.tag is not None:
            if "img" not in self.tag:
                if not value:
                    raise ValueError("LeafNode must have a value")

    def to_html(self):
        beginning = f"<{self.tag} {self.props_to_html()}>"
        value = self.value or ""
        end = f"</{self.tag}>" if self.tag != "img" else ""
        return f"{beginning}{value}{end}"


class ParentNode(HTMLNode):
    def __init__(
        self, tag: str, children: list[HTMLNode], props: Optional[dict] = None
    ):
        super().__init__(value=None, tag=tag, children=children, props=props)
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have children")

    def to_html(self):
        children_html = "".join([child.to_html() for child in self.children])
        return f"<{self.tag} {self.props_to_html()}>{children_html}</{self.tag}>"

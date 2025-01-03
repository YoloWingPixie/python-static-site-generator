from enum import Enum
from typing import Optional

from htmlnode import LeafNode


class TextType(Enum):
    NORMAL = 1
    BOLD = 2
    ITALIC = 3
    CODE = 4
    LINK = 5
    IMAGE = 6


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: Optional[str] = None):
        self.text = text
        self.text_type = text_type
        self.url = url or ""

        if not isinstance(text_type, TextType):
            raise ValueError("Invalid TextType")

        if text_type == TextType.LINK and not url:
            raise ValueError("Link must have a URL")

        if text_type == TextType.IMAGE and not url:
            raise ValueError("Image must have a URL")

    def __eq__(self, other: "TextNode") -> bool:
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    def to_html_node(self):
        if self.text_type == TextType.NORMAL:
            return LeafNode(self.text, "p")
        elif self.text_type == TextType.BOLD:
            return LeafNode(self.text, "b")
        elif self.text_type == TextType.ITALIC:
            return LeafNode(self.text, "i")
        elif self.text_type == TextType.CODE:
            return LeafNode(self.text, "code")
        elif self.text_type == TextType.LINK:
            if not self.url:
                raise ValueError("Link must have a URL")
            return LeafNode(self.text, "a", {"href": self.url})
        elif self.text_type == TextType.IMAGE:
            if not self.url:
                raise ValueError("Image must have a URL")
            return LeafNode(None, "img", {"src": self.url, "alt": self.text})
        else:
            raise ValueError("Invalid TextType")

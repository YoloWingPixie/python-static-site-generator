from textnode import TextNode, TextType


def main():
    text = "Hello, world!"
    node = TextNode(text, TextType.Normal, "")
    print(node)


if __name__ == "__main__":
    main()

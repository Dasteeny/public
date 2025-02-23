from text_node import TextNode, TextType


def main():
    text_node = TextNode("This is a text node", TextType.BOLD, "http://www.boot.dev")
    print(text_node)


main()

import os

from markdown_blocks import markdown_to_html_node


def extract_title(markdown: str):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")


def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as file:
        markdown = file.read()

    html_str = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    with open(template_path) as file:
        template = file.read()

    page = template.replace("{{ Title }}", title).replace("{{ Content }}", html_str)

    with open(dest_path, "w+") as file:
        file.write(page)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if os.path.isfile(dir_path_content):
        filename = dest_dir_path.replace(".md", ".html")
        print(f"{dir_path_content=}, {filename=}")
        generate_page(dir_path_content, template_path, filename)
        return
    for content_dir in os.listdir(dir_path_content):
        dest_path = os.path.join(dest_dir_path, content_dir)
        os.mkdir(dest_path)
        generate_pages_recursive(
            os.path.join(dir_path_content, content_dir), template_path, dest_path
        )

import os
import shutil

from markdown_blocks import markdown_to_html_node


def main():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    public = os.path.join(project_root, "public")
    static = os.path.join(project_root, "static")
    if os.path.exists(public):
        shutil.rmtree(public)
    copy_static_to_public(public, static)
    from_path = os.path.join(project_root, "content/index.md")
    template_path = os.path.join(project_root, "template.html")
    dest_path = os.path.join(public, "index.html")
    generate_page(from_path, template_path, dest_path)
    print(os.listdir(public))


def copy_static_to_public(public_path, static_path):
    if not os.path.exists(public_path):
        os.mkdir(public_path)
    for item in os.listdir(static_path):
        dst_item = os.path.join(public_path, item)
        src_item = os.path.join(static_path, item)
        if os.path.isfile(src_item):
            print(f"Copying {src_item} to {dst_item}")
            shutil.copy2(src_item, dst_item)
        elif os.path.isdir(src_item):
            print(f"Copying folder {src_item} to {dst_item}")
            os.mkdir(dst_item)
            copy_static_to_public(dst_item, src_item)
            # shutil.copytree(src_item, dst_item)  # This replaces the recursive call


def extract_title(markdown):
    for line in markdown.splitlines():
        if line.startswith("#"):
            return line.split("#")[1].strip()
    raise Exception("Title not found")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r", encoding="utf-8") as f:
        markdown = f.read()

    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)

    dest_directory = os.path.dirname(dest_path)
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(template)


if __name__ == "__main__":
    main()

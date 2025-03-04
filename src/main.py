import os
import shutil

from page_generator import generate_pages_recursive

DIR_PATH_STATIC = "./static"
DIR_PATH_PUBLIC = "./public"
DIR_PATH_CONTENT = "./content"
TEMPLATE_PATH = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(DIR_PATH_PUBLIC):
        shutil.rmtree(DIR_PATH_PUBLIC)

    print("Copying static files to public directory...")
    copy_all(DIR_PATH_STATIC, DIR_PATH_PUBLIC)

    generate_pages_recursive(DIR_PATH_CONTENT, TEMPLATE_PATH, DIR_PATH_PUBLIC)


def copy_all(src, dst):
    if not os.path.exists(dst):
        os.mkdir(dst)

    for filename in os.listdir(src):
        from_path = os.path.join(src, filename)
        to_path = os.path.join(dst, filename)
        print(f" * {from_path} -> {to_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)
        else:
            copy_all(from_path, to_path)


if __name__ == "__main__":
    main()

import os
import shutil


def main():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    public = os.path.join(project_root, 'public')
    static = os.path.join(project_root, 'static')
    if os.path.exists(public):
        shutil.rmtree(public)
    copy_static_to_public(public, static)
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


if __name__ == '__main__':
    main()
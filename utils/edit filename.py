# _*_coding:utf-8_*_
# __author: a123456
import os
import re

base_dir = ""


def main(path):
    """修改文件名脚本"""
    for path, dirs, files in os.walk(path):
        if {"env", ".git"} & set(path.split("/")):
            continue

        for filename in files:
            if re.search(r"^\d+_", filename):
                new_name = filename.replace("_", ".", 1).replace("_", " ").replace(".python", ".py")
                os.rename(f"{path}/{filename}", f"{path}/{new_name}")


if __name__ == '__main__':
    main(base_dir)

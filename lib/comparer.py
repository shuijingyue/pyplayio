import os


def readdirs(path: str) -> None:
    print(path)

    if os.path.isdir(path):
        for file in os.listdir(path):
            readdirs(os.path.join(path, file))
    else:
        with open(path, 'r', encoding="utf-8") as file:
            print(file.read(100))
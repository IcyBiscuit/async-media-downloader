import pathlib
import sys

BASE_DIR = pathlib.Path(__file__).parent.parent.parent


def setBasePath():
    sys.path.append(BASE_DIR.as_posix())


if __name__ == "__main__":
    setBasePath()
    print(sys.path)

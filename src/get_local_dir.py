import os


def src(filename: str = None):
    return os.path.join(os.path.dirname(__file__), filename)

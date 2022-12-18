import os


def src(filename: str = None):
    """Function to get directory of local file and append a string to it if needed.

    Args:
        filename (str, optional): appends string to file/directory address. Defaults to None.

    Returns:
        string: file location as string
    """
    dir_of_self = os.path.dirname(__file__)
    parent_dir = os.path.join(dir_of_self,os.pardir)
    return os.path.join(parent_dir,filename)
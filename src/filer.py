# Filer is a small utility script that can do things related to files. (that is why it is called filer)
from os import write
from pathlib import Path

def filing(file_path_str: str, create_file: bool = False, write_contents: str = "0") -> bool:
    """filing: Check if a file exists, create it on specification

    Args:
        file_path_str (str): The path to the desired file
        create_file (bool, optional): If file_path_str does not exist, create it. Defaults to False.

    Returns:
        bool: True if file exists, False if didn't and was created
    """
    
    file_path_str = Path(file_path_str)
    if file_path_str.is_file():
        return True
    
    elif create_file:
        with open(file_path_str, 'w') as f:
            f.write(write_contents)
            f.close()
            return False

    return False
        
def read_file(file_path: str) -> str:
    """Read the contents of a file and return them.

    Args:
        file_path (str): The path to the file to be read

    Returns:
        str: The contents of the file
    """

    with open(file_path, 'r') as f:
        f_contents = f.read()
        f.close()
        return f_contents

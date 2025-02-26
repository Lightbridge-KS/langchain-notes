__all__ = ['list_dir', 'read_text_dir', 'read_text_file', 'write_text_file']

import os
import pickle
from pathlib import Path

def list_dir(directory, pattern: str = "", recursive = True) -> list[Path]:
    path = Path(directory)
    if recursive:
        return list(path.rglob(pattern))
    else:
        return list(path.glob(pattern))


def read_text_dir(dir_path):
    """Read all text files in a directory and return their contents in a dictionary.

    Parameters
    ----------
    dir_path : str or Path
        Path to the directory containing text files.

    Returns
    -------
    dict
        Dictionary with filenames as keys and file contents as values, sorted by filename.

    Raises
    ------
    FileNotFoundError
        If the specified directory does not exist.
    NotADirectoryError
        If the specified path is not a directory.
    """
    dir_path = Path(dir_path)

    # Validate that the path exists and is a directory
    if not dir_path.exists():
        raise FileNotFoundError(f"The directory '{dir_path}' does not exist.")
    if not dir_path.is_dir():
        raise NotADirectoryError(f"The path '{dir_path}' is not a directory.")

    # Get the list of files in the directory
    file_ls = [f for f in os.listdir(dir_path) if not f.startswith('.')] 

    # Construct full file paths
    path_ls = [dir_path / file for file in file_ls]

    # Read contents of each file, with error handling
    content_dict = {}
    for file, path in zip(file_ls, path_ls):
        try:
            content_dict[file] = read_text_file(path)
        except Exception as e:
            print(f"Error reading file '{file}': {e}")
            continue
    # Sort the dictionary by keys
    sorted_content_dict = dict(sorted(content_dict.items()))
    return sorted_content_dict


def read_text_file(file_path):    
    """Read a text file and return its content as a string.

    This function attempts to read a text file from the specified path using UTF-8 encoding.

    Args:
        file_path (str or Path): The path to the text file to be read.

    Returns:
        str: The content of the text file as a string if successful.
        None: If the file is not found or an error occurs during reading.

    Raises:
        FileNotFoundError: If the specified file path does not exist.
        Exception: For other possible errors during file reading operations.
    """
    file_path = Path(file_path)
    try:
        # Open the text file in read mode
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read the entire file content into a string
            text_content = file.read()
            return text_content
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def write_text_file(text, file_path):    
    """Write text content to a file at the specified path.

    This function takes a string of text and writes it to a file, creating the file if it
    doesn't exist or overwriting it if it does. The file is written using UTF-8 encoding.

    Args:
        text (str): The text content to be written to the file.
        file_path (str | Path): The path where the file should be created/written to.

    Raises:
        Exception: Any exception that occurs during file operations will be caught and printed.

    Example:
        >>> write_text_file("Hello World", "output.txt")
        Text successfully written to output.txt
    """
    file_path = Path(file_path)
    try:
        # Open the text file in write mode
        with open(file_path, 'w', encoding='utf-8') as file:
            # Write the string of text to the file
            file.write(text)
        print(f"Text successfully written to {file_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")


def write_pickle(obj, filename: str):
    """
    Write a Python object to a pickle file.

    Parameters
    ----------
    obj : any
        The Python object to save
    filename : str
        Path to the pickle file (e.g., 'data.pkl')

    Returns
    -------
    None
    """
    with open(filename, 'wb') as file:  # 'wb' for write binary mode
        pickle.dump(obj, file)

# Read the object from the file
def read_pickle(filename: str):
    """
    Read a Python object from a pickle file.

    Parameters
    ----------
    filename : str
        Path to the pickle file (e.g., 'data.pkl')

    Returns
    -------
    any
        The loaded Python object
    """
    with open(filename, 'rb') as file:  # 'rb' for read binary mode
        return pickle.load(file)
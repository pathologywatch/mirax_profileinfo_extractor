import os
import ctypes
from pathlib import Path

# Load the shared library
cur_dir = Path(os.path.dirname(os.path.abspath(__file__)))
lib = ctypes.CDLL(os.path.join(cur_dir, "libprofileinfo_extractor.so"))


# Define the structure in Python
class Attribute(ctypes.Structure):
    _fields_ = [("key", ctypes.c_char * 100),
                ("value", ctypes.c_char * 100)]


# Define the return type and argument types for the function
lib.extract_attributes_from_directory.restype = ctypes.POINTER(Attribute)
lib.extract_attributes_from_directory.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_int)]


def _extract_attributes_from_directory(directory):
    count = ctypes.c_int()
    attributes_ptr = lib.extract_attributes_from_directory(directory.encode('utf-8'), ctypes.byref(count))

    attributes_list = [attributes_ptr[i] for i in range(count.value)]

    # Convert the list of Attribute objects to a dictionary
    result = {}
    for attr in attributes_list:
        result[attr.key.decode('utf-8')] = attr.value.decode('utf-8')

    # Free the allocated memory in C
    lib.free(attributes_ptr)

    return result


def get_mirax_profile_info(mirax_file):
    file = Path(mirax_file).resolve()
    data_content = file.parent / file.stem
    return _extract_attributes_from_directory(str(data_content))


if __name__ == '__main__':
    folder = input("Enter the path to the mirax file: ")
    properties = get_mirax_profile_info(folder)
    print("Extracted properties:", properties)

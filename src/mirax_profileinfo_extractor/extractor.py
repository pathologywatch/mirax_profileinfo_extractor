import sys
import ctypes
from pathlib import Path


def load_library(libname):
    # Detect the platform and adjust the library name
    if sys.platform == "win32":
        libname = libname + ".dll"
    elif sys.platform == "darwin":  # macOS
        libname = "lib" + libname + ".dylib"
    else:  # Assume Linux or similar
        libname = "lib" + libname + ".so"

    # Construct the path to the library based on the current file's location (within the package)
    path_within_package = Path(__file__).parent / libname

    # Check if the library exists within the package directory
    if path_within_package.exists():
        path = path_within_package
    else:
        # If not, check the broader site-packages directory
        path = Path(__file__).parent.parent / libname
        if not path.exists():
            raise Exception(f"Library {libname} not found in expected locations")

    # Load the library
    return ctypes.CDLL(str(path))


# Load the library
lib = load_library("profileinfo_extractor")


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

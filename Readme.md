# Mirax profile info extractor

This simple lib helps extract extra information from Mirax files that are not provided by other open source libraries like
[Openslide](https://github.com/openslide/openslide).

# How to use?

Add the lib to your project from pypi and call the function `get_mirax_profile_info` passing the path to the file as parameter.

```python
from mirax_profileinfo_extractor import get_mirax_profile_info

mirax_info = get_mirax_profile_info('path/to/file.mrxs')
```
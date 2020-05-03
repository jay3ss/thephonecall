"""
Converts images of the memorandum into text and saves the text into
memorandum.txt

This script expects that the images to be the only images in the
directory.
"""
import pathlib
import sys

from PIL import Image
import pyocr
import pyocr.builders


tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

# The tools are returned in the recommended order of usage
tool = tools[0]
print(f'Will use tool "{tool.get_name()}"')

langs = tool.get_available_languages()
print(f'Available languages: {", ".join(langs)}')
lang = langs[1]
print(f'Will use lang "{lang}"')

if len(sys.argv) <= 1:
    img_path = "."
else:
    img_path = sys.argv[1]

img_paths = list(pathlib.Path.cwd().glob("*png"))

# create a list of text extracted from the images
txts = []
with open("memorandum.txt", "w") as f:
    for img in sorted(img_paths):
        txt = tool.image_to_string(
            Image.open(img), lang=lang, builder=pyocr.builders.TextBuilder()
        )
        f.write(txt)

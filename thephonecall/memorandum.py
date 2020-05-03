"""Contains a Python string of the text of the memorandum"""
import pkgutil


text =  pkgutil.get_data(__name__, "data/memorandum-cleaned.txt").decode()

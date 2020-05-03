"""Contains a Python string of the text of the memorandum"""
import pkgutil


raw_text =  pkgutil.get_data(__name__, "data/memorandum-cleaned.txt").decode()

def text_as_dictionary():
    lines = raw_text.split('\n')
    lines_filtered = [line for line in lines if line]

    text = {
        'meta': {
            'classification': lines_filtered[0],
            'published': lines_filtered[2],
            'title': lines_filtered[3],
            'subject': lines_filtered[4],
            'participants': lines_filtered[5],
            'notetakers': lines_filtered[6],
            'date_time': lines_filtered[7],
            'place': lines_filtered[8],
            'caution': '\n'.join(lines_filtered[9:16]),
            'classified_by': lines_filtered[16],
            'derived_from': lines_filtered[17],
            'declassified_on': lines_filtered[18]
        },
        'body': '\n'.join(lines[29:])
    }
    return text

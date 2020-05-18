import PIL
import telebot as tb
from pyes import consts


def get_type(mime_type):
    return mime_type.split('/')[1]


def gen_list_of_formats():
    res = ""
    for keys in consts.formats:
        res += '\n'.join(consts.formats[keys]) + '\n'
    return res


def from_video_note_to_smth(needed_type):
    pass

import PIL
import telebot as tb
from pyes import consts


def gen_list_of_formats():
    res = ""
    for keys in consts.formats:
        res += '\n'.join(consts.formats[keys]) + '\n'
    return res


def from_ogg_to_mp3(file_path):
    pass



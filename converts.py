import PIL
import telebot as tb
from pyes import consts


def gen_list_of_formats():
    res = ""
    for keys in consts.formats:
        res += '\n'.join(consts.formats[keys]) + '\n'
    return res


def from_mp3_to_ogg(file_path):
    pass


def from_ogg_to_mp3(file_path):
    pass


def from_jpg_to_png(file_path):
    pass


def from_png_to_jpg(file_path):
    pass


def from_docx_to_pdf(file_path):
    pass

from bot_config import bot
from pyes import consts
from pyes import markups as mp
from PIL import Image
import docx2pdf
import docx2txt


def get_type(name):
    # gets word after last '.'
    return name.split('.')[len(name.split('.')) - 1]


def ans_doc(message):
    bot.send_message(message.from_user.id, "We're processing your request...")
    file_id = message.document.file_id
    file_info = bot.get_file(file_id)
    file = bot.download_file(file_info.file_path)
    file_name = message.document.file_name
    file_path = consts.dir_path + file_name
    with open(file_path, 'wb') as new_file:
        new_file.write(file)

    file_type = get_type(message.document.file_name)

    if file_type in consts.formats['photo']:

        def image_processing(msg):
            nonlocal file_path, file_type
            convert_to = msg.text
            convert_img(file_path, file_type, convert_to, msg.from_user.id)

        msg = bot.send_message(message.from_user.id, consts.file_ans,
                               reply_markup=mp.gen_mrkp(file_type, consts.formats['photo']))
        bot.register_next_step_handler(msg, image_processing)
    elif file_type in consts.formats['video']:
        pass
    elif file_type in consts.formats['text_document']:

        def doc_processing(msg):
            nonlocal file_path, file_type
            convert_to = msg.text
            convert_text_doc(file_path, file_type, convert_to, msg.from_user.id)

        msg = bot.send_message(message.from_user.id, consts.file_ans,
                               reply_markup=mp.gen_mrkp(file_type, consts.formats['text_document']))
        bot.register_next_step_handler(msg, doc_processing)


def convert_text_doc(file_path, file_type, convert_to, user_id):
    file = None
    new_file_path = file_path.replace(file_type, convert_to)
    if file_type == 'docx' and convert_to == 'pdf':
        docx2pdf.convert(file_path, new_file_path)
        file = open(new_file_path, 'rb')

    if file_type == 'docx' and convert_to == 'txt':
        text = docx2txt.process(file_path)
        with open(new_file_path, 'w') as new_file:
            new_file.write(text)
        file = open(new_file_path, 'r')

    bot.send_document(user_id, file)


def convert_img(file_path, file_type, convert_to, user_id):
    im = Image.open(file_path)
    new_file_path = file_path.replace(file_type, convert_to)
    # print(file_path, new_file_path)
    if file_type == 'png' and convert_to == 'jpg':
        rgb_im = im.convert('RGB')
        rgb_im.save(new_file_path, "JPEG", quality=100)

    if file_type == 'jpg' and convert_to == 'png':
        rgba_im = im.convert('RGBA')
        rgba_im.save(new_file_path, "PNG", quality=100)

    if file_type == 'jpg' and convert_to == 'ico':
        rgba_im = im.convert('RGBA')
        rgba_im.save(new_file_path, "ICO", quality=100)

    if file_type == 'png' and convert_to == 'ico':
        im.save(new_file_path, "ICO", quality=100)

    if file_type == 'ico' and convert_to == 'png':
        try:
            im.save(new_file_path, "PNG", quality=100)
        except:
            pass

    if file_type == 'ico' and convert_to == 'jpg':
        try:
            rgb_im = im.convert('RGB')
            rgb_im.save(new_file_path, "JPEG", quality=100)
        except:
            pass

    if file_type == 'jpg' and convert_to == 'bmp':
        im.save(new_file_path, "BMP", quality=100)

    if file_type == 'bmp' and convert_to == 'jpg':
        rgb_im = im.convert('RGB')
        rgb_im.save(new_file_path, "JPEG", quality=100)

    if file_type == 'png' and convert_to == 'bmp':
        im.save(new_file_path, "BMP", quality=100)

    if file_type == 'bmp' and convert_to == 'png':
        im.save(new_file_path, "PNG", quality=100)

    if file_type == 'ico' and convert_to == 'bmp':
        try:
            im.save(new_file_path, "BMP", quality=100)
        except:
            pass

    if file_type == 'bmp' and convert_to == 'ico':
        im.save(new_file_path, "ICO", quality=100)
    file = open(new_file_path, 'rb')
    bot.send_document(user_id, file)

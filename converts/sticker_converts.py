from bot_config import bot
from pyes import consts
from pyes import markups as mp


def ans_sticker(message):
    bot.send_message(message.from_user.id, "We're processing your request...")
    file_id = message.sticker.file_id
    file_info = bot.get_file(file_id)
    file = bot.download_file(file_info.file_path)
    file_name = 'unknown.'
    msg = None
    file_type = None

    def sticker_processing(msg):
        nonlocal file_type, file
        flag = 1
        file_type = msg.text
        if msg.text == 'sticker without its pack':
            file_type = 'png'
            flag = 0
        file_path = consts.dir_path + file_name + file_type
        with open(file_path, 'wb') as new_file:
            new_file.write(file)
        file = open(file_path, 'rb')
        if flag:
            bot.send_document(msg.from_user.id, file)
        else:
            bot.send_sticker(msg.from_user.id, file)

    def animated_sticker_processing(msg):
        nonlocal file_type, file
        if msg.text == 'sticker without its pack':
            file_type = 'tgs'
        file_path = consts.dir_path + file_name + file_type
        with open(file_path, 'wb') as new_file:
            new_file.write(file)
        file = open(file_path, 'rb')
        bot.send_document(msg.from_user.id, file)

    if message.sticker.is_animated:
        msg = bot.send_message(message.from_user.id, consts.file_ans,
                               reply_markup=mp.gen_mrkp('', consts.formats['animated_sticker']))
        bot.register_next_step_handler(msg, animated_sticker_processing)
    else:
        msg = bot.send_message(message.from_user.id, consts.file_ans,
                               reply_markup=mp.gen_mrkp('', consts.formats['sticker']))
        bot.register_next_step_handler(msg, sticker_processing)
from pyes import consts
from pyes import markups as mp
from bot_config import bot


def ans_voice(message):
    msg1 = bot.send_message(message.from_user.id, consts.file_ans,
                            reply_markup=mp.gen_mrkp('voice', consts.formats['voice']))

    def ans_mrkp_voice(to_type):
        # if to_type.text == 'mp3':
        file_id = message.voice.file_id
        file_info = bot.get_file(file_id)
        file = bot.download_file(file_info.file_path)
        file_name = 'unknown'
        file_path = consts.dir_path + file_name + '.' + to_type.text
        with open(file_path, 'wb') as new_file:
            new_file.write(file)
        send_from_voice(to_type.from_user.id, to_type.text, file_path)

    bot.register_next_step_handler(msg1, ans_mrkp_voice)


def send_from_voice(user_id, file_type, file_path):
    file = open(file_path, 'rb')
    if file_type == 'mp3':
        bot.send_audio(user_id, file)
    else:
        bot.send_document(user_id, file)
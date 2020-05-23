from bot_config import bot
from pyes import consts
from pyes import markups as mp


def ans_audio(message):
    bot.send_message(message.from_user.id, "We're processing your request...")

    def audio_file_procession(msg):
        file_id = message.audio.file_id
        file_info = bot.get_file(file_id)
        file = bot.download_file(file_info.file_path)
        file_name = message.audio.title + '.'
        file_type = msg.text
        file_path = consts.dir_path + file_name + file_type
        if file_type == 'voice':
            file_path.replace(file_type, 'ogg')
        with open(file_path, 'wb') as new_file:
            new_file.write(file)

        send_from_audio(msg.from_user.id, file_type, file_path)

    msg = bot.send_message(message.from_user.id, consts.file_ans,
                           reply_markup=mp.gen_mrkp('audio', consts.formats['audio']))
    bot.register_next_step_handler(msg, audio_file_procession)


def send_from_audio(user_id, file_type, file_path):
    file = open(file_path, 'rb')
    if file_type == 'voice':
        bot.send_voice(user_id, file)
    elif file_type == 'mp3':
        bot.send_audio(user_id, file)
    else:
        bot.send_document(user_id, file)
    file.close()
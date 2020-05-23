from bot_config import bot
from pyes import consts
from pyes import markups as mp


def ans_video(message):
    bot.send_message(message.from_user.id, "We're processing your request...")

    def video_message_processing(msg):
        file_id = message.video.file_id
        file_info = bot.get_file(file_id)
        file = bot.download_file(file_info.file_path)
        file_name = 'unknown.'
        file_type = msg.text
        file_path = file_name + file_type
        with open(file_path, 'wb') as new_file:
            new_file.write(file)
        send_from_video(msg.from_user.id, file_type, file_path)

    msg = bot.send_message(message.from_user.id, consts.file_ans,
                           reply_markup=mp.gen_mrkp('video', consts.formats['video']))
    bot.register_next_step_handler(msg, video_message_processing)


def send_from_video(user_id, file_type, file_path):
    file = open(file_path, 'rb')
    if file_type == 'mp4' or file_type == 'mov':
        bot.send_video(user_id, file)
    elif file_type == 'video_note':
        bot.send_message(user_id, 'Sorry, we cannot do it yet')
    else:
        bot.send_document(user_id, file)

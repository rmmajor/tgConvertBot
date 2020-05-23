from bot_config import bot
from pyes import consts
from pyes import markups as mp


def ans_video_note(message):
    bot.send_message(message.from_user.id, "We're processing your request...")
    file_type = ''

    def video_note_file_processing(msg):
        file_type = msg.text
        file_id = message.video_note.file_id
        file_info = bot.get_file(file_id)
        file = bot.download_file(file_info.file_path)
        file_name = 'unknown.'
        file_path = consts.dir_path + file_name + file_type
        with open(file_path, 'wb') as new_file:
            new_file.write(file)
        video = open(file_path, 'rb')
        bot.send_document(message.from_user.id, video)

    msg = bot.send_message(message.from_user.id, consts.file_ans,
                           reply_markup=mp.gen_mrkp('video_note', consts.formats['video_note']))
    bot.register_next_step_handler(msg, video_note_file_processing)
    print('done1')
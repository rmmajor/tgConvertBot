import telebot as tb
from pyes import consts
from pyes import markups as mp
from pyes import converts

bot = tb.TeleBot(consts.token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Bot converts your files into needed format\n"
                          "Send yor file please")
    # bot.send_message(message.from_user.id, 'Please select what do you like to convert',
    #                  reply_markup=mp.select_mode_mrkp)


@bot.message_handler(commands=['check_list'])
def send_list(message):
    ans = converts.gen_list_of_formats()
    bot.send_message(message.from_user.id, 'You can send one of the following types of files:')
    bot.send_message(message.from_user.id, ans)


@bot.message_handler(commands=['donate'])
def send_list(message):
    bot.send_message(message.from_user.id, 'Coming soon :)')


@bot.message_handler(content_types=['voice'])
def ans_voice(message):
    file_id = message.voice.file_id
    file_info = bot.get_file(file_id)
    file = bot.download_file(file_info.file_path)

    def set_voice_name(name):
        file_name = name.text
        file_path = consts.dir_path + file_name + '.ogg'
        with open(file_path, 'wb') as new_file:
            new_file.write(file)
        msg1 = bot.send_message(message.from_user.id, consts.file_ans,
                                reply_markup=mp.gen_mrkp('voice', consts.formats['voice']))

        def ans_mrkp_voice(to_type):
            if to_type.text == 'mp3':
                converts.from_ogg_to_mp3(file_path)

        bot.register_next_step_handler(msg1, ans_mrkp_voice)

    msg = bot.send_message(message.from_user.id, "Please send a name for your future audio file")
    bot.register_next_step_handler(msg, set_voice_name)


@bot.message_handler(content_types=['audio'])
def ans_audio(message):
    bot.send_message(message.from_user.id, "We're processing your request...")

    def audio_file_procession(msg):
        file_id = message.audio.file_id
        file_info = bot.get_file(file_id)
        file = bot.download_file(file_info.file_path)
        file_name = message.audio.title
        file_type = msg.text
        file_path = consts.dir_path + file_name + file_type
        if file_type == 'voice':
            file_path.replace(file_type, 'ogg')
        with open(file_path, 'wb') as new_file:
            new_file.write(file)

        send_from_mp3(msg.from_user.id, file_type, file_path)

    msg = bot.send_message(message.from_user.id, consts.file_ans,
                           reply_markup=mp.gen_mrkp('audio', consts.formats['audio']))
    bot.register_next_step_handler(msg, audio_file_procession)


def send_from_mp3(user_id, file_type, file_path):
    file = open(file_path, 'rb')
    if file_type == 'voice':
        bot.send_voice(user_id, file)
    elif file_type == 'mp3':
        bot.send_audio(user_id, file)
    else:
        bot.send_document(user_id, file)
    file.close()


@bot.message_handler(content_types=['video'])
def ans_video(message):
    bot.send_message(message.from_user.id, "We're processing your request...")
    file_id = message.video.file_id
    file_info = bot.get_file(file_id)
    file = bot.download_file(file_info.file_path)
    file_name = 'unknown.'
    file_type = converts.get_type(message.video.mime_type)
    if file_type not in consts.all_types:
        # bot.send_message(message.from_user.id, "")
        send_error(message)
    file_path = consts.dir_path + file_name + file_type
    with open(file_path, 'wb') as new_file:
        new_file.write(file)
    bot.send_message(message.from_user.id, consts.file_ans,
                     reply_markup=mp.gen_mrkp('video', consts.formats['video']))
    print('done')


@bot.message_handler(content_types=['video_note'])
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


@bot.message_handler(content_types=['photo'])
def ans_photo(message):
    bot.send_message(message.from_user.id, "Please send this as file, not as photo")


@bot.message_handler(func=lambda message: True)
def send_error(message):
    bot.send_message(message.from_user.id, "We don't support such file type.\n"
                                           "You can easily check the list of available formats "
                                           "by /check_list command")


bot.polling(none_stop=True, interval=0, timeout=0)

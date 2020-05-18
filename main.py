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
        # bot.register_next_step_handler(msg, ans_mrkp_voice(file_path=file_path))

        def ans_mrkp_voice(to_type):
            if to_type.text == 'mp3':
                converts.from_ogg_to_mp3(file_path)

        bot.register_next_step_handler(msg1, ans_mrkp_voice)

    msg = bot.send_message(message.from_user.id, "Please send a name for your future audio file")
    bot.register_next_step_handler(msg, set_voice_name)


# @bot.message_handler(content_types=['text'])


@bot.message_handler(content_types=['audio'])
def ans_audio(message):
    bot.send_message(message.from_user.id, consts.file_ans)
    bot.send_message(message.from_user.id, "тут потом має бути клавіатура")
    file_id = message.audio.file_id
    file_info = bot.get_file(file_id)
    file = bot.download_file(file_info.file_path)
    with open(consts.dir_path + 'new_file.mp3', 'wb') as new_file:
        new_file.write(file)


#############################################################################
# @bot.message_handler(content_types=['document'])
# def ans_audio(message):
#     bot.send_message(message.from_user.id, consts.file_ans)
#############################################################################


@bot.message_handler(func=lambda message: True)
def send_error(message):
    bot.send_message(message.from_user.id, "Just send us file.\n"
                                           "You can easily check the list of available formats "
                                           "by /check_list command")


bot.polling(none_stop=True, interval=0, timeout=0)

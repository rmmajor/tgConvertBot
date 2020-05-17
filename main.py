import telebot as tb
from pyes import consts
from pyes import markups as mp

bot = tb.TeleBot(consts.token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Bot converts your files into needed format"
                          "Send yor file please")
    # bot.send_message(message.from_user.id, 'Please select what do you like to convert',
    #                  reply_markup=mp.select_mode_mrkp)


@bot.message_handler(content_types=['voice', 'audio', 'document', 'photo', 'video', 'video_note'])
def ans_file(file):
    # bot.download_file('C:\\Users\\Major\\Desktop\\Progs\\tgConvertBot\\files\\')
    bot.send_message(file.from_user.id, "test text")


@bot.message_handler(func=lambda message: True)
def send_error(message):
    bot.send_message(message.from_user.id, "Just send us file.\n"
                                           "You can easily check the list of available formats "
                                           "by /check list command")


# @bot.callback_query_handler(func=lambda call: True)
# def callback_query(call):
#     if call.data == 'img':
#         bot.send_message(call.from_user.id, 'send',
#                          reply_markup=mp.select_mode_mrkp)
#     elif call.data == 'audio':
#         bot.answer_callback_query(call.id, "beta")
#     elif call.data == 'video':
#         bot.answer_callback_query(call.id, "beta")


bot.polling(none_stop=True, interval=0, timeout=0)
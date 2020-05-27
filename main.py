from pyes import consts
from pyes import markups as mp
from converts import converts
from converts import voice_converts
from converts import audio_converts
from converts import video_converts
from converts import docs_converts
from converts import video_note_converts
from converts import sticker_converts
from bot_config import bot


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Bot converts your files into needed format\n"
                          "Send yor file please")


@bot.message_handler(commands=['check_list'])
def send_list(message):
    ans = converts.gen_list_of_formats()
    bot.send_message(message.from_user.id, 'You can send one of the following types of files:')
    bot.send_message(message.from_user.id, ans)


@bot.message_handler(commands=['donate'])
def donate_ans(message):
    bot.send_message(message.from_user.id, 'Coming soon :)')


@bot.message_handler(content_types=['voice'])
def echo_voice(message):
    voice_converts.ans_voice(message)


@bot.message_handler(content_types=['audio'])
def echo_audio(message):
    audio_converts.ans_audio(message)


@bot.message_handler(content_types=['video'])
def echo_video(message):
    video_converts.ans_video(message)


@bot.message_handler(content_types=['video_note'])
def echo_video_note(message):
    video_note_converts.ans_video_note(message)


@bot.message_handler(content_types=['sticker'])
def echo_sticker(message):
    sticker_converts.ans_sticker(message)


@bot.message_handler(content_types=['document'])
def echo_doc(message):
    file_type = docs_converts.get_type(message.document.file_name)
    if converts.not_in_list(file_type):
        send_error(message)
    else:
        docs_converts.ans_doc(message)


@bot.message_handler(content_types=['photo'])
def ans_photo(message):
    bot.send_message(message.from_user.id, "Please send this as file, not as photo")


@bot.message_handler(func=lambda message: True)
def send_error(message):
    bot.send_message(message.from_user.id, "We don't support such file type.\n"
                                           "You can easily check the list of available formats "
                                           "by /check_list command")


bot.polling(none_stop=True, interval=0, timeout=0)

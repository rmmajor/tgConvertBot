import telebot as tb


def gen_mrkp(father_format, able_formats, rows=2):
    # print(able_formats)
    markup = tb.types.ReplyKeyboardMarkup(row_width=rows, resize_keyboard=True, one_time_keyboard=True)
    for caption in able_formats:
        if caption == father_format:
            continue
        markup.add(tb.types.KeyboardButton(caption))
    return markup

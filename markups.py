import telebot as tb

select_mode_mrkp = tb.types.InlineKeyboardMarkup()
select_mode_mrkp.row_width = 3
select_mode_mrkp.add(tb.types.InlineKeyboardButton('Audio',  callback_data='audio'),
                     tb.types.InlineKeyboardButton('Video',  callback_data='video'),
                     tb.types.InlineKeyboardButton('Images', callback_data='img'),)


select_audio_mode_mrkp = tb.types.InlineKeyboardMarkup()
select_audio_mode_mrkp.row_width = 2
select_audio_mode_mrkp.add(tb.types.InlineKeyboardButton('mp3 to audio message', callback_data='mp3->ogg'),
                           tb.types.InlineKeyboardButton('audio message to mp3', callback_data='ogg->mp3'),
                           tb.types.InlineKeyboardButton('Back', callback_data='back'))


select_video_mode_mrkp = tb.types.InlineKeyboardMarkup()
select_video_mode_mrkp.row_width = 2
select_audio_mode_mrkp.add(tb.types.InlineKeyboardButton('mp4 to avi', callback_data='mp4->avi'),
                           tb.types.InlineKeyboardButton('avi to mp4', callback_data='avi->mp4'),
                           tb.types.InlineKeyboardButton('Back', callback_data='back'))


select_img_mode_mrkp = tb.types.InlineKeyboardMarkup()
select_img_mode_mrkp.row_width = 2
select_audio_mode_mrkp.add(tb.types.InlineKeyboardButton('jpg to png', callback_data='mp3->ogg'),
                           tb.types.InlineKeyboardButton('png to mp4', callback_data='ogg->mp3'),
                           tb.types.InlineKeyboardButton('Back', callback_data='back'))

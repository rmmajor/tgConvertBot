file_ans = 'We can convert this in one of the following types:'

dir_path = 'tgConvertBot/files/'

all_types = {
    'voice', 'mp3', 'txt', 'docx', 'pdf', 'png', 'jpg', 'svg'
    'video_note', 'mp4', 'wav', 'ogg', 'mov',
}

formats = {
    'audio': ('voice', 'ogg', 'wav'),
    'voice': ('mp3', 'ogg', 'wav'),
    'document': ('txt', 'docx', 'pdf'),
    'photo': ('png', 'jpg', 'svg'),
    'video': ('video_note', 'avi', 'mov', 'mkv'),
    'video_note': ('mp4', 'mov', 'mkv', 'avi'),
    'animated_sticker': ('sticker without its pack', ),
    'sticker': ('png', 'jpg', 'svg', 'sticker without its pack'),
}
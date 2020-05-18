token = "<your token>"

file_ans = 'We can convert this in one of the following types:'

dir_path = 'tgConvertBot/files/'

content_types = ['voice', 'audio', 'document', 'photo', 'video', 'video_note']

all_types = {
    'voice', 'mp3', 'txt', 'docx', 'pdf', 'png', 'jpg', 'svg'
    'video_note', 'mp4',
}

formats = {
    'audio': ('voice', ),
    'voice': ('mp3', ),
    'document': ('txt', 'docx', 'pdf'),
    'photo': ('png', 'jpg', 'svg'),
    'video': ('video_note', ),
    'video_note': ('mp4', 'mov', 'mkv', 'avi')
}

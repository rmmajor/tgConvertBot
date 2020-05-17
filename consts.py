token = "<your token>"

file_ans = 'We can convert this in one of the following types:'

dir_path = 'tgConvertBot/files/'

content_types = ['voice', 'audio', 'document', 'photo', 'video', 'video_note']

formats = {
    'audio': ('voice', ),
    'voice': ('mp3', ),
    'document': ('txt', 'docx', 'pdf'),
    'photo': ('png', 'jpg', 'svg'),
    'video': ('video_note', ),
    'video_note': ('mp4', )
}

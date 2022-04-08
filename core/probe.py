import ffmpeg

class infoData(object):
    def __init__(self, data):
        self.data = data
        self.title = self.data.get('tags', {}).get('title', None)
    def __repr__(self):
        return self.title



class probeVideo(object):
    def __init__(self, path_video):
        self.path = path_video
        self.probe = ffmpeg.probe(self.path)
        self.video = []
        self.audio = []
        self.subtitle = []
        self.parse_details()
    def parse_details(self):
        self.get_video()
        self.get_audio()
        self.get_subtitle()
    def get_video(self):
        for item in self.probe['streams']:
            if item['codec_type'] == 'video':
                video_object = infoData(item)
                self.video.append(video_object)
    def get_audio(self):
        for item in self.probe['streams']:
            if item['codec_type'] == 'audio':
                audio_object = infoData(item)
                self.audio.append(audio_object)
    def get_subtitle(self):
        for item in self.probe['streams']:
            if item['codec_type'] == 'subtitle':
                subtitle_object = infoData(item)
                self.subtitle.append(subtitle_object)
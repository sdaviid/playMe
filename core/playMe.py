import mpv
from core.probe import(
    probeVideo
)




class playMe(object):
    def __init__(self):
        self.player = mpv.MPV()
        self.info = None
    def get_info(self, path):
        self.info = probeVideo(path)
    def watch(self, path):
        self.player.play(path)
        self.get_info(path)
        self.player.pause = False
    def pause(self):
        self.player.pause = True
    def start(self):
        self.player.pause = False
    def toggle_play(self):
        if self.player.pause == False:
            self.player.pause = True
        else:
            self.player.pause = False
    def stop(self):
        self.player.stop()
    def set_audio(self, id):
        print('set audio ... {}'.format(id))
        try:
            id = int(id)
            self.player.aid = id
        except Exception as err:
            print('exp set audio ... {}'.format(err))
    def set_subtitle(self, id):
        print('set set_subtitle ... {}'.format(id))
        try:
            id = int(id)
            self.player.sid = id
        except Exception as err:
            print('exp set subtitle ... {}'.format(err))






# path_video = r'/media/dd/1Tbb/Fleabag.S01.1080p.AMZN.WEB-DL.DDP5.1.H.264-SiGLA/Fleabag.S01E01.1080p.AMZN.WEB-DL.DDP5.1.H.264-SiGLA.mkv'
# path_video = 'http://192.168.1.103/Fleabag.S01.1080p.AMZN.WEB-DL.DDP5.1.H.264-SiGLA/caralho/Fleabag.S01E01.1080p.AMZN.WEB-DL.DDP5.1.H.264-SiGLA.mkv'


# p = playMe()
# p.watch(path_video)

# aid = p.info.audio()


# player = mpv.MPV()
# player.play(path_video)
# player.wait_for_playback()



# import ffmpeg


# input = ffmpeg.input(path_video)


# probe = ffmpeg.probe(path_video)
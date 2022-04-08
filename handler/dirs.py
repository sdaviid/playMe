import tornado.web
from core.detail import detailApacheFolder
import os

class listDir(tornado.web.RequestHandler):
    def initialize(self, http_serving):
        self.http_serving = http_serving
    def get(self):
        self.set_header('Content-Type', 'application/json')
        q = self.get_argument('q', '')
        serve = os.path.join(self.http_serving, q)
        data_folder = detailApacheFolder(serve)
        data = {'status': True, 'data': []}
        for file in data_folder.archives:
            temp_data = {
                'title': file.title,
                'type': file.type,
                'size': file.size
            }
            data['data'].append(temp_data)
        self.write(data)


class listTemplate(tornado.web.RequestHandler):
    def initialize(self, http_serving):
        self.http_serving = http_serving
    def get(self):
        self.render('../view/list.html')


class play(tornado.web.RequestHandler):
    def initialize(self, http_serving, inst_player):
        self.inst_player = inst_player
        self.http_serving = http_serving
    def get(self):
        path = self.get_argument('q', False)
        if path != False:
            path_full = os.path.join(self.http_serving, path)
            self.inst_player.watch(path_full)


class toggle_play(tornado.web.RequestHandler):
    def initialize(self, inst_player):
        self.inst_player = inst_player
    def get(self):
        self.inst_player.toggle_play()



class get_audio(tornado.web.RequestHandler):
    def initialize(self, inst_player):
        self.inst_player = inst_player
    def get(self):
        self.set_header('Content-Type', 'application/json')
        data_audio_info = self.inst_player.info.audio
        data_audio = []
        for audio_index in range(0, len(data_audio_info)):
            audio = data_audio_info[audio_index]
            data_audio_temp = {'id': (audio_index + 1), 'descr': audio.title}
            data_audio.append(data_audio_temp)
        data = {'status': True, 'data': data_audio}
        self.write(data)



class get_subtitle(tornado.web.RequestHandler):
    def initialize(self, inst_player):
        self.inst_player = inst_player
    def get(self):
        self.set_header('Content-Type', 'application/json')
        data_sub_info = self.inst_player.info.subtitle
        data_sub = []
        for sub_index in range(0, len(data_sub_info)):
            sub = data_sub_info[sub_index]
            data_sub_temp = {'id': (sub_index + 1), 'descr': sub.title}
            data_sub.append(data_sub_temp)
        data = {'status': True, 'data': data_sub}
        self.write(data)


class set_audio(tornado.web.RequestHandler):
    def initialize(self, inst_player):
        self.inst_player = inst_player
    def get(self):
        id = self.get_argument('id', 0)
        self.inst_player.set_audio(id)



class set_subtitle(tornado.web.RequestHandler):
    def initialize(self, inst_player):
        self.inst_player = inst_player
    def get(self):
        id = self.get_argument('id', 0)
        self.inst_player.set_subtitle(id)
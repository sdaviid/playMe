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
import os
import tornado.web
from core.playMe import playMe


from handler.dirs import(
    listDir,
    listTemplate,
    play,
    toggle_play
)


player = playMe()



port = int(os.getenv('PORT', 5000))
http_serving = 'http://192.168.1.103/'


def make_app():
    return tornado.web.Application([
        (r"/", listTemplate, dict(http_serving=http_serving)),
        (r"/list-dir", listDir, dict(http_serving=http_serving)),
        (r"/play", play, dict(http_serving=http_serving, inst_player=player)),
        (r"/pause", toggle_play, dict(inst_player=player)),
    ], 
    settings = {
        "template_path": 'view/'
    }
    )



if __name__ == "__main__":
    app = make_app()
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()

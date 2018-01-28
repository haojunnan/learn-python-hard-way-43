import web
import sys 
sys.path.append("D:\\learn\\python11\\text\\project\\gothonweb")
from gothonweb import map
urls = (
    '/game','GameEngine',
    '/','Index',
)
app = web.application(urls,globals())
if web.config.get('_session')is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app,store,initializer={'room': None})
    web.config._session = session
else:
    session = web.config._session
render = web.template.render('templates/',base="layout")
class Index:
    def GET(self):
        session.room = map.START
        web.seeother("/game")
class GameEngine:
    def GET(self):
        if session.room:
            return render.show_room(room=session.room)
        else:
            return render.you_died()
    def POST(self):
        form = web.input(action="")
        if session.room:
            session.room = session.room.go(form.action)
        web.seeother("/game")
if __name__ == "__main__":
    app.run()

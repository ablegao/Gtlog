import tornado.ioloop

import tornado.websocket
import tornado.httpserver
import tornado.netutil
import views
import views.users
import views.blog
import uimodules
from settings import DEBUG,PORT,PROCESSES_NUM

class Application(tornado.web.Application):
    def __init__(self):
      
        settings    = {
            'debug':DEBUG, ##ddebug模式无法开始多进程.
            'ui_modules':uimodules,
            'template_path':'templates',
            'static_path':'static',
            'login_url':'/login',
            'cookie_secret':'61oETzKXQAGaYmGeJJFuYh7EQnp2XdTP1o0003',
        }
        handlers = [
            (r"/" , views.blog.Index),
            (r"/blog_edit", views.blog.EditBlog),
            (r'/login' , views.users.UserLogin), 
            
        ]
        tornado.web.Application.__init__(self, handlers, **settings)



application = Application()
if __name__ == "__main__":
    if DEBUG == True:
        application.listen(PORT)
    else:
        #多线程起动。 
        sockets = tornado.netutil.bind_sockets(PORT)
        tornado.process.fork_processes(PROCESSES_NUM)
        server = tornado.httpserver.HTTPServer(application)
        server.add_sockets(sockets)
    
    tornado.ioloop.IOLoop.instance().start()

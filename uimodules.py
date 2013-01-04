import tornado.web

class LeftMenu(tornado.web.UIModule):
    def render(self):
        return self.render_string("admin/left_menu.html")

class Header(tornado.web.UIModule):
    def render(self):
        return self.render_string("admin/header.html")


class Footer(tornado.web.UIModule):
    def render(self):
        return self.render_string("admin/footer.html")

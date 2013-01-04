from . import AdminUserHeader

class login(AdminUserHeader):
    def get(self):
        if self.current_user != None:
            self.redirect( "%s/main" % (self.uri, ) )
            return 
        self.render("admin/login.html")

    def post(self):
        self.set_secure_cookie("admin_user" , self.get_argument('username' , None))
        self.redirect( "%s/main" % (self.uri, ))


class main(AdminUserHeader):
    def get(self):
        self.render("admin/main.html")

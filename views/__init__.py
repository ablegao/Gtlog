import tornado.web
import settings

class ObjectDict(object):
    form = None
    form_error = None
    '''
    def __getattr__(self, key):
        if key in self:
            return self[key]
        return None
    def __setattr__(self, key ,value):
        self[key] = value
    '''

class RequestHandler(tornado.web.RequestHandler):
    _form_error = {}
    def form_error(self,key,val = None):
        if val == None and key in self._form_error:
            return self._form_error
        elif(val != None):
            self._form_error[key] = val
        return None
    def _execute(self, transforms, *args, **kwargs):
        #当使用post模式时， 用_method f负值调用PUT DELETE这些方法。 
        if self.request.method.lower() == 'post':
            if self.get_argument("_method" , None) : 
                self.request.method = self.get_argument('_method').upper()

        tornado.web.RedirectHandler._execute(self,transforms,*args , ** kwargs)

  

class UserHeader (RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")
    
    def render(self , template_name,**kwargs):
        ##z增加一个模板配置支持
        template_name = "%s/%s" % (settings.USER_WEB_THEME , template_name)
        RequestHandler.render(self,template_name, **kwargs)

class AdminUserHeader (RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("adminuser")

#!/usr/bin/env python
#
# Copyright 2013 Able Gao
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
"""
这部分功能， 用户验证用户登陆或者其他用户专属操作。 
"""

from . import UserHeader,RequestHandler
from model.database import database
import json
import hashlib



class UserLogin(UserHeader):
    def get(self):
        self.render("login.html")

    def post(self):
        username    = self.get_argument('username' , None) 
        passwd      = self.get_argument('passwd' , None)
        
        if username and passwd:
            #转码gb2312后md5 . 中文通用
            md5pass = hashlib.md5(passwd.encode(encoding="gb2312"))
            passwd  = md5pass.hexdigest() 
            db = database()
            if db!=None:
                cursor = db.cursor()
                cursor.execute("SELECT id,username,passwd FROM users WHERE username = %(username)s"  ,{"username":username} )
                row  = cursor.fetchone()
                if row != None and row[1] == passwd:
                    self.set_secure_cookie("user" , username)
                    self.redirect("/")
                elif(row == None):
                    self.form_error("username" , '用户名不能为空!')
                elif(row[1] != passwd ):
                    print( "%s :: %s " % (row[1] , passwd))
                    self.form_error("passwd" , '密码不正确')
            db.close()
        elif username == None:
            self.form_error('username' , '登陆名不能为空')
        elif passwd == None:
            self.form_error('passwd' , '密码不能为空')
        self.write(json.dumps(self._form_error)) 

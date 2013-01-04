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
blog 管理模块
"""
from . import UserHeader,RequestHandler
from model.database import database
import datetime
import time
class Index(UserHeader):
    def get(self):
        db = database()
        cursor = db.cursor()
        cursor.execute("SELECT title,content FROM blog_content where is_del=0 ORDER BY create_time DESC")
        rows = cursor.fetchall()
        cursor.close()
        db.close()
        self.render("index.html"  , rows = rows)


  
class EditBlog(UserHeader):
    def initialize(self):
        if self.current_user == None:
            self.redirect("/")
    def get(self):
        db = database()
        cursor = db.cursor()
        cursor.execute("SELECT id,title,content FROM blog_content WHERE is_del=0 ORDER BY create_time DESC")
        rows = cursor.fetchall()
        cursor.close()
        db.close()
        self.render("edit_index.html"  , rows = rows)

    def post(self):
        title   = self.get_argument('title' , None)
        content = self.get_argument('content' , None)
        if title and content:
            db          = database()
            cursor      = db.cursor()
            insert_sql  =    ("INSERT INTO blog_content "
                            "(id,user_id , cate_id , title , content ,create_time,tags)"
                            "VALUES "
                            "(NULL,%(user_id)s , %(cate_id)s ,%(title)s , %(content)s , %(times)s , %(tags)s)")
            data        = {
                    'user_id':1,
                    'cate_id':1,
                    'title':title,
                    'content':content,
                    'times':datetime.datetime.now(),
                    'tags':'',
                    }
            cursor.execute(insert_sql,data)
            cursor.close()
            db.close()
            self.redirect("/blog_edit?t=%s" % (time.time(),) ,permanent=True)

    def delete(self):
        id      = self.get_argument("id" , None)
        sql     = "UPDATE  blog_content SET is_del=1 WHERE id=%(id)s"
        db      = database()
        cursor  = db.cursor()
        cursor.execute(sql,{'id':id})
        cursor.close()
        db.close()
        self.write(1)

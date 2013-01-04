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
使用这套程序， 需要安装mysql 官方操作驱动 , 我安装的版本号， 1.0.7 其他版本并没有测试过。 
    http://dev.mysql.com/downloads/connector/python/
"""

import mysql.connector
import settings 
from model import out

'''
数据连接
'''
class database (mysql.connector.MySQLConnection):
    def __init__(self):
        try:
            conf = settings.DB_CONFIG
            mysql.connector.MySQLConnection.__init__(self,**conf)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                out.error("Something is wrong your username or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                out.error("Database does not exists")
            else:
                out.error(err)
            cnx.close()
            return None




'''
为了实现数据模型， 建立的一个数据库查询基本类。 
'''
class BaseDB(database):
    
    def __init__(self):
        database.__init__(self)

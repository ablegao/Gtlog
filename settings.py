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
配置文件。
"""

"""
开始模式(DEBUG = True)， 生产模式切换。 
"""
DEBUG           = True
"""
进程启动时， 占用的端口
"""
PORT            = 8080
"""
当DEBUG = False 时， 站点将会用多进程模式启动， 用来增加执行效率。
下面的参数用户告知站点启动的应用数量。  
"""
PROCESSES_NUM   = 3

"""
模板设置
对应template/default 
    static/default
"""
USER_WEB_THEME  = 'github'


ADMIN_URI   = 'admin'

DB_CONFIG   = {
  'user': 'root',
  'password': '',
  'host': '127.0.0.1',
  'database': 'play28_db',
  'raise_on_warnings': True,
}

#用来记录错误日志. 
ERROR_LOG = False
ERROR_LOG_PATH = "/tmp/error.log"

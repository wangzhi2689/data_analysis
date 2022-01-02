# -*- coding: utf-8 -*-
# file: main.py
# author: wang zhi
# time: 01/27/2021 9:53 AM
# Copyright 2021 wang zhi. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------
import numpy as np
import time
import datetime
# 需要用python的脚本来快速检测一个文件内的二个时间日期字符串的大小，其实实现很简单,首先一些基础的日期格式化知识如下

import time
import datetime

'''
%a星期的简写。如 星期三为Web
%A星期的全写。如 星期三为Wednesday
%b月份的简写。如4月份为Apr
%B月份的全写。如4月份为April
%c: 日期时间的字符串表示。（如： 04/07/10 10:43:39）
%d: 日在这个月中的天数（是这个月的第几天）
%f: 微秒（范围[0,999999]）
%H: 小时（24小时制，[0, 23]）
%I: 小时（12小时制，[0, 11]）
%j: 日在年中的天数 [001,366]（是当年的第几天）
%m: 月份（[01,12]）
%M: 分钟（[00,59]）
%p: AM或者PM
%S: 秒（范围为[00,61]，为什么不是[00, 59]，参考python手册~_~）
%U: 周在当年的周数当年的第几周），星期天作为周的第一天
%w: 今天在这周的天数，范围为[0, 6]，6表示星期天
%W: 周在当年的周数（是当年的第几周），星期一作为周的第一天
%x: 日期字符串（如：04/07/10）
%X: 时间字符串（如：10:43:39）
%y: 2个数字表示的年份
%Y: 4个数字表示的年份
%z: 与utc时间的间隔 （如果是本地时间，返回空字符串）
%Z: 时区名称（如果是本地时间，返回空字符串）
%%: %% => %
'''

def getLocalTime():
    n_time = datetime.datetime.now()  # 获取当前时间
    print("获取当前时间 : ", n_time)  # 2021-01-27 00:55:51.129879
    print(type(n_time))  # <class 'datetime.datetime'>

    n_time = datetime.datetime.now().strftime('%Y-%m-%d')  # 获取当前时间格式转换
    print("获取当前时间格式转换 : ", n_time)  # 2021-01-27
    print(type(n_time))  # <class 'str'>

    n_ts = time.time()
    print(n_ts)
    return n_time

# 比较两个真实日期之间的大小，date1 > date2 则返回True
def date_compare(date1, date2, fmt='%Y-%m-%d'):

    zero = datetime.datetime.fromtimestamp(86400)
    try:
        d1 = datetime.datetime.strptime(str(date1), fmt)
    except:
        d1 = zero
    try:
        d2 = datetime.datetime.strptime(str(date2), fmt)
    except:
        d2 = zero
    return d1 > d2

if __name__ == '__main__':
    #begin_char = input('## please input the first character:')
    #print(begin_char)
    jsontime = '2017-04-03'
    # string->time
    print(time.strptime(jsontime, "%Y-%m-%d"))
    # string->datetime
    print(datetime.datetime.strptime(jsontime, "%Y-%m-%d"))
    # time->string
    print(time.strftime("%Y-%m-%d", time.localtime()))

    getLocalTime()
    a=date_compare("2017-04-03","2020-03-03")
    print("date_compare : " + str(a))


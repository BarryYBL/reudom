#!/usr/bin/python
#
# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from .case import TestCase
from .running.test_runner import main

# 跳过用例
from .skip import skip
from .skip import skip_if
from .skip import skip_unless

# request方法引入
from requests import post
from requests import get
from requests import put
from requests import head
from requests import patch
from requests import options

# 时间戳
from .testdata.timestamp import TimeStamp

# ddt数据驱动
from .testdata.parameterizeds import ddt, ddt_class

# User-Agent 浏览器用户代理
from .testdata.User_Agent import chromePC, safariPC, iePC, firefoxPc
from .testdata.User_Agent import chromePhone, safariPhone, iePhone, firefoxPhone

__author__ = "Barry"

__version__ = "1.2.3.0"

__description__ = "Automated testing framework based on requests and unittest interface."

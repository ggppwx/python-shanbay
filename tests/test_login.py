#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shanbay import AuthException, ConnectException, Shanbay
import unittest
from shanbay.dict_api import DictAPI

class TestLogin(unittest.TestCase):
    def test_login(self):
        try:
            s = Shanbay('ggppwx', '3006216088')
            s.login()
        except:
            self.fail("login failure")
            
            
    def test_user(self):
        try:
            s = Shanbay('ggppwx', '3006216088')
            s.login()
            api = DictAPI(s)
            user = api.user().json()
            print(user)
        except:
            pass
            
    '''
    def test_exception(self):
        try:
            Shanbay('rxxxoot', 'axxbcd').login()
        except AuthException:
            pass
    
        try:
            proxies = {
                "http": "http://10.10.1.10:3128",
                "https": "http://10.10.1.10:1080",
            }
            Shanbay('rooxxt', 'abcxx').login(proxies=proxies, timeout=3)
        except ConnectException:
            pass
    '''
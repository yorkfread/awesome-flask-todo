# -*- coding: utf-8 -*-

"""
    单元测试
"""

import unittest
from app import app


class TestTodo(unittest.TestCase):
    def setUp(self):
        """
        测试函数运行之前调用
        :return: 
        """
        self.app = app.test_client()

    def tearDown(self):
        """
        测试函数运行结束后调用
        :return: 
        """
        pass

    def test_index(self):
        rv = self.app.get('/')
        assert '备忘小条子' in bytes.decode(rv.data)


if __name__ == '__main__':
    unittest.main()

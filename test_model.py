import unittest
from model import TodoItem

class TodoItem(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownclass')

    def setUp(self):
        print('setUp')
        self.todo_1 = TodoItem('Remember to finish the Pexon homework')

    def tearDown(self):
        print('tearDown\n')

    def test_item(self):
        print('test_item')
        self.assertEqual(self.todo_1, max_length=180)
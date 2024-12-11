import unittest

from main import is_sublist, list1, list2

class Test01(unittest.TestCase):
    def test_is_sublist(self):
        '''
        Here we test the is_sublist function
        '''
        data1 = ['1', 'a', '2', 'b', '3', 'c', '4', 'd']
        data2 = ['a', '2', 'b', '3']
        result = is_sublist(data1, data2)
        self.assertEqual(True, result)

class Test02(unittest.TestCase):
    def test_is_sublist(self):
        '''
        Here we test the is_sublist function
        '''
        data1 = ['1', 'a', '2', 'b', '3', 'c', '4', 'd']
        data2 = ['a', 'b', 'c', 'd']
        result = is_sublist(data1, data2)
        self.assertEqual(False, result)


class Test03(unittest.TestCase):
    def test_list1(self):
        '''
        Here we test the list1 function
        '''
        data = ['a', 'b', 'c', 'd', 'e', 'f']
        result = list1(data)
        self.assertEqual('abcdef', result)

class Test04(unittest.TestCase):
    def test_list1(self):
        '''
        Here we test the list1 function
        '''
        data = ['mele', 'pere', 'arance', 'limoni', 'fragole', 'fichi']
        result = list1(data)
        self.assertEqual('meleperearancelimonifragolefichi', result)


class Test05(unittest.TestCase):
    def test_list2(self):
        '''
        Here we test the list2 function
        '''
        data = ['a', 'b', 'c', 'd', 'e', 'f']
        result = list1(data)
        self.assertEqual('abcdef', result)

class test06(unittest.TestCase):
    def test_list2(self):
        '''
        Here we test the list2 function
        '''
        data = ['mele', 'pere', 'arance', 'limoni', 'fragole', 'fichi']
        result = list1(data)
        self.assertEqual('meleperearancelimonifragolefichi', result)

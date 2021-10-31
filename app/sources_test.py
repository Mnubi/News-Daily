import unittest
from models import sources
Source=sources.Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source("abc-news",'Python Must Be Crazy','A thrilling new Python Series','https://abcnews.go.com','general')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))


if __name__ == '__main__':
    unittest.main()
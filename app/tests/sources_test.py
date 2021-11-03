import unittest
class Source:
    '''
    Source class to define source objects
    '''
    def __init__(self,id,name,description,url,category,):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category= category

class NewsSourceTest(unittest.TestCase):
    def setUp(self):
        self.new_source = Source(
            'abc-news', 'ABC News', 'Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.', "https://abcnews.go.com", 'general')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))

if __name__ == '__main__':
    unittest.main()
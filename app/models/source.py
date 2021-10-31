class Source:
    '''
    Source class to define source objects
    '''
    def __init__(self,id,name,description,url,category):
        self.id = id
        self.name = name
        self.description = description
        self.url = "https://abcnews.go.com" + url
        self.category= category
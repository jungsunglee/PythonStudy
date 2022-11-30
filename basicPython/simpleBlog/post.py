
class Post:
    '''
    posts class
    param id : post number
    param title : post title
    param content : post content
    param hits : post hits
    '''
    def __init__(self, id: int, title: str, content: str, hits:int) -> None:
        self.id = id
        self.title = title
        self.content = content
        self.hits = hits
    
    def set_post(self, id: int, title: str, content: str, hits:int):
        self.id = id
        self.title = title
        self.content = content
        self.hits = hits  

    def incresceHits(self):
        self.hits += 1
    
    def getId(self):
        return self.id
    
    def getTitle(self):
        return self.title
    
    def getContent(self):
        return self.content
    
    def getHits(self):
        return self.hits
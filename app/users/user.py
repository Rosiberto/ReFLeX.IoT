
class User():
    __tablename__ = 'users'
    
    def __init__(self, id, name, username, password):
        self._id       = id
        self._name     = name
        self._username = username
        self._password = password
        
        
    def getId(self):
        return self._id
        
    def getName(self):
        return self._name
    
    def setName(self, name):
        self._name = name
        
    def getUserName(self):
        return self._username
        
    def setUserName(self, username):
        self._username = username

    def getPassword(self):
        return self._password
        
    def setPassword(self, password):
        self._password = password

import uuid


class User:
    users = []
    def __init__(self, information:list):
        self.Name,self.Lastname,self.Age,self.passsword, *_ = information
        self.Id = uuid.uuid4()
        self.accountValue = ""
        self.gamblesHistory = {}
    
    
    def __str__(self) -> str:
        return f"{self.Name} {self.Lastname}"
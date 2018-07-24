class BaseClass(object):
    def __init__(self):
        self.x = 10

class InsideClass(BaseClass):
    def __init__(self):
        super(InsideClass,self).__init__()
        self.x = 20
number = InsideClass()
print(number.x)
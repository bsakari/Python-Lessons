class BaseClass(object):
    def jina(self):
        print("King")


class InsideClass(BaseClass):
    def jina(self):
        print("Wanyama")

name = InsideClass()
name.jina()

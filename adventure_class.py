class Hero(object):
    def __init__(self,name):
        self.name = name
        self.health = 10
        self.items = {"weapon":'sword',"item1":"none","item2":"~none~"}
        self.pos = 1

    def list_items(self):
        print
        print("~~~backpack~~~")
        for i in (self.items):
            print("    "+ self.items[i])
        print("~~~~~~~~~~~~~~")
        print
        
    def say_name(self):
        print(self.name)


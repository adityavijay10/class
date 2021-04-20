class Bird(object):
    def __init__(self,name,colour,speed):
        self.name:name
        self.colour: colour
        self.speed:speed

    def details(self):
        print('hi')

peacock=Bird('peacock', 25,"blue")
peacock.details()

print(peacock.name)
class Animal:
    def eat(self):
        print('I can eat')
    
    def sleep(self):
        print('I can sleep')

class Tiger(Animal):
    def hunt(self):
        print('I can hunt')

Tiger1 = Tiger()

Tiger1.eat()
Tiger1.sleep()

Tiger1.hunt()
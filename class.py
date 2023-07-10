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

#new
a = int(input("enter a num"))
if a%2 == 0:
    print("even")
else:
    print("odd")

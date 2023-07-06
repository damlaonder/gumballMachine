
import random

class Gumball_Machine:


    #contructor: 1 arg - how many gumballs the machine is filled with 
    def __init__(self, capacity):
        
        #variable /attribute that hold the argument 
        self.capacity = capacity

        #each machine starts off empty
        self.money = 0

        # empty list to store our gumballs
        self.gumballs = []
        #randomly select gumballs 
        for x in range(self.capacity):
            color = random.randint(1,3)
            if color == 1:
                self.gumballs.append("red")
            if color == 2:
                self.gumballs.append("blue")
            if color == 3:
                self.gumballs.append("green")
        


        

        #announce output
        print("Gumball Machine created with", capacity, "random gumballs")
        print()


    def report(self):
        print("Gumball Machine Report:")
        print("* Gumballs in machine: ", self.capacity)
        print("* Money in machine: $"+str(self.money))
        print()

    def dispense(self, coin):
        if self.capacity == 0:
            print("Machine is empty, no gumball will be dispensed")
            print()
            
        elif coin != 0.25:
            print("Invalid coin, no gumball will be dispensed")
            print()
            
        else:
            self.capacity -= 1
            #add money
            self.money += coin
            print("Accepting 0.25; Dispensing a", self.gumballs[0], "gumball")
            #remove gumball
            self.gumballs.pop(0)
            print()

            


    def count_gumballs_by_type(self, Gtype):
        print("There are", self.gumballs.count(Gtype), "gumballs of type", Gtype,  "in the machine")
        print()




# TESTER CODE
  
machine = Gumball_Machine(5)
machine.report()
  
machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")
  
machine.dispense(0.10)
machine.dispense(0.50)
machine.dispense(0.01)
  
machine.report()
  
machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")
  
machine.dispense(0.25)
machine.dispense(0.25)
machine.dispense(0.25)
  
machine.report()
  
machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")
  
machine.dispense(0.25)
machine.dispense(0.25)
machine.dispense(0.25)
  
machine.report()
  
machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")

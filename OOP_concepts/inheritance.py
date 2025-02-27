# Write a program where a child class inherits from two parent class
# What will be the output of the program

# Class Parent1():
#     def __init__(self, name, age, profession):
#         self.name = name 
#         self.age = age
#         self.profession = profession
    
#     def introduction(self):
#         print(f"I am {self.name} and {self.age} year old and my profession is {self.profession}")
        
#     def city(self, address):
#         print(','.join(address))
        
# Class Parent2():
    
    
    
class A:
   def __init__(self):
        self.name = "sravani"
   def display(self):
        print(self.name)
class B(A):
    def __init__(self):
        super().__init__()
        self.name = "sreesravani"
    def display(self):
        print(self.name)
class C(B):
    def __init__(self):
        super().__init__()
        
c_object = C()
c_object.display()
class Robot:
    def __init__(self, name):
        self.name = name
    
        
class CleaningRobot():
    def performtask(self):
        print("cleaning")
    
class SecurityRobot():
    def performtask(self):
        print("checking")
    
cleaner = CleaningRobot()
security = SecurityRobot()
cleaner.performtask()
security.performtask()
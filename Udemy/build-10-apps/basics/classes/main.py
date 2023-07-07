class human:
    """ This class will be a template for a simple human
    """
    def __init__(self, name):
        self.name = name
    
    def birth(self):
        return f"{self.name} is born. Yeey!"
        
    def eat(self):
        return f"{self.name} eats food. Nom nom"
    
    def grow(self):
        return f"{self.name} grows."
    
    def learn(self):
        return f"{self.name} learns stuff."

    def work(self):
        return f"{self.name} works."
        
    def sleep(self):
        return f"{self.name} sleeps. Zzz"
    
    def getold(self):
        return f"{self.name} gets old. (bones creaking)"
    
    def die(self):
        return f"{self.name} dies. (people sad) "
        
        
names = ["Billy Bob", "Valery Vix", "Jane Jensen", "John Johnson", "Mike Malarkey"]        
humans = []

for name in names:
    humans.append(human(name))

for person in humans:
    print(person.birth(), person.eat(), person.grow(), person.learn())
    
  
class triathlon:
    def __init__(self, first, last, location, swim, cycle, run, total):
        self.first = first   
        self.last = last       
        self.location = location  
        self.swim = swim        
        self.cycle = cycle      
        self.run = run          
        self.total = total
    def info(self):
        print(f"{self.first} {self.last} ({self.location}): Swim {self.swim} Cycle {self.cycle} Run {self.run} Total {self.total}")
peter = triathlon("Peter", "City A", "City B", 25, 30,20,75)
print(peter.info())

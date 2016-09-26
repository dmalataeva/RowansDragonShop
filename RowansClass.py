class Pet:
    
    def __init__(self,name,species,breed,gender,age,origin,diet,hostility,price,sold):
        self.name=name
        self.species=species
        self.breed=breed
        self.gender=gender
        self.age=age
        self.origin=origin
        self.diet=diet
        self.hostility=hostility
        self.price=price
        self.sold=sold
        
    def getName(self):
        return self.name
    
    def getSpecies(self):
        return self.species
    
    def getBreed(self):
        return self.breed
    
    def getGender(self):
        return self.gender
    
    def getAge(self):
        return self.age
    
    def getOrigin(self):
        return self.origin
        
    def getDiet(self):
        return self.diet
        
    def getHostility(self):
        return self.hostility
    
    def getPrice(self):
        return self.price
    
    def getSold(self):
        return self.sold
    
    def __str__(self): # used for testing purposes in the code
        if self.gender=="male":
            print("%s is a %s year-old %s. He comes from %s where he mostly feeds on %s." % (self.name,self.age,self.breed,self.origin,self.diet))
        elif self.gender=="female":
            print("%s is a %s year-old %s. She comes from %s where she mostly feeds on %s." % (self.name,self.age,self.breed,self.origin,self.diet))
        if int(self.hostility)>=6:
            print("The hostility rate for %s is %s, which means caution should be exercised." % (self.name,self.hostility))
        elif int(self.hostility)<=5:
            print("The hostility rate for %s is %s, which means this dragon is more or less friendly." % (self.name,self.hostility))
        print("Price: %s Woolongs" % (self.price))
        return
    
    def AboutMe(self): # outputs information about current pet
        print("Name: %s" % (self.name))
        print("Species: %s" % (self.species))
        print("Breed: %s" % (self.breed))
        print("Age: %s" % (self.age))
        print("Origin: %s" % (self.origin))
        print("Gender: %s" % (self.gender))
        print("Hostility rate (from 1 to 10): %s" % (self.hostility))
        print("Price: %s" % (self.price))
        return

    def Diet(self): # outputs diet information
        if int(self.hostility)>=8:
            altdiet="a carnivore diet"
        elif int(self.hostility)<8 and int(self.hostility)>3:
            altdiet="an omnivore diet"
        elif int(self.hostility)<=3:
            altdiet="a herbivore diet"
        return "%s mostly feeds on %s but due to his/her hostility rate (%s) can maintain %s." % (self.name,self.diet,self.hostility,altdiet)
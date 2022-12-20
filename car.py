#Run using below commands
''' g=Garage()
car1=['VW','Passat',2021]
g.add(car1)
car2=['Buick','Nevera',2011]
g.add(car2)
car3=['Riamac','Enclave',2015]
g.add(car3)
g.getRandomCar()
car4=['VW','Passat',2020]
g.add(car4)
g.getCarsBasedOnMake('VW')
g.__str__()
c=Car('Ford','Pinto',2015)
c1=c.getcar()
c1 in g
c1=Car('Buick','Nevera',2011)
cc=c1.getcar()
cc in g
print(g.__len__())
g.__iter__()
'''
import random
cardet=[]
class Car (object):
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.carr=[self.make,self.model,self.year]
        
    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getYear(self):
        return self.year
    def getcar(self):
        return self.carr

    def __str__(self):
        return 'I am a {} {} made in {}.'.format(self.make,self.model,self.year)

    def __repr__(self):
        return "Car('{}','{}','{}')".format(self.make,self.model,self.year)
    
        
class Garage(object):
    'an object that contains cars'

    def __init__(self):
        pass

    def __contains__(self,car):
        'Returns True if the garage contains and car that matches the make, model and year.'
        if car in self.cardet:
            print(True)
        else:
            print(False)
            

    def getCarsBasedOnMake(self,make):
        mack_C=[]
        for i in range(0,len(self.cardet)):
            if make in cardet[i]:
                 mack_C.append(self.cardet[i])
        print( mack_C)
                 

    def getRandomCar(self):
        n = random. randint(0,len(self.cardet))
        print(self.cardet[n])

    def add(self,car):
        #'add a car to the garage'
        cardet.append(car)
        self.cardet=cardet

    def __len__(self):
        return len(self.cardet)

    def __str__(self):
        print('There are {} cars in the Garage'.format(len(self.cardet)))
    def __iter__(self):
        
        for c in self.cardet:
            xx=Car(c[0],c[1],c[2])
            print(xx)
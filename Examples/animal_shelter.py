class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []
    
    def enqueue(self, animal, type):
        if type == 'Cat':
            self.cats.append(animal)
        else:
            self.dogs.append(animal)
    
    def dequeueCat(self):
        if len(self.cats) == 0:
            return None
        else:
            cat = self.cats.pop()
            return cat
    
    def dequeueDog(self):
        if len(self.dogs) == 0:
            return None
        else:
            dog = self.dogs.pop()
            return dog
    
    def dequeueAny(self):
        if len(self.cats) == 0:
            result = self.dogs.pop(0)
        else:
            result = self.cats.pop(0)
        return result

customShelter = AnimalShelter()
customShelter.enqueue('Dog1', 'Dog')
customShelter.enqueue('Dog2', 'Dog')
customShelter.enqueue('Cat1', 'Cat')
customShelter.enqueue('Dog3', 'Dog')
customShelter.enqueue('Cat2', 'Cat')
customShelter.enqueue('Cat3', 'Cat')


print(customShelter.dequeueAny())
print(customShelter.dequeueCat())
print(customShelter.dequeueDog())

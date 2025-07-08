class vehicle:
    def __init__(self,model,make):
        self.model = model
        self.make = make
    def moves(self):
        print("move along..")
    def get_make_model(self):
        print(f" {self.model}\n {self.make}")

my_car = vehicle('tesla','roadster')
print(my_car.make)
my_car.moves()

my_car.get_make_model()

# inheritance

class airplane(vehicle):
    def __init__(self,model,make,faa_id):
        self.faa_id = faa_id
        super().__init__(make,model)
        
    def moves(self):
        print(f"fliess along with {self.faa_id}")

boing = airplane('boeing','747','13423525')

boing.moves()

class golfCaddy(vehicle):
    pass # passes down the properties and methods of parent class

beeng = airplane('boeing','747','122e424')
beeng.moves()

# polymorphism: where multiple instances have the same input and methods put response is different
for v in (my_car,boing,beeng):
    v.get_make_model()
    v.moves()

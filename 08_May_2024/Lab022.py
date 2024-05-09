class Car:
    name = None
    make = None
    model = None

    def __init__(self, o_name, o_make, o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self):
        print("Starting a car with name:", self.name)
        print("Starting a car with make:", self.make)
        print("Starting a car with model:", self.model)


ferarri = Car("Ferrari", "V4", "2023")
ferarri.start_engine()
print("_________________________________________________________________")
Lambo = Car("Lambo", "V8", "2022")
Lambo.start_engine()
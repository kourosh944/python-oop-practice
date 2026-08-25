class Device:
    def __init__(self, brand):
        self.brand = brand

class Laptop(Device):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

lap = Laptop("Lenovo", "ThinkPad")
print(lap.brand, lap.model)
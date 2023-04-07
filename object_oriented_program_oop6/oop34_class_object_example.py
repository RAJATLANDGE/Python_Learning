

class Car:
    def __init__(self, cid, name, brand, model, fuel_type, price, seats=5):   #function under class is called method
        self.cid = cid
        self.name = name
        self.make = brand
        self.launch_year = model
        self.fuel = fuel_type
        self.price = price
        self.seats = seats

    def service(self):
        pass

    def purchase(self):
        pass

Dzire = Car(1, "dzire", "suzuki", 2018, "petrol", 800000 )
Fortuner = Car(2, "fortuner", "toyota", 2021, "diesel", 1500000, "Seats=7")
print(Dzire.make)
print(Dzire.launch_year)



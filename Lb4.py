class Vehicle:
    def __init__(self, make: str, model: str, year: int):
        self.__make = make
        self.__model = model
        self.__year = year

    def __str__(self) -> str:
        return f"Vehicle(make={self.__make}, model={self.__model}, year={self.__year})"

    def __repr__(self) -> str:
        return f"Vehicle({self.__make!r}, {self.__model!r}, {self.__year})"

    def start_engine(self) -> str:
        return f"The engine of {self.__make} {self.__model} has started."


class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int, doors: int):
        super().__init__(make, model, year)
        self._Vehicle__year = None
        self._Vehicle__model = None
        self._Vehicle__make = None
        self.__doors = doors

    def __str__(self) -> str:
        return f"Car(make={self._Vehicle__make},\
         model={self._Vehicle__model}, year={self._Vehicle__year}, doors={self.__doors})"

    def __repr__(self) -> str:
        return f"Car({self._Vehicle__make!r}, {self._Vehicle__model!r}, {self._Vehicle__year}, {self.__doors})"

    def start_engine(self) -> str:
        base_message = super().start_engine()
        return f"{base_message} This is a car with {self.__doors} doors."


if __name__ == "__main__":
    vehicle = Vehicle("Toyota", "Camry", 2020)
    print(vehicle)
    print(repr(vehicle))

    car = Car("Honda", "Civic", 2021, 4)
    print(car)
    print(repr(car))
    print(car.start_engine())
    pass

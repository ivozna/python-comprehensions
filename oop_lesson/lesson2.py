from typing import List, Tuple

class Vehicle:
    def __init__(self, name: str, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

def get_list() -> List[Tuple[int, float, bool]]:
    return 1

print(get_list())

School_bus = Bus("School Volvo", 12, 50)

print(isinstance(School_bus, Vehicle))
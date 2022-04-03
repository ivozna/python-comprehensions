from datetime import date


class Employee:
    MONTH_IN_YEAR = 12

    name: str
    _position: str
    salary: int
    year_of_hire: int
    country: str

    def __init__(self, name, position, salary, year, country) -> None:
        self.name = name
        self._position = position
        self.salary = salary
        self.year_of_hire = year
        self.country = country

    ###### ENCAPSULATION
    def get_position(self) -> str:
        return self._position
    def set_position(self, new_pos) -> str:
        self._position = new_pos
    ############

    def __repr__(self) -> str:
        return f"Employee ({self.name}, {self.position}, {self.salary}, {self.year_of_hire}, {self.country})"

    def __add__(self, bonus) -> str:
        self.salary = self.salary + bonus
        return self
        
    def total_income(self) -> float:
        total_income = (Employee.get_current_year() - self.year_of_hire) * self.MONTH_IN_YEAR * self.salary
        print(total_income)
        return total_income

    @classmethod
    def change_month_count(cls, count):
        cls.MONTH_IN_YEAR = count

    @staticmethod
    def get_current_year() -> int:
        return date.today().year

def main():
    emp1 = Employee("Ira", "AQA", 800, 2014, "Ukraine")
    emp2 = Employee("Vasyl", "SW", 12000, 2004, "Ukraine")

    emp1.total_income()
    
    emp1 += 12
    print(emp1.salary)

if __name__ == "__main__":
    main()


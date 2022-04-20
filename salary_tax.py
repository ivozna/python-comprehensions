from ast import Return


def progressive_tax(income):
   #>=120 - 20%
   # <120 - 5%
    if income >= 120000:
        return income*0.2
    else:
        return income*0.05
    
def danish_tax(income):
    if income < 40_000:
        return 0
    elif income < 100_000:
        return income * 0.1
    else:
        return income * 0.15


class MonthlySalaryContract:

    def __init__(self, compensation) -> None:
        self.compensation = compensation
    
    def annual_income(self):
        return self.compensation * 12


class HourlyContract:
    def __init__(self, compensation) -> None:
        self.compensation = compensation

    def annual_income(self):
        return self.compensation * 8 * 21 * 12
        

class Coder:
    def __init__(self, contract, get_tax_rate) -> None:
        self.contract = contract
        self.get_tax_rate = get_tax_rate

    def total_income(self):
        return self.contract.annual_income()
       
    def get_tax(self):
        return self.get_tax_rate(self.total_income())


def main():
    coder_1_contract = MonthlySalaryContract(compensation=5000)
    coder_1 = Coder(
        contract=coder_1_contract,
        get_tax_rate=progressive_tax
    )
    ## expected: ~ 5000 * 12
    print(coder_1.total_income())
    print(coder_1.get_tax())


    coder_2_contract = HourlyContract(compensation=250)
    coder_2 = Coder(
        contract=coder_2_contract,
        get_tax_rate=danish_tax
    )
    # expected: 250 * 8 * 21 * 12
    print(coder_2.total_income())
    print(coder_2.get_tax())


if __name__ == '__main__':
    main()


class BankCustomer:
    def __init__(self, accNo, name, ic, job, accountType):
        self.accNo = accNo
        self.name = name
        self.ic = ic
        self.job = job
        self.accountType = accountType

bankCust1 = BankCustomer(451254, "Raj", "123456-12-1234", "Teacher", "Saving")
print(bankCust1. __dict__)

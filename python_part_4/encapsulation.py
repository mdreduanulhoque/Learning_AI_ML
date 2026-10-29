class Bank:
    def __init__(self, branch_name, balance, total_employee):
        self.branch_name = branch_name      #public
        self.__balance = balance        #private
        self._total_employee = total_employee       #protected

    def get_banalce(self):
        return self.__balance

    def set_balance(self, new_balance):
        self.__balance = new_balance

    def display(self):
        print(f"Branch Name: {self.branch_name}     Total Employee: {self._total_employee}      Balance: {self.__balance}")


b1 = Bank(branch_name="Dhaka", balance=28000, total_employee=78)
b1.display()

b1.set_balance(98000)
b1.display()


        
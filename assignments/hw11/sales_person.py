"""
Mark Fiegel
hw11.py
I certify that this assignment is entirely my own work.
"""
class SalesPerson:
    def __init__(self,employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []
    def get_id(self):
        id = self.employee_id
        return id
    def get_name(self):
        name = self.name
        return name
    def set_name(self,name):
        set_name = name
        return set_name
    def enter_sale(self,sale):
        self.sales.append(sale)
    def total_sales(self):
        sales = 0
        for i in range(len(self.sales)):
            sales = sales + self.sales[i]
        return sales
    def get_sales(self):
        return self.sales
    def met_quota(self,quota):
        if self.total_sales() >= quota:
            return True
        else:
            return False
    def compare_to(self,other):
        if self.total_sales() > other:
            return 1
        elif self.total_sales() == other:
            return 0
        elif self.total_sales() < other:
            return -1
    def __str__(self):
        return "{employee_id} - {name}:{total_sales}".format(employee_id=self.get_id(),name=self.get_name(),total_sales=self.total_sales())
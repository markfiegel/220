"""
Mark Fiegel
hw11.py
I certify that this assignment is entirely my own work.
"""
class SalesForce:
    def __init__(self):
        self.sales_people = []
    def add_data(self,file_name):
        files = open(file_name,'r')
        sales_people = files.read()
        self.sales_people = sales_people.split('\n')
        files.close()
        return self.sales_people
    def quota_report(self,quota):
        listo = []
        for i_val in range(len(self.sales_people)-1):
            new_list = self.sales_people[i_val].split(',')
            floats = new_list[2]
            new_list.pop(2)
            emp_nums = new_list[0]
            emp_nums = int(emp_nums)
            new_list.pop(0)
            new_list.insert(0,emp_nums)
            sum = 0
            floats = str(floats)
            floats = floats.split(' ')
            floats.pop(0)
            for j_val in range(len(floats)):
                y_val = (floats[j_val])
                y_val = float(y_val)
                sum = sum + y_val
                if j_val == len(floats)-1:
                    new_list.append(sum)
                    if sum > quota:
                        new_list.append(True)
                    else:
                        new_list.append(False)
                    listo.append(new_list)
        return listo
    def top_seller(self):
        listo = []
        for i_val in range(len(self.sales_people) - 1):
            sum = 0
            new_list = self.sales_people[i_val].split(',')
            floats = new_list[2]
            new_list.pop(2)
            emp_nums = new_list[0]
            emp_nums = int(emp_nums)
            new_list.pop(0)
            new_list.insert(0, emp_nums)
            floats = str(floats)
            floats = floats.split(' ')
            floats.pop(0)
            for j_val in range(len(floats)):
                y_val = (floats[j_val])
                y_val = float(y_val)
                sum = sum + y_val
            listo.append(sum)
        top_sum = 0
        for i in range(len(listo)):
            new_sum = listo[i]
            if top_sum < new_sum:
                top_sum = new_sum
        final_product = []
        if listo.count((top_sum)) == 1:
            adder = listo.index(top_sum)
            final_product.append(self.sales_people[adder])
        if listo.count(top_sum) > 1:
            for p in range(listo.count(top_sum)):
                replacer = listo.index(top_sum)
                final_product.append(self.sales_people[replacer])
                listo.pop(replacer)
                listo.insert(replacer,' ')
        return final_product
    def individual_sales(self,employee_id):
        id_list = []
        names = []
        for i in range(len(self.sales_people)-1):
            j = self.sales_people[i]
            j = j.split(',')
            id_appender = int(j[0])
            name_appender = j[1]
            id_list.append(id_appender)
            names.append(name_appender)
        if id_list.count(employee_id) == 1:
            selector = id_list.index(employee_id)
            return names[selector]
        else:
            return None
    def get_sale_frequencies(self):
        # I couldnt figure this out
        sales = {}
        sales = []
        for i in range(len(self.sales_people)-1):
            f = self.sales_people[i]
            f = f.split(',')
            x = f[2]
            print(x)
        print(sales)
m = SalesForce()
m.add_data('sales_data.txt')
m.get_sale_frequencies()
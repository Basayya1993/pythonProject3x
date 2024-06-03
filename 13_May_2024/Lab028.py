class calculator():
    num1 = None
    num2 = None
    def __init__(self,i_num1,i_num2):
        self.num1 = i_num1
        self.num2 = i_num2

    def addition(self):
        print("Addition of Two numbers:",self.num1 + self.num2)

add = calculator(3,4)
add.addition()

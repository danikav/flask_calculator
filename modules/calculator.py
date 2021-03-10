class Calculator():

    # def __init__(self):


    def add(self, number_1, number_2):
        return (number_1 + number_2)

    def subtract(self, number_1, number_2):
        return number_1 - number_2

    def multiply(self, number_1, number_2):
        return number_1 * number_2

    def divide(self, number_1, number_2):
        if number_1 >= 0 and number_2 >=0:
            return number_1 / number_2

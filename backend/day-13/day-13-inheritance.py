class BasicCalculator:
    def sum(self, numlist: list):
        _sum = 0

        for num in numlist:
            _sum += num

        return _sum

class ComplexCalculator(BasicCalculator):
    def power(self, base, exponent):
        return pow(base, exponent)
    
    def abs(self, number):
        return abs(number)
        
basic = BasicCalculator()
complex = ComplexCalculator()

# print(basic.sum([1, 2, 3]))
print(complex.power(2,5))
print(complex.abs(-100))


class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        sum = 0
        # O(sqrt(n)) instead of brute-force technique O(n)
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                # If divisors are equal, print only one
                if n / i == i:
                    sum += i
                # Otherwise print both
                else:
                    sum += i
                    sum += n // i
        return sum


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)

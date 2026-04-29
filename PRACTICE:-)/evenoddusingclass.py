class NumberCheck:
    def is_even(self, num):
        if num % 2 == 0:
            return True
        else:
            return False
    
    def is_odd(self, num):
        if num % 2 != 0:
            return True
        else:
            return False
check = NumberCheck()
num = 69
if check.is_even(num):
    print('The number', num, 'is even')
else:
    print('The number', num, 'is odd')

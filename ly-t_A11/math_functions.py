#math_functions.py
def power(num, power):
    return num**power
    
def divide(num, divisor):
    if divisor == 0:
        return "The divisor cannot be 0"
    else:
        return num/divisor
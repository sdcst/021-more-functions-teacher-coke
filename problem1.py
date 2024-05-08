#!python3
"""
Create a function that converts from degrees F to degrees C or
vice versa, depending on which initial unit is given
2 input parameters:
float: the number of degrees
string: the unit that you currently have: may be 'C' of 'F'

return: float the number of degrees of the other unit. Round answers to 2 decimals

Sample assertions:
assert convertTemp(10,'C') == 50
assert converTemp(32,'F') == 0
"""


def convertTemp(temp, unit):
    if unit == 'C':
        d = temp * (9/5) + 32
        d = round(d, 2)
        return d
    elif unit == 'F':
        d = (temp - 32) * (5/9)
        d = round(d, 2)
        return d


def tests():
    assert convertTemp(10, 'C') == 50.00
    assert convertTemp(32, 'F') == 0.00
    assert convertTemp(100, 'C') == 212.00
    assert convertTemp(100, 'F') == 37.78
    
    
if __name__ == "__main__":
    tests()
#!python3
"""
##### Problem 2
Create a function that determines if a triangle is scalene, right or obtuse.  
3 input parameters:  
float: one side  
float: another side  
float: 3rd side  

return:
0 : triangle does not exist
1 : if the triangle is acute
2 : if the triangle is right
3 : if the triangle is obtuse

Sample assertions:  
assert triangle(12,5,13) == 2     
assert triangle(5,3,3) == 3  
assert triangle(5,15,12) == 3  
assert triangle(1,1,4) == 0  
(2 points)
"""


def triangle(a, b, c):
    abc = [a, b, c]
    abc.sort()
    if abc[0] + abc[1] < abc[2]:
        return 0
    if abc[2] ** 2 == abc[0] ** 2 + abc[1] ** 2:
        return 2
    elif abc[2] ** 2 > abc[0] ** 2 + abc[1] ** 2:
        return 3
    elif abc[2] ** 2 < abc[0] ** 2 + abc[1] ** 2:
        return 1
    else:
        return 0


def tests():
    assert triangle(12, 5, 13) == 2
    assert triangle(5, 3, 3) == 3
    assert triangle(5, 15, 12) == 3
    assert triangle(1, 1, 4) == 0


if __name__ == "__main__":
    tests()

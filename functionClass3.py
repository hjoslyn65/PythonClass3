import math


def HelloWorld():
    print("HelloWorld")

def MathFormulas():
    print("c**2==a**2+b**")

def list_iterate():
    list1 = [0, 1, 2, 3, 4, 5]
    for x in list1:
        print(x+1)

def fruits_iterate():
    fruits1 = ["apple", "banana", "cherry"]
    for x in fruits1:
        print(x)

def quadraticForumla():
    a = input("a = ?")
    b = input("b = ?")
    c = input("c = ?")
    x = ((-b+math.sqrt(b**2-4*a*c))/(2*a))
    y = ((-b-math.sqrt(b**2-4*a*c))/(2*a))
    listquad = [x, y]
    for variable in listquad:
        print(variable)






# print("first root = {}".format(quadraticForumla(aInput, bInput, cInput)))
#
# def quadraticForumlaNeg(a, b, c):
#     x = ((-b-math.sqrt(b**2-4*a*c))/(2*a))
#     return x
#
# print("2nd root = {}".format(quadraticForumlaNeg(aInput, bInput, cInput)))
#
#
#
# a = int(input("enter the number"))
# b = int(input("enter the number"))
# c = int(input("enter the number"))

def test_calc(a):

    if a == 0 or 5 <= a <= 20 or a % 10 >= 5 or 11 <= a % 100 <= 15 or a % 10 == 0:
        case = str(a) + "abc"
    elif a % 10 == 1 or a == 1:
        case = str(a) + "def"
    else:
        case = str(a)+ "ghi"
    return case

# a = print(test_calc(234))
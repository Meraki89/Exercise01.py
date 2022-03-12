def name_age():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print("Hello " + name + ". Your age is: " + age)
    return name+age


def swap_integers(num1, num2):
    print("x=", num1)
    print("y=", num2)
    temp = num1
    num1 = num2
    num2 = temp
    print()
    print("After swap:")
    print("x=", num1)
    print("y=", num2)
    print()
    return str(num1)+str(num2)


def check_numbers(num1, num2):
    print("Condition 1: At least one number is divisible by 6 ")
    print("Condition 2: Both numbers are divisible by 10")
    print("Number 1:", num1)
    print("Number 2:", num2)

    if (num1 % 6 == 0 or num2 % 6 == 0) and (num1 % 10 == 0 and num2 % 10 == 0):
        print("Both conditions are true")
        return True
    else:
        print("Either only one or no condition is true")
        return False


def sum_up(num1, num2):
    print("Number 1 =", num1)
    print("Number 2 =", num2)
    total = 0
    for i in range(num1, num2 + 1):
        total = total + i
    if num2 < num1:
        return 0
    elif num1 < 0 or num2 < 0:
        return 0
    else:
        return total


def circle_area(r1, r2, r3):
    π = 3.141
    area_of_circle1 = π * r1 * r1
    print("The area of the first circle with a radius of " + str(r1) + " is", area_of_circle1)

    area_of_circle2 = π * r2 * r2
    print("The area of the second circle with a radius of " + str(r2) + " is", area_of_circle2)

    area_of_circle3 = π * r3 * r3
    print("The area of the third circle with a radius of " + str(r3) + " is", area_of_circle3)
    result = area_of_circle1 + area_of_circle2 + area_of_circle3
    print("The sum of all three circle areas is " + str(result))
    return result


def check_string(text):
    if (text.startswith("a") or text.startswith("A")) or (text.endswith("a")) or text.endswith("A"):
        print("Yippie! This text either starts or ends with A/a!")
        return True
    else:
        print("Awww, not this time! Unfortunately this text does not start or end with A/a")
        return False


def triangle(rows):
    n = rows
    for i in range(1, n + 1):
        print("* " * i + " " * (n - i))
print("Digite os valores de X e Y:")
x = float(input())
y = float(input())

while x != 0 and y != 0:
    if x > 0 and y > 0:
        print("Q1")
    elif x < 0 and y > 0:
        print("Q2")
    elif x < 0 and y < 0:
        print("Q3")
    elif x > 0 and y < 0:
        print("Q4")

    print("Digite os valores de X e Y:")
    x = float(input())
    y = float(input())

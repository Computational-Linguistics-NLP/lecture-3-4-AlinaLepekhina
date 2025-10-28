"""a = int(input())
if a % 400 == 0 or a % 4 == 0 and a % 100 != 0
    print("YES")
else:
    print("NO")"""


"""a = int(input())
if a % 400 == 0:
    print("yes")
else:
    if a % 100 == 0:
        print("no")
    else:
        if a % 4 == 0:
            print("yes")
        else:
            print("no")"""


a = int(input())
if a % 400 == 0:
    print("yes")
elif a % 100 == 0:
    print("no")
elif a % 4 == 0:
    print("yes")
else:
    print("no")

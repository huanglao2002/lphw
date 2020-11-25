
numbers = []

def test_while(i,num):
    for i in range(i,num):
        print(f"At the top i is {i}")
        numbers.append(i)

        #i = i + 1
        #num  = num  + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    print("The numbers: ")

    for n in numbers:
        print(n)

i = 2
num = 10
test_while(i,num)
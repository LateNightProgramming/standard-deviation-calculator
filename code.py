from math import sqrt

class v:
    data = []

def maths(size): #size refers to if its a sample or population, kinda stupid fucking variable name but im too lazy to give an actual fuck
    mean = 0
    total = 0
    for num in v.data:
        mean += int(num)
    mean /= len(v.data)
    for x in range(len(v.data)):
        v.data[x-1] -= mean
        v.data[x-1] = pow(v.data[x-1], 2)
        total += v.data[x-1]
    if size == 0:
        total /= (len(v.data)-1)
    else:
        total /= len(v.data)
    return ("standard deviation = " + str(sqrt(total)))
    
def setup():
    inp = input("input a value ")
    if inp != "end":
        try:
            v.data.append(int(inp))
        except:
            print("invalid response")
            setup()
        else:
            setup()
    else:
        print("data process ended")
    while True:
        inp = input("is this a population or a sample? ").lower()
        if inp == "sample":
            print(maths(0))
            exit()
        elif inp == "population":
            print(maths(1))
            exit()
        else:
            print("invalid response")
setup()

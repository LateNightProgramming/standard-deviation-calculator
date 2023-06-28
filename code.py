from math import sqrt

class v:
    data = []

def sample():
    mean = 0
    total = 0
    for num in v.data:
        mean += int(num)
    mean /= len(v.data)
    for x in range(len(v.data)):
        v.data[x-1] -= mean
        v.data[x-1] = pow(v.data[x-1], 2)
        total += v.data[x-1]
    total /= (len(v.data)-1)
    print("standard deviation = " + str(sqrt(total)))
    exit()
    
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
            sample()
            break
        elif inp == "population":
            print("still working on that")
            break
        else:
            print("invalid response")
            
setup()

from matplotlib import pyplot as plt
def conjecture(x):
    thisarray = []
    thisarray.append(x)
    steps = 0
    while x != 1:
        if (x%2) == 0:
            x = x/2   
            thisarray.append(x)
            steps = steps + 1
        else:
            x = 3 * x + 1           
            thisarray.append(x)
            steps = steps + 1
    print("total steps: ",steps)
    plt.plot(thisarray)
    plt.show()
    

if __name__ == "__main__":
    x = int(input())
    if x < 1:
        print("The number is invalid")
    else:
        conjecture(x)
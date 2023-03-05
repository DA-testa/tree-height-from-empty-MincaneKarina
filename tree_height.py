# python3

import sys
import threading


def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Your code here

    list = []
    for p_str in parents.split():
        p_int = int(p_str)
        list.append(p_int)
    #print(list)

    i = 0
    x = 0
    k = 0
    a = []
    for index in range(0, n):
        a.insert(index,0)
    b = [None] * n
    c = []
    while x != n:
        print("turpina")   
        print(list[i])
        
        if b[i] != 1 :
            print("vel nav parbaudits")
            c.append(i)
            print(c)
            for item in c:
                a[item] = a[item] + 1
                
        else: 
            print("ir parbaudits")
            #print(i) 
            print(c)
            if c:
                print("nonaca te")
                print(i)
                a[c[-1]] =a[i]  + 1
            else: a[list.index(i)] =a[i]  + 1  
            c = []
        b[i] = 1
        print(a)
        print(b)
        #a[i] = 0
        
        i = list[i]

        if i == -1:
            print (" i ir -1")
            x = 0
            k = 0
            
            for item in b:
                if item == None:
                    i = b.index(item)  
                    break
                else: 
                    x = x + 1
            if x == n and i == -1:
                print("ff")
                print(c)
                print(i)
                for item in c:
                    j = list.index(i)
                    a[item] = a[item] + 1
            else: c = []
    print("Apmeklejums")
    print(b)
    print("a")
    print(a)

    max_height = 0
    for item in a:
        if item > max_height:
            max_height = item

    return max_height

def main():
    # implement input form keyboard and from files
    text = input()
    if "I" in text:
        n = int(input())
        parents = input()
        print(compute_height(n,parents))
    elif "F" in text:
        filename = input()
        with open ("./test/" + filename, mode="r") as file:
            n = file.readline()
            parents =file.readline()
        print(compute_height(n,parents))
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

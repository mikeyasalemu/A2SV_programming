if __name__ == '__main__':
    N = int(input())
    lst =[]
    inputs = []
    for iterate in range(N):
        inputs.clear()
        inputs = input().split()
        if inputs[0] == "insert":
            lst.insert(int(inputs[1]), int(inputs[2]))
        elif inputs[0] == "print":
            print(lst)
        elif inputs[0] == "remove":
            lst.remove(int(inputs[1]))
        elif inputs[0] == "append":
            lst.append(int(inputs[1]))
        elif inputs[0] == "sort":
            lst.sort()
        elif inputs[0] == "pop":
            lst.pop()
        elif inputs[0] == "reverse":
            lst.reverse()
        

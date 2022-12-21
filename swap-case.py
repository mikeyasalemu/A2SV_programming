def swap_case(s):
    r = ""
    for x in s:
        if x.islower():
            r += x.upper()
        else:
            r += x.lower()
    return r

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

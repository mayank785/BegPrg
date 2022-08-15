# use a tuple and count the even and odd numbers in it and finally print the count

T = (20, 12, 15, 563, 1)        # can change the values inside
def cnt(t):
    ce = 0
    co = 0
    for i in range(len(t)):
        if t[i] % 2 == 0:
            ce += 1
        else:
            co += 1
    print(f'Even = {ce} and Odd = {co}')
cnt(T)

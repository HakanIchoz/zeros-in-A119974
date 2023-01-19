def nfinder(x):
    while x%2 == 0:
        x = x/2
    return int((x+1)/2)

def zerofinder(x):
    if x % 2 == 1 or x < 3:
        return '​'
    dividing_point = nfinder(x)
    totalzeros = int(((x - 3)/2))
    firstsetofzeros = dividing_point - 1
    print(str(firstsetofzeros) + '' + ',', end='')
    print(str(totalzeros - firstsetofzeros + 1))

for i in range(3,25):
    if i % 2 == 0:
        print(str(i) + ' ', end='')
    zerofinder(i)
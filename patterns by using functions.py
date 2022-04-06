#patterns by using functions
def pattern(i,j):
    for row in range(i+1):
        for col in range(j+1):
            if (col==3):
                print('*',end='')
            else:
                print(end=' ')
        print()
x=pattern(5,5)

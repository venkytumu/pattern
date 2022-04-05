'''#pattern of c
for row in range(7):
    for col in range(5):
        if ((row==0 or row==6) and (col!=0)) or ((col==0) and (row>0 and row<6)):
            print('*',end='')


        else:
            print(end=' ')
    print()'''
'''#pattern of D
for row in range(7):
    for col in range(5):
        if (col==0) or ((row==0 or row==6) and (col<4)) or ((col==4) and (row>0 and row<6)):
            print('*',end='')


        else:
            print(end=' ')
    print()
'''
'''
#pattern of E
for row in range(7):
    for col in range(5):
        if (row==0 or row==3 or row==6 or col==0):
            print('*',end='')


        else:
            print(end=' ')
    print()
    '''
'''
#pattern of F
for row in range(7):
    for col in range(5):
        if (row==0 or row==3 or col==0):
            print('*',end='')


        else:
            print(end=' ')
    print()
    '''
'''
#pattern of G
for row in range(7):
    for col in range(5):
        if (row==0 or row==6 or col==0)or (col==4 and (row> 3 and row<6)) or (row==3 and (col>2 and col<5)):
            print('*',end='')


        else:
            print(end=' ')
    print()
    '''
'''
#pattern of H
for row in range(7):
    for col in range(5):
        if (col==0 or row==3 or col==4):
            print('*',end='')


        else:
            print(end=' ')
    print()
'''
'''
#pattern of I
for row in range(7):
    for col in range(5):
        if (col==3):
            print('*',end='')


        else:
            print(end=' ')
    print()
'''
'''
#pattern of J
for row in range(7):
    for col in range(5):
        if (row==0 or (col==2 and row<6) or (col==1 and row==6) or (col==0 and row==5)):
            print('*',end='')


        else:
            print(end=' ')
    print()
'''
#pattern of K
for row in range(7):
    for col in range(5):
        if (row==0 or row==3 or row==6 or col==0):
            print('*',end='')


        else:
            print(end=' ')
    print()




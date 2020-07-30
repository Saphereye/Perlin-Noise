import os
os.chdir(os.getcwd())
if __name__=="__main__":
    rang=[120,40]
    val=value(rang)
    val=noise(val)
    print(val)
    print()
    for i in val:
        print(i)
        

    for i in last(val):
		#chr(664) is mountains, O is plateaus,. is plains and ' ' is water(for reference)
        print()
        for j in i:
            if j==1:
                print('.',end='')
            elif j==4:
                print('O',end='')
            elif j==6:
                print(chr(664),end='')
            elif j==-9:
                print(' ',end='')
            elif j==None:
                print('!',end='')
            else:
                print('#',end='')

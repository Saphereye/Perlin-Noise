#Seed is the list which makes the code random
#rang is the size of world eg.[30,10]
def fun(x,seed):
    return (seed[0]*(sin((seed[1]*x)+seed[2])))

def value(rang):
    return [[i for i in range(rang[0])] for j in range(rang[1])]

def val_add(l,value):
    if value==None:
        return l
    else:
        l=l[:-1]
        l.append(value)
        return l

def highest(list):
    element=0
    count=0
    for i in list:
        if list.count(i)>count:
            count=list.count(i)
            element=i
    else:
        return element
				
def last(val):
    x=val
#6,4,1,-9 are the ouputs of the current seed
    for k in range(len(val)):
        for i in range(len(val)-2):
            for j in range(len(val[i])-2):
                    if val[i][j]==6:
                        if val[i][j-1]!=6:
                            val[i][j-1]=4
                        if val[i][j+1]!=6:
                            val[i][j+1]=4
                        if val[i-1][j]!=6:
                            val[i-1][j]=4
                        if val[i+1][j]!=6:
                            val[i+1][j]=4
                    elif val[i][j]==4:
                        if val[i][j-1]!=4 and val[i][j-1]!=6:
                            val[i][j-1]=1
                        if val[i][j+1]!=4 and val[i][j-1]!=6:
                            val[i][j+1]=1
                        if val[i-1][j]!=4 and val[i][j-1]!=6:
                            val[i-1][j]=1
                        if val[i+1][j]!=4 and val[i][j-1]!=6:
                            val[i+1][j]=1
                    elif val[i][j]==1:
                        if val[i][j-1]!=1 and val[i][j-1]!=4 and val[i][j-1]!=6:
                            val[i][j-1]=-9
                        if val[i][j+1]!=1 and val[i][j-1]!=4 and val[i][j-1]!=6:
                            val[i][j+1]=-9
                        if val[i-1][j]!=1 and val[i][j-1]!=4 and val[i][j-1]!=6:
                            val[i-1][j]=-9
                        if val[i+1][j]!=1 and val[i][j-1]!=4 and val[i][j-1]!=6:
                            val[i+1][j]=-9

def noise(val):
	#Gives the random set
    for i in range(len(val)):
        for j in range(len(val[i])):
            val[i][j]=int((fun(randint(0,3),seed)))
    return val

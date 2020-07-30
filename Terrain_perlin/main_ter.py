from math import sin
from random import randint
seed=[randint(0,10) for i in range(9)]

def fun(x,seed):
    return (seed[0]*(sin((seed[1]*x)+seed[2])))*(seed[3]*(sin((seed[4]*x)+seed[5])))*(seed[6]*(sin((seed[7]*x)+seed[8])))
def main():
        im = Image.new('L', (width, height))
        for i in range(-10,11):
            for y in range(0, height):
                for x in range(0, width):
                    value = (fun(randint(0,10),seed))
                    color = int((value+i) * 128)
                    im.putpixel((x, y), color)
            im.save('Perlin.png')
            im.show()
#i=1,2,3 for best result, mostly
if __name__=="__main__":
	from PIL import Image
	height = 100
	width = 100
	main()
	
"""This code will produce ten images of 100x100 dimension which are to
be then compiled together to get the required terrain"""

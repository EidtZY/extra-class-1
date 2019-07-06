import math

f = open('fermat.txt','w')

for a in range(1,100):
    #print('a.%d' % (a))
    for b in range(a,100):
        #print('b.%d' % (b))
        sum = a*a + b*b
        c = math.sqrt(sum)
        #print(c)
        if (c % 1) == 0:
            print('right')
            line1 = ('a-b-c=%d-%d-%d\n' % (a,b,c))
            f.write(line1)
        else:
            print('no')

f.close()

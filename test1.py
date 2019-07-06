'''
s1 = 'hello'
s2 = 'world'
s3 = ' '
print(s1+s3+s2)

for i in range(1,10):
    print(i)
'''

for x in range(1,3):
    print('\tx.%d' % (x))
    for y in range(1,3):
        print('\t\ty.%d' % (y))
        for z in range(1,3):
            print('\t\t\tz.%d' % (z))
            print('\t\t\t\tx-y-z = %d-%d-%d' % (x,y,z))

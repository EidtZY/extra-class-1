import random
filename1 = 'test1.txt'
f1 = open(filename1,'w')
f1.write('-------maths-------\n')
f1.close()


filename2 = 'test2.txt'
f2 = open(filename2,'w')
f2.write('-------maths(含答案)-------\n')
f2.close()


# ---
filename1 = 'test1.txt'
f1 = open(filename1,'a')

filename2 = 'test2.txt'
f2 = open(filename2,'a')

#-----
for i in range(1,21):
    line1 = ''
    line2 = ''
    for j in range(1,6):

        # fbb -----
        #line1 = line1 + 'a + b =  \t\t'
        #line2 = line2 + 'a + b = c\t\t'
        a = random.randint(1,99)
        b = random.randint(1,99)
        op = random.randint(1,4)
        if op == 1:
            line1 = line1 + '%02d + %02d = \t\t' % (a,b)
            c = a + b
            line2 = line2 + '%02d + %02d = %02d \t\t' % (a,b,c)

        if op == 2:
            line1 = line1 + '%02d - %02d = \t\t' % (a,b)
            c = a - b
            line2 = line2 + '%02d - %02d = %02d  \t\t' % (a,b,c)

        if op == 3:
            line1 = line1 + '%02d * %02d = \t\t' % (a,b)
            c = a * b
            line2 = line2 + '%02d * %02d = %02d  \t\t' % (a,b,c)

        if op == 4:
            line1 = line1 + '%02d / %02d = \t\t' % (a,b)
            c = a / b
            line2 = line2 + '%02d / %02d = %02d  \t\t' % (a,b,c)



        # fbe ------

    line1 = line1 + '\n'
    line2 = line2 + '\n'

    f1.write(line1)
    f2.write(line2)

#------------
f1.write('-------ending-------\n')
f2.write('-------ending-------\n')
f1.close()
f2.close()

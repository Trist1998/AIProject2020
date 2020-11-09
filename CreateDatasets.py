import random
true = open('data/cleanTrue.csv', 'r').readlines()
false = open('data/cleanFake.csv', 'r').readlines()

trainData = open('data/train.csv', 'w')
testData = open('data/test.csv', 'w')
trainData.write("title,text,subject,date,truth\n")
testData.write("title,text,subject,date,truth\n")


for i in range(1, int(len(true))):
    rand = random.randint(0, 1)
    if rand == 1:
        trainData.write(true[i][0: -1] + ', 1\n')
        testData.write(false[i][0: -1] + ', 0\n')
    else:
        testData.write(true[i][0: -1] + ', 1\n')
        trainData.write(false[i][0: -1] + ', 0\n')

trainData.close()
testData.close()

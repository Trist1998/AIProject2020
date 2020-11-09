false = open('raw/Fake.csv', 'r').readlines()
true = open('raw/True.csv', 'r').readlines()
cleanTrueData = open('cleanTrue.csv', 'w')
cleanFakeData = open('cleanFake.csv', 'w')
cleanTrueData.write("title,text,subject,date,truth\n")
cleanFakeData.write("title,text,subject,date,truth\n")

openQuote = False
for i in range(1, int(len(false))):
    line = false[i].replace("\n", "")
    cleanFakeData.write(line)
    if len(line) == 1:
        openQuote = not openQuote
    else:
        if openQuote:
            cleanFakeData.write("\n")

openQuote = False
for i in range(1, int(len(true))):
    line = true[i].replace("\n", "")
    cleanTrueData.write(line)
    if len(line) == 1:
        openQuote = not openQuote
    else:
        if openQuote:
            cleanTrueData.write("\n")

# for i in range(1, int(len(false))):
#     line = false[i].replace("\n", "")
#     if len(line) == 1:
#         print("Hello: " + str(i))
#         #cleanData.write(line + "\n")

#cleanData.close()

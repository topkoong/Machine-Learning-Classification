import os
os.chdir('../Feature Vector Files')
#os.chdir('browsing/USER1_b_1499548549244')
user1_src_filename = "User1.txt"
user2_src_filename = "User2.txt"
user3_src_filename = "User3.txt"
user4_src_filename = "User4.txt"
user5_src_filename = "User5.txt"
user6_src_filename = "User6.txt"
user7_src_filename = "User7.txt"
user8_src_filename = "User8.txt"
dest_filename = "trainUser1.txt"
# first 3823 lines from User1
# first 546 lines from others
def generateTrainUserDataSet():
    generateTrainUser1()
    generateTrainUser2()
    generateTrainUser3()
    generateTrainUser4()
    generateTrainUser5()
    generateTrainUser6()
    generateTrainUser7()
    generateTrainUser8()

def generateTrainUser1():
    lineNum = 1
    user1InputFile = open(user1_src_filename, 'r') # open file for reading
    outputFile = open(dest_filename, 'a') # open file for appending
    for line in user1InputFile.readlines():
        if(lineNum == 3823):
            user1InputFile.close()
            outputFile.close()
        else :
            print("Reading \n\n %s \nfrom line# %d \n in %s\n" % (line, lineNum, user1_src_filename))
            print("=====================================\n")
            print("Writing \n\n %s \nto line# %d in %s\n" % (line, lineNum, dest_filename))
            print("=====================================\n")
            outputFile.write(line.strip("\n")+ ", 1\n")
            lineNum += 1

def generateTrainUser2():
    lineNum = 1
    user2InputFile = open(user2_src_filename, 'r') # open file for reading
    outputFile = open(dest_filename, 'a') # open file for appending
    for line in user2InputFile.readlines():
        if(lineNum == 546):
            user2InputFile.close()
            outputFile.close()
        else :
            print("Reading \n\n %s \nfrom line# %d \n in %s\n" % (line, lineNum, user2_src_filename))
            print("=====================================\n")
            print("Writing \n\n %s \nto line# %d in %s\n" % (line, lineNum, dest_filename))
            print("=====================================\n")
            outputFile.write(line.strip("\n")+ ", 1\n")
            lineNum += 1

def generateTrainUser3():
    lineNum = 1
    user3InputFile = open(user3_src_filename, 'r') # open file for reading
    outputFile = open(dest_filename, 'a') # open file for appending
    for line in user3InputFile.readlines():
        if(lineNum == 546):
            user3InputFile.close()
            outputFile.close()
        else :
            print("Reading \n\n %s \nfrom line# %d \n in %s\n" % (line, lineNum, user3_src_filename))
            print("=====================================\n")
            print("Writing \n\n %s \nto line# %d in %s\n" % (line, lineNum, dest_filename))
            print("=====================================\n")
            outputFile.write(line.strip("\n")+ ", 1\n")
            lineNum += 1

def generateTrainUser4():
    lineNum = 1
    user4InputFile = open(user4_src_filename, 'r') # open file for reading
    outputFile = open(dest_filename, 'a') # open file for appending
    for line in user4InputFile.readlines():
        if(lineNum == 546):
            user4InputFile.close()
            outputFile.close()
        else :
            print("Reading \n\n %s \nfrom line# %d \n in %s\n" % (line, lineNum, user4_src_filename))
            print("=====================================\n")
            print("Writing \n\n %s \nto line# %d in %s\n" % (line, lineNum, dest_filename))
            print("=====================================\n")
            outputFile.write(line.strip("\n")+ ", 1\n")
            lineNum += 1

def generateTrainUser5():
    lineNum = 1
    user5InputFile = open(user5_src_filename, 'r') # open file for reading
    outputFile = open(dest_filename, 'a') # open file for appending
    for line in user5InputFile.readlines():
        if(lineNum == 546):
            user5InputFile.close()
            outputFile.close()
        else :
            print("Reading \n\n %s \nfrom line# %d \n in %s\n" % (line, lineNum, user5_src_filename))
            print("=====================================\n")
            print("Writing \n\n %s \nto line# %d in %s\n" % (line, lineNum, dest_filename))
            print("=====================================\n")
            outputFile.write(line.strip("\n")+ ", 1\n")
            lineNum += 1

def generateTrainUser6():
    lineNum = 1
    user6InputFile = open(user6_src_filename, 'r') # open file for reading
    outputFile = open(dest_filename, 'a') # open file for appending
    for line in user6InputFile.readlines():
        if(lineNum == 546):
            user6InputFile.close()
            outputFile.close()
        else :
            print("Reading \n\n %s \nfrom line# %d \n in %s\n" % (line, lineNum, user6_src_filename))
            print("=====================================\n")
            print("Writing \n\n %s \nto line# %d in %s\n" % (line, lineNum, dest_filename))
            print("=====================================\n")
            outputFile.write(line.strip("\n")+ ", 1\n")
            lineNum += 1

def generateTrainUser7():
    lineNum = 1
    user7InputFile = open(user7_src_filename, 'r') # open file for reading
    outputFile = open(dest_filename, 'a') # open file for appending
    for line in user7InputFile.readlines():
        if(lineNum == 546):
            user7InputFile.close()
            outputFile.close()
        else :
            print("Reading \n\n %s \nfrom line# %d \n in %s\n" % (line, lineNum, user7_src_filename))
            print("=====================================\n")
            print("Writing \n\n %s \nto line# %d in %s\n" % (line, lineNum, dest_filename))
            print("=====================================\n")
            outputFile.write(line.strip("\n")+ ", 1\n")
            lineNum += 1

def generateTrainUser8():
    lineNum = 1
    user8InputFile = open(user8_src_filename, 'r') # open file for reading
    outputFile = open(dest_filename, 'a') # open file for appending
    for line in user8InputFile.readlines():
        if(lineNum == 546):
            user8InputFile.close()
            outputFile.close()
        else :
            print("Reading \n\n %s \nfrom line# %d \n in %s\n" % (line, lineNum, user8_src_filename))
            print("=====================================\n")
            print("Writing \n\n %s \nto line# %d in %s\n" % (line, lineNum, dest_filename))
            print("=====================================\n")
            outputFile.write(line.strip("\n")+ ", 1\n")
            lineNum += 1




generateTrainUserDataSet()

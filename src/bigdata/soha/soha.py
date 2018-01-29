import os
import csv
import operator

for filename in os.listdir("/home/kumin/Dropbox/DATN2016/code/ClassifyGender/input"):
    fr = open(
        "/home/kumin/Dropbox/DATN2016/code/ClassifyGender/input/" + filename, "r")
    fw = open("/home/kumin/Dropbox/DATN2016/code/ClassifyGender/output/" + filename, "w")

    frCsv = csv.reader(fr, delimiter=",", quotechar="\"")
    for row in frCsv:
        csvLineOutput = "\"" + row[0] + "\",\"" + row[1] + "\","
        phoneStr = row[2].split(",")
        emailStr = row[3].split(",")

        if len(phoneStr) > 3:
            phoneDic = {}
            for phone in phoneStr:
                if ":" in phone:
                    phoneDic.update({phone.split(":")[0]: phone.split(":")[1]})
                else:
                    try:
                        phoneDic.update({phone: "0.1000000"})
                    except ValueError as e:
                        print filename+","+phone
            phoneDicSorted = sorted(phoneDic.items(), key=operator.itemgetter(1), reverse=True)

            csvLineOutput += "\"" + phoneDicSorted[0][0] + ":" + phoneDicSorted[0][1] + "," + \
                             phoneDicSorted[1][0] + ":" + phoneDicSorted[1][1] + "," + \
                             phoneDicSorted[2][0] + ":" + phoneDicSorted[2][1] + "\","

        else:
            csvLineOutput += "\"" + row[2] + "\","

        if len(emailStr) > 3:
            emailDic = {}
            for email in emailStr:
                if ":" in email:
                    emailDic.update({email.split(":")[0]: email.split(":")[1]})
                else:
                    emailDic.update({email: "0.1000000"})
            emailDicSorted = sorted(emailDic.items(), key=operator.itemgetter(1), reverse=True)

            csvLineOutput += "\"" + emailDicSorted[0][0] + ":" + emailDicSorted[0][1] + "," + \
                             emailDicSorted[1][0] + ":" + emailDicSorted[1][1] + "," + \
                             emailDicSorted[2][0] + ":" + emailDicSorted[2][1] + "\""

        else:
            csvLineOutput += "\"" + row[3] + "\""

        # print csvLineOutput
        fw.write(csvLineOutput + "\n")
    fr.close()
    fw.close()

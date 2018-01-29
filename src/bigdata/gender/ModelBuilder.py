# -*- coding: utf-8 -*-
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
import codecs

alphabet_vn = [u'a', u'á', u'à', u'ả', u'ã', u'ạ', u'ă', u'ắ', u'ằ', u'ẳ', u'ẵ', u'ặ', u'â', u'ấ', u'ầ', u'ẩ', u'ẫ',
               u'ậ',
               u'b', u'c', u'd', u'đ', u'e', u'é', u'è', u'ẻ', u'ẽ', u'ẹ', u'ê', u'ế', u'ề', u'ể', u'ễ', u'ệ',
               u'g', u'h', u'i', u'í', u'ì', u'ỉ', u'ĩ', u'ị', u'k', u'l', u'm', u'n', u'o', u'ó', u'ò', u'ỏ', u'õ',
               u'ọ',
               u'ô', u'ố', u'ồ', u'ổ', u'ỗ', u'ộ', u'ơ', u'ớ', u'ờ', u'ở', u'ỡ', u'ợ', u'p', u'q', u'r', u's', u't',
               u'u', u'ú', u'ù', u'ủ', u'ũ', u'ụ', u'ư', u'ứ', u'ừ', u'ử', u'ữ', u'ự', u'v', u'x',
               u'y', u'ý', u'ỳ', u'ỷ', u'ỹ', u'ỵ']
last_name = [u'nguyễn', u'trần', u'lê', u'phạm', u'hoàng', u'huỳnh', u'phan', u'vũ', u'võ', u'đặng', u'bùi', u'đỗ',
             u'hồ', u'ngô', u'dương']


def count_feature_en(name):
    alphabet_length = 26
    arr = np.zeros(alphabet_length * 2 + alphabet_length * alphabet_length)
    for ind, x in enumerate(name):
        arr[ord(x) - ord('a')] += 1
        arr[ord(x) - ord('a') + alphabet_length] += 1 + ind

    for x in xrange(len(name) - 1):
        ind = (ord(name[x]) - ord('a')) * alphabet_length + (ord(name[x + 1]) - ord('a')) + alphabet_length * 2
        arr[ind] = +1

    arr[-1] = len(name)
    arr[-2] = ord(name[-2]) - ord('a')
    arr[-3] = ord(name[-1]) - ord('a')

    return arr


def count_feature_vn(name):
    alphabet_length = 89
    arr = np.zeros(alphabet_length * 2 + alphabet_length * alphabet_length)
    for ind, x in enumerate(name):
        # print x
        arr[alphabet_vn.index(x)] += 1
        arr[alphabet_vn.index(x) + alphabet_length] += 1 + ind

    for x in xrange(len(name) - 1):
        ind = alphabet_vn.index(name[x]) * alphabet_length + alphabet_vn.index(name[x + 1]) + alphabet_length * 2
        arr[ind] = +1

    arr[-1] = len(name)
    arr[-2] = alphabet_vn.index(name[-2])
    arr[-3] = alphabet_vn.index(name[-1])

    return arr


def train():
    print "training...!"
    f = codecs.open("../../../data/name_gender.txt", "r", encoding="utf-8")
    X = []
    y = []
    for line in f:
        line = preprocessing_text(line)
        X.append(count_feature_vn(line.split(",")[0]))
        y.append(line.split(",")[1])

    max_accuracy = 0
    for x in xrange(5):
        Xtr, Xt, ytr, yt = train_test_split(X, y, test_size=0.33)
        Xtr_balance = []
        ytr_balance = []
        for i in range(len(ytr) - 1):
            if ytr[i] == 'female':
                for j in xrange(7):
                    Xtr_balance.append(Xtr[i])
                    ytr_balance.append(ytr[i])
            else:
                Xtr_balance.append(Xtr[i])
                ytr_balance.append(ytr[i])
        print str(len(Xtr)) + " " + str(len(Xtr_balance))
        print str(len(ytr)) + " " + str(len(ytr_balance))

        count_male = 0
        count_female = 0
        for label in ytr_balance:
            if label == 'male':
                count_male += 1
            else:
                count_female += 1
        print 'male: ' + str(count_male) + ' female:' + str(count_female)
        clf = RandomForestClassifier(n_estimators=150, min_samples_split=10)
        clf.fit(Xtr_balance, ytr_balance)

        accuracy = np.mean(clf.predict(Xt) == yt)
        if accuracy > max_accuracy:
            joblib.dump(clf, "../../../model/clf_vi.model")
            max_accuracy = accuracy
        print accuracy


def predic_gender_test():
    clf = joblib.load("../../../model/clf_vi.model")
    while True:
        first_name = raw_input("Enter First Name:")
        first_name = unicode(first_name, 'utf-8')
        first_name = preprocessing_text(first_name)
        first_name = first_name.replace(' ', '')

        print first_name

        print clf.predict(count_feature_vn(first_name))

def preprocessing_text(content):
    content = content.lower()
    content = content.rstrip()

    return content


def remove_last_name(full_namne):
    for ln in last_name:
        full_namne = full_namne.re

    return full_namne

if __name__ == '__main__':
    # train()
    predic_gender_test()

    # f = codecs.open("/home/kumin/Dropbox/DATN2016/code/ClassifyGender/data/name_gender.txt", "r", encoding="utf-8")
    #
    # for line in f:
    #     line = line.rstrip()
    #     line = line.split(",")[0]
    #     print type(line)
    #     print line
    #     for ind, x in enumerate(line):
    #         print type(x)
    #         print x
    #         print alphabet_vn.index(x)

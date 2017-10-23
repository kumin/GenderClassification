
from sklearn.model_selection import cross_val_predict
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib
import matplotlib.pyplot as plt
from collections import Counter
import codecs
import re
import pandas as pd
import numpy as np

class Random_Forest:
    def __init__(self):
        self.corpus = []
        self.labels = []
        self.vector_feature = []
        self.clf = RandomForestClassifier(n_jobs=2)

    def preprocessing(self, line):
        line = line.lower()
        return re.sub(r'[\W]', ' ', line, flags=re.UNICODE)

    def create_dictionary_from_text(self):
        fw = codecs.open('/home/kumin/PycharmProjects/SparkExample/data/dict.dc', 'w')
        with codecs.open('/home/kumin/PycharmProjects/SparkExample/data/VCC_2016_Social_Facebook.data', 'r',
                         encoding='utf8') as f:
            # csv_reader = csv.reader(f, delimiter=',', quotechar='"')
            list_word = []
            for line in f:
                line = line.strip()
                if line != '' and not line.startswith('==='):
                    self.labels.append(line.split("###")[0])
                    line = line.split("###")[1]
                    line = self.preprocessing(line)
                    self.corpus.append(line)

                    list_word.extend(line.split())
        word_count = Counter(list_word)
        index_dic =0;
        for count in word_count.items():
            index_dic += 1
            fw.write(str(index_dic)+':')
            fw.write(count[0].encode('utf-8')+':')
            fw.write(str(count[1])+'\n')

    def transform_vector_feature(self):
        vectorizer = CountVectorizer()
        self.vector_feature = vectorizer.fit_transform(self.corpus, self.labels)

        return self.vector_feature

    def train(self):
        self.create_dictionary_from_text()
        self.transform_vector_feature()
        predicted = cross_val_predict(self.clf, self.vector_feature.toarray(), self.labels, cv=10)

        print predicted
        # fig, ax = plt.subplots()
        # ax.scatter(self.labels, predicted)
        # ax.plot([min(self.labels), max(self.labels)], [min(self.labels), max(self.labels)], 'k--', lw=4)
        # ax.set_xlabel('Measured')
        # ax.set_ylabel('Predicted')


        plt.scatter()
        plt.show()
        # self.clf.fit(self.vector_feature.toarray(), self.labels)
        # print self.clf.predict(self.vector_feature.toarray()[2])
        # joblib.dump(self.clf, "/home/kumin/PycharmProjects/SparkExample/models/rdf.model")



if __name__ == '__main__':
    rf = Random_Forest()
    rf.train()


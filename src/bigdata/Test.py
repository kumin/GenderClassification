import os
import sys

os.environ['SPARK_HOME'] = "/home/kumin/VCC/spark-2.0.2"
sys.path.append("/home/kumin/VCC/spark-2.0.2/python/lib/py4j-0.10.3-src.zip")
sys.path.append("/home/kumin/VCC/spark-2.0.2/python")
try:
    from pyspark import SparkContext
    from pyspark import SparkConf

    print "success imported spark";

except ImportError as e:
    print("can not import spark module", e)

from hdfs import InsecureClient

class SparkExample:
    def __init__(self):
        self.conf = SparkConf().setAppName("test_app").setMaster("local")
        self.sc = SparkContext(conf=self.conf)
        self.client = InsecureClient("http://192.168.23.200:9000", "minhhv")

    def writeFileHDFS(self):
        print "writting hdfs"
        fr = open("/home/kumin/PycharmProjects/SparkExample/data/content.txt", "r")
        with self.client.write("hdfs://192.168.23.200:9000/user/minhhv/DataCollection/2017_04_18/content.txt") as writer:
            for line in fr:
                # writer.write("")
                print line
        fr.close()

    def readFileHdfs(self):
        text_file = self.sc.textFile("hdfs://192.168.23.200:9000/user/minhhv/DataCollection/2017_04_18/content.txt/part-00000")
        for line in text_file.collect():
            print line

    def countWord(self):
        text_file = self.sc.textFile("/home/kumin/PycharmProjects/SparkExample/data/content.txt")
        counts = text_file.flatMap(lambda line: line.split(" ")).map(lambda word: (word,1)).reduceByKey(lambda a,b: a+b)

        counts.saveAsTextFile("hdfs://192.168.23.200:9000/user/minhhv/DataCollection/2017_04_18/content.txt")
        # words = self.sc.parallelize(["minh", "dm", "dm"])
        # print words.count()
        # print text_file




if __name__ == '__main__':
    spark = SparkExample()
    # spark.writeFileHDFS()
    # spark.countWord()
    spark.readFileHdfs()
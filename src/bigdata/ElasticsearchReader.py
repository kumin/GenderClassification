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
class SparkElastic:
    def __init__(self):
        self.conf = SparkConf().setAppName("test_app").setMaster("local")
        self.sc = SparkContext(conf=self.conf)
    # def readData(self):

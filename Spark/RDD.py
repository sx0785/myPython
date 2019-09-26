"""
This is for .

Author: Shawn Xiao
"""
#from pyspark.sql import SparkSession
#from pyspark import SparkContext,SparkConf

#from pyspark import SparkConf,SparkContext
from pyspark import SparkConf,SparkContext

import os

os.environ["SPARK_HOME"]="/home/sxiao/Option/Spark"
os.environ["PYSPARK_PYTHON"] ="/usr/local/bin/python3.7"

appname="RDD"
master = "local[*]"
conf = SparkConf().setAppName(appname).setMaster(master)
sc = SparkContext(conf=conf)

lines = sc.textFile("/home/sxiao/Option/Spark/README.md")
#print(lines)
#print(lines.first())
pairs = lines.map(lambda s:(s,1))
counts = pairs.reduceByKey(lambda a,b:a+b)
print(counts.collect())

#counts.first()








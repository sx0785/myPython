#from pyspark.sql import SparkSession
from pyspark import SparkContext,SparkConf
appname="RDD"
master = "local"
conf = SparkConf().setAppName(appname).setMaster(master)
sc = SparkContext(conf=conf)

lines = sc.textFile("C:\src\spark\README.md")
pairs = lines.map(lambda s:(s,1))
print(pairs.reduceByKey(lambda a,b:a+b))





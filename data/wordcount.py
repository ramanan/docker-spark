#!/usr/bin/env python
import sys

from pyspark import SparkContext, SparkConf

if __name__ == "__main__":

   # create Spark context with necessary configuration
   sc = SparkContext("spark://master:7077", "PySpark Word Count Exmaple")

   # read data from text file and split each line into words
   words = sc.textFile("./somelines.txt").flatMap(lambda line: line.split(" "))

   # count the occurrence of each word
   wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

   # save the counts to output
   wordCounts.saveAsTextFile("./output")

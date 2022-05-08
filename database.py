import mysql.connector
import pyspark
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.sql import HiveContext
import sqlalchemy as sa
import pandas as pd
import database
import mysql.connector
import sys
import os




def mysql_connection():
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "#########################",#### REMOVE BEFORE COMMITING CODE
    database = "Shark_Attack_Login",
    )
    #print(mydb)


    # Create Cursor Instance
    
    mycursor = mydb.cursor()
    commit = mydb.commit()
    #mycursor.close()
    return mycursor, commit



def hive_context():
    
    conf = SparkConf()
    sc = SparkContext.getOrCreate(conf=conf)
    hc = HiveContext(sc)
    return hc, sc, 





def spark_session(): 
    conf = SparkConf()    
    sc = SparkContext.getOrCreate(conf=conf)
    sqlContext = SQLContext(spark)
        
    conf = pyspark.SparkConf()\
        .setMaster("local[*]")\
        .setAppName("sharkAnalysis")\
        .setAll([("spark.driver.memory", "1g"),\
        ("spark.executor.memory", "1g")])
        
        
    spark = SparkSession(sc)\
        .builder \
        .master("local[*]") \
        .appName("sharkAnalysis") \
        .config("spark.some.config.option", "some-value")\
        .enableHiveSupport()\
        .getOrCreate()   
    
    
    return conf, spark, sqlContext, sc, conf
    
    
    
    
    
    


# Create Cursor Instance
#my_cursor = mydb.cursor()
#global userName
#global userPassword
#global userPassword2   

#class DB:
    # def __del__(self):
        #self.mydb.close()
        

    # def __init__(self):
        #self.mydb = mysql.connector.connect(
            #host = "localhost",
            #user = "root",
            #passwd = "####################",#### REMOVE BEFORE COMMITING CODE
            #database = "Shark_Attack_Login",
        #)
        #print("Started database connection")
        


    #this will insert into database newly created user
    # def insert_new_user_into_database(self):
        #mycursor = self.mydb.cursor()
        ## NEED TO CREATE SHARKATTACHDATABASE  DATABASE IN MYSQL ######
        #resultSet1 = "INSERT INTO SharkAttackDatabase (userName, userPassword, userPassword2) VALUES (%s, %s, %s)"
        #answer = (userName, userPassword, userPassword2)
        #mycursor.execute(resultSet1,answer)
        #mycursor.commit()
        #userMenu()
        
        #mycursor.close()



    # def do_that_with_connection(self):
    # def connect_to_mysql(self):
        #mycursor = self.mydb.cursor()
        #mydb = mysql.connector.connect(
        #host = "localhost",
        #user = "root",
        #passwd = "#################",#### REMOVE BEFORE COMMITING CODE
        #database = "Shark_Attack_Login",
        #)
        #print(mydb)


        # Create Cursor Instance
        #mycursor = mydb.cursor()
        #mycursor.close()
        
        
        
        
        


    
        
        
 





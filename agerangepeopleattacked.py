import mysql.connector
from queries import typesOfQueries
import pandas as pd
import sys
import os



# Query for average age range of people attacked
def ageRangePeopleAttacked():
    
    typesOfQueries().avgAgePeopleAttacked()
    
    import usermenu


ageRangePeopleAttacked()

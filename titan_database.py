import mysql.connector
import titan_gui
#import hashlib

connection = mysql.connector.connect(
    user="root",
    password="camarlisPASSword1!",
    host= "localhost",
    port = 3306,
)      
            
      
#creates cursor to allow the creation and changing of databases
cursor = connection.cursor()
#executes the create database if not exists
cursor.execute("CREATE DATABASE IF NOT EXISTS titan_db;")

connection = mysql.connector.connect(
    user="root",
    password="camarlisPASSword1!",
    host= "localhost",
    port = 3306,
    database = "titan_db"
)      


cursor = connection.cursor()

#creates tables
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS users(
    ID INT AUTO_INCREMENT PRIMARY KEY,
    usernames VARCHAR(30) NOT NULL ,
    hashed_pass VARCHAR(30) NOT NULL,
    Titan_folder CHAR(50) NOT NULL
    )     
    '''
)

def connect_user_folder():
    #f account is created then
    
    
username = "admin"
password = "test"
add_account = ("INSERT INTO users (usernames, hashed_pass, Titan_folder) VALUES (%s, %s, %s)")
account_test = (username, password, )
cursor.execute(add_account, account_test)

    
#cursor.execute("INSERT INTO users, 'username','hashed_pass' VALUES 'test1', 'test2' ")
#sign up and login check code, passing information from "titan_gui" another file in my code

#def check_signup():
 
 
 
 
    
#def check_login():


connection.commit()
import mysql.connector
import bcrypt


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
        CREATE TABLE IF NOT EXISTS titanUsers(
        ID INT AUTO_INCREMENT PRIMARY KEY,
        userNames VARCHAR(30) NOT NULL,
        hashedPass VARCHAR(30) NOT NULL,
        TitanFolder CHAR(50) NOT NULL 
        )     
        '''     
)

'''
#function that will be used to create an accounr
#funtion gets current input from the entry box and will hash it
def create_acc():
    
    tl = titan_signup() # connects to the titanlogin class file to get user input
    l_pass = tl.get_pass # calluing the fucntion from the class
    print (l_pass)#output to test if the function is grabbing the text


#using bcrypt to hash a password entered by user during login 

bcrypt.hash(, saltRounds, function(err, hash) {
    // Store hash in your password DB.
})

#function that will be used to create an accounr
#funtion gets current input from the entry box and will hash it

def create_acc():
    
    tl = titan_signup() # connects to the titanlogin class file to get user input
    l_pass = tl.get_pass # calluing the fucntion from the class
    print (l_pass)#output to test if the function is grabbing the text
'''
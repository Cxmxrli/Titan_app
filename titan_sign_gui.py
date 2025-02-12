import customtkinter as tk
from PIL import Image
import mysql.connector
import bcrypt
from titan_main_gui import titan_main
from titan_login_gui import titan_login

#used customtkinter documentation to help ith multiwindow development
#used to help with ctk classes: https://www.youtube.com/watch?v=GPcCLiOYVe4
tk.set_appearance_mode("dark")#"light"
#---------------------------------------------------------------------------#
tk.set_appearance_mode("dark")
#class for sighning up
class titan_signup(tk.CTk):
    def __init__(self):  
        super().__init__()
        self.destroy
        self.title("sign up")
        self.geometry("500x550")
        self.resizable(False, False)
        
        #here i define the backround image for light and dark mode so that it changes accordingly
        self.back_img = "image_files/wobbly_image.png"
        self.main_backround = tk.CTkImage(
        light_image=Image.open(self.back_img),
        dark_image=Image.open(self.back_img),
        size=(2000,1000)
        )
        
        self.image_label = tk.CTkLabel(master=self, 
            text="",
            width=650,
            height=650,
            image=self.main_backround
        )
        self.image_label.place(relx=0.5, rely=0.5, relwidth=1.0, relheight=1.0, anchor="center")
        self.image_label = self.main_backround
        
        self.signup_frame = tk.CTkFrame(master=self,
            fg_color="black",
            bg_color="black",
            width=1000,
            height=500,
            border_color="white",
            corner_radius=30,                        
        )
        self.signup_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        self.user_entry = tk.CTkEntry(master=self.signup_frame,
            width=75,
            height=40,
            placeholder_text="Create username",
            placeholder_text_color="grey",
            corner_radius=25,
            show="",
            font=(("comicsans",20)),
            fg_color="black",
            border_width=0.95,
            border_color="white",
            text_color="white"
        )
        self.user_entry.place(relx=0.5, rely=0.3, relwidth=0.4, relheight=0.15, anchor="s")
       
        self.password_entry = tk.CTkEntry(master=self.signup_frame,
            width=75,
            height=40,
            placeholder_text="Create Password",
            placeholder_text_color="grey",
            corner_radius=25,
            show="",
            font=(("comicsans",20)),
            fg_color="black",
            border_width=0.95,
            border_color="white",
            text_color="white"
        )
        self.password_entry.place(relx=0.5, rely=0.35, relwidth=0.4, relheight=0.15, anchor="n")
         
        self.confirm_pass = tk.CTkEntry(master=self.signup_frame,
            width=75,
            height=40,
            placeholder_text="confirm Password",
            placeholder_text_color="grey",
            corner_radius=25,
            show="*",
            font=(("comicsans",20)),
            fg_color="black",
            border_width=0.95,
            border_color="white",
            text_color="white"
        )
        self.confirm_pass.place(relx=0.5, rely=0.55, relwidth=0.4, relheight=0.15, anchor="n")    
        
        self.signup_button = tk.CTkButton(master=self.signup_frame,
            text="Sign up",
            anchor="center",
            corner_radius=25,
            width=75,
            height=40, 
            command=self.sign_up
        )
        self.signup_button.place(relx=0.5, rely=0.70, relwidth=0.4, relheight=0.15, anchor="n")
        
        self.back_button = tk.CTkButton(master=self.signup_frame,
            text="Back",
            anchor="center",
            corner_radius=25,
            width=75,
            height=40,   
        )
        self.back_button.place(relx=0.5, rely=0.85, relwidth=0.4, relheight=0.15, anchor="n")
        
    #function zone -----------------------------------------------------------------
    
    def create_account(self):
        l_pass = self.create_pass.get() 
        salt_rounds = 10
        salt = bcrypt.gensalt(salt_rounds)
        hash_pass = bcrypt.hashpw(l_pass.encode(), salt)
        return (hash_pass)
      
    def back(self):
        self.destroy() 
        main = titan_login()
        main.mainloop()
    
    def sign_up(self):
        
        #gets username and password form customtkinter
        username = self.user_entry.get()
        password = self.password_entry.get()
        confirm = self.confirm_pass.get()
        
        if password != confirm:
            print("passwords do not match")
            
        #connection to the database, between mySQL and visual studio code
        connection = mysql.connector.connect(
            user="root",
            password="camarlisPASSword1!",
            host= "localhost",
            port = 3306,
        )     
        
        cursor = connection.cursor()#cursor to interact with database
        cursor.execute(" CREATE DATABASE IF NOT EXISTS titanDB")
        cursor.execute("USE titanDB")
        
        #creation of database field names and parametres
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS titanUsers(
            ID INT AUTO_INCREMENT PRIMARY KEY,
            userNames VARCHAR(30) NOT NULL,
            hashedPass VARCHAR(30) NOT NULL,
            titanFolder CHAR(50) NOT NULL  
            )
            '''   
        )
        cursor.execute("USE titanUsers")

        #checks id the username entered exists in the table already
        #will regturn an error if the user hasnt
        cursor.execute("SELECT userNames FROM titanUsers;")
        
        #list temportarily containing usernames
        exist_usernames = cursor.fetchall()
        
        #checks if the username is in use and returns an error
        for user in exist_usernames:
            if user in exist_usernames:
                return("username is taken...")
        else:
            
            file = (f"{username}_file") # automatically creates invidivual folder name for user
            if len(username) <= 30 or len(password) <= 30: # check length of input to return error
                user_inp = (username, password, file)
                add_account = ("INSERT IGNORE INTO titanUsers (userNames, hashedPass, titanFolder) VALUES (%s, %s, %s)")
                cursor.execute(add_account, user_inp)
                print("successful account creation")
                connection.commit() 
            else:      
                print("error username or password is too long")
        
if __name__ == "__main__":
    app = titan_signup()
    app.mainloop()

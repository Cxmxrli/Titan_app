import customtkinter as tk
from PIL import Image
import mysql.connector
from titan_main_gui import titan_main
import time
import bcrypt
#used customtkinter documentation to help ith multiwindow development
#used to help with ctk classes: https://www.youtube.com/watch?v=GPcCLiOYVe4
tk.set_appearance_mode("dark")#"light"
#---------------------------------------------------------------------------#

#class for the login window in customtkinter. named "titan_login"
class titan_login(tk.CTk):
    def __init__(self):
        super().__init__()
        self.destroy
        #if user does not exist in database, prompt user to press sign in and pass it in automatcally pass it into sign in menu
        
        
        #functions to set the appearance, size and resolution of thr window
        #currently set to dark mode by defualt
        self.title("---Titan App---")
        self.geometry("700x700")
        self.resizable(False, False)
        
        #frame that holds the elements and buttons used for user input when logging in
        #signing up, or forgetting password
        self.login_frame = tk.CTkFrame (master=self,
            fg_color="black",
            #fg_color="#ff65f3",
            bg_color="transparent",
            width=400,
            height=400,
            border_width=0.9,
            border_color="white",
            background_corner_colors=("black","black","black","black",)
            #background_corner_colors=("white","white","white","white",)
        )
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        #here i define the backround image for light and dark mode so that it changes accordingly
        self.back_img = "image_files/wobbly_image.png"
        self.main_backround = tk.CTkImage(
        light_image=Image.open(self.back_img),
        dark_image=Image.open(self.back_img),
        size=(2000,1000)
        )
    
        
        #label that holds the image, behind other elements to create backround
        #size and position defined here, relwidth/height arguement ensures the
        #image stretched across the whole image
        self.image_label = tk.CTkLabel(master=self, 
            text="",
            width=650,
            height=650,
            image=self.main_backround
        )
        self.image_label.place(relx=0.5, rely=0.5, relwidth=1.0, relheight=1.0, anchor="center")
        
        #frame that holds the elements and buttons used for user input when logging in
        #signing up, or forgetting password
        self.login_frame = tk.CTkFrame (master=self,
            fg_color="black",
            #fg_color="#ff65f3",
            bg_color="transparent",
            width=400,
            height=400,
            corner_radius=30,
            border_width=0.9,
            border_color="white",
            background_corner_colors=("black","black","black","black",)
            #background_corner_colors=("white","white","white","white",)
        )
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        self.info_text = tk.CTkLabel(master=self.login_frame,
            fg_color="black",
            width=75,
            height=5,
            text="Enter username & password",
            text_color="white",
            font=(("Comic Sans",20)),        
        )
        self.info_text.place(relx=0.5, rely=0.125, relwidth=0.7, relheight=0.10, anchor="s" )
        #input areas for username and for password inputs, contain commands wich check 
        #their contents
        self.username_entry = tk.CTkEntry(master=self.login_frame,
            width=75,
            height=40,
            placeholder_text="Username",
            placeholder_text_color="grey",
            corner_radius=25,
            font=(("Comic Sans",20)),
            fg_color="black",
            border_width=0.95,
            border_color="white",
            text_color="white"
        )
        self.username_entry.place(relx=0.5, rely=0.37, relwidth=0.97, relheight=0.23, anchor="s")

        self.password_entry = tk.CTkEntry(master=self.login_frame,
            width=75,
            height=40,
            placeholder_text="Password",
            placeholder_text_color="grey",
            corner_radius=25,
            show="*",
            font=(("Comic Sans",20)),
            fg_color="black",
            border_width=0.95,
            border_color="white",
            text_color="white"
        )
        self.password_entry.place(relx=0.5, rely=0.61, relwidth=0.97, relheight=0.23, anchor="s")
        
        
        #log in button, command will be to check login details
        self.log_button = tk.CTkButton(master=self.login_frame, 
            text="Log In",
            font=(("Comic Sans",20)),
            text_color="white",
            fg_color="#343638",
            #fg_color="#d622dc",
            hover_color="black",
            corner_radius=30,
            height=75,
            width=40,
            command=self.check_user
            #border_width=0.5,
            #border_color="white",
        )
        self.log_button.place(relx=0.495, rely=0.715, relwidth=0.48, anchor="e")
            
        #sign up button, command will be to create account details in database
        self.signup_button = tk.CTkButton(master=self.login_frame, 
            text="Sign up",
            font=(("Comic Sans",20)),
            text_color="white",
            fg_color="#343638",
            #fg_color="#d622dc",
            hover_color="black",
            corner_radius=30,
            height=75,
            width=40,
            command=self.open_signup
            #border_width=0.5,
            #border_color="white",
        )
        self.signup_button.place(relx=0.505, rely=0.715, relwidth=0.48, anchor="w")
            
        #button to enable user to change password when it forgotten
        self.forgot_pass_button = tk.CTkButton(master=self.login_frame, 
            text="forgot password",
            font=(("Comic Sans",20)),
            text_color="white",
            fg_color="#343638",
            #fg_color="#d622dc",
            hover_color="black",
            corner_radius=30,
            height=65,
            width=45,
            command=self.check_user
        )
        self.forgot_pass_button.place(relx=0.5, rely=0.82, relwidth=0.97, anchor="n")
        
        #couple of asthetic gui black lines
        self.gui_label_1 = tk.CTkLabel(master=self,
            bg_color="black",
            text="TITAN",
            text_color="white",
            font=(("Comic Sans",37)),
            width=100,
            height=60,
        )
        self.gui_label_1.place(relx=0.5, rely=0.065, relwidth=1.0, anchor="s")
        
        self.gui_label_2 = tk.CTkLabel(master=self,
            bg_color="black",
            text="",
            text_color="white",
            width=100,
            height=60,
        )
        self.gui_label_2.place(relx=0.5, rely=1.0, relwidth=1.0, anchor="s")
    
        #button to view text in password entry box, used eye icon to depict closed eye
        # master is entry box to place the buttons in the entry box
        self.view_text = tk.CTkButton(master=self.password_entry,
            text="👁",
            font=(("Comic Sans",20)),
            text_color="white",
            fg_color="black",
            hover_color="grey",
            corner_radius=30,
            height=10,
            width=10,
            command=self.view_text
        )
        self.view_text.place(relx=0.98, rely=0.5, anchor="e")
        self.view_text.bind("<ButtonRelease>", command=self.hide_text)
        
        

    #button to hide text in password entry box, uses sideways bracket to depict closed eye
    # master is entry box to place the buttons in the entry box
    
    
    #sets password text to be visible when this fucntion is run
    def view_text(self):
        self.password_entry.configure(show="")
    
    #this function sets the password entry text to be "*" hiding
    #it from the user for security purposes
    def hide_text(self, *args):
        self.password_entry.configure(show="*")
    
    #this function closes the current window and opens the signup class window when pressed
    def open_signup(self):
        self.destroy() 
        main = titan_signup()
        main.mainloop()
    
    #this function checks for test values in entry boxes equal the variables,
    #this system will be integrated with the database systems when it is complete
    def check_user(self):    
        user_check = self.username_entry.get()
        pass_check = self.password_entry.get()
        true_username = "camarli"
        true_password = "password"
        if user_check == true_username and pass_check == true_password:
            self.info_text.configure(text="correct password")
            time.sleep(3)
            self.destroy()
            main = titan_main()
            main.mainloop()
        else:
            self.info_text.configure(text="incorrect username or password")
            
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
    app = titan_login()
    app.mainloop()
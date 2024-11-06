import customtkinter as tk
from PIL import Image
import titan_main_gui
#used customtkinter documentation to help with multiwindow development
#used to help with ctk classes: https://www.youtube.com/watch?v=GPcCLiOYVe4
tk.set_appearance_mode("dark")#"light"
#---------------------------------------------------------------------------#


#class for the login window in customtkinter. named "titan_login"
class titan_login(tk.CTk):
    def __init__(self):
        super().__init__()
        
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
        self.backround_img = tk.CTkImage(
            light_image=Image.open("image_files/wobbly_image.png"),
            dark_image=Image.open("image_files/wobbly_image.png"),
            size=(2000,1000)
        )
        
        #label that holds the image, behind other elements to create backround
        #size and position defined here, relwidth/height arguement ensures the
        #image stretched across the whole image
        self.image_label = tk.CTkLabel(master=self, 
            text="",
            width=650,
            height=650,
            image=self.backround_img
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
            font=(("comicsans",20)),        
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
            font=(("comicsans",20)),
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
            font=(("comicsans",20)),
            fg_color="black",
            border_width=0.95,
            border_color="white",
            text_color="white"
        )
        self.password_entry.place(relx=0.5, rely=0.61, relwidth=0.97, relheight=0.23, anchor="s")
        
        
        #log in button, command will be to check login details
        self.log_button = tk.CTkButton(master=self.login_frame, 
            text="Log In",
            font=(("comicsans",20)),
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
            font=(("comicsans",20)),
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
            font=(("comicsans",20)),
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
            font=(("comicsans",37)),
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
            font=(("comicsans",20)),
            text_color="white",
            fg_color="black",
            hover_color="grey",
            corner_radius=30,
            height=10,
            width=10,
            command=self.view_text
        )
        self.view_text.place(relx=0.98, rely=0.5, anchor="e")
        
        #button to hide text in password entry box, uses sideways bracket to depict closed eye
        # master is entry box to place the buttons in the entry box

        self.hide_text = tk.CTkButton(master=self.password_entry,
            text="‿",
            font=(("comicsans",40)),
            text_color="white",
            fg_color="black",
            hover_color="black",
            corner_radius=30,
            height=2,
            width=10,
            command=self.hide_text
        )
        self.hide_text.place(relx=0.88, rely=0.39, relheight=0.5, anchor="e")
     
    def view_text(self):
        self.password_entry.configure(show="")
   
        
    def hide_text(self):
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
            self.destroy()
            main = titan_main()
            main.mainloop()
        else:
            self.info_text.configure(text="incorrect username or password")
     
       
#class for sighning up
class titan_signup(tk.CTk):
    def __init__(self):  
        super().__init__()
        self.title("sign up")
        self.geometry("500x550")
        self.resizable(False, False)
        
        #here i define the backround image for light and dark mode so that it changes accordingly
        self.backround_signup = tk.CTkImage(
            light_image=Image.open("image_files/wobbly_image.png"),
            dark_image=Image.open("image_files/wobbly_image.png"),
            size=(600,600)
        )
        
        self.image_label = tk.CTkLabel(master=self, 
            text="",
            width=650,
            height=650,
            image=self.backround_signup
        )
        self.image_label.place(relx=0.5, rely=0.5, relwidth=1.0, relheight=1.0, anchor="center")
        
        self.signup_frame = tk.CTkFrame(master=self,
            fg_color="black",
            bg_color="black",
            width=1000,
            height=500,
            border_color="white",
            corner_radius=30,                        
        )
        self.signup_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        self.create_user = tk.CTkEntry(master=self.signup_frame,
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
        self.create_user.place(relx=0.5, rely=0.3, relwidth=0.4, relheight=0.15, anchor="s")
       
        self.create_pass = tk.CTkEntry(master=self.signup_frame,
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
        self.create_pass.place(relx=0.5, rely=0.35, relwidth=0.4, relheight=0.15, anchor="n")
           
        self.create_pass = tk.CTkEntry(master=self.signup_frame,
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
        self.create_pass.place(relx=0.5, rely=0.35, relwidth=0.4, relheight=0.15, anchor="n")
         
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
      
 
#class for main page and tabs of the appilcation
class titan_main(tk.CTk):
    def __init__(self):
        super().__init__()
        self.title("new me")
        self.geometry("1000x700")
        self.resizable(True,True)
       
        self.gui_label_1 = tk.CTkLabel(master=self,
            bg_color="black",
            text="TITAN",
            text_color="white",
            font=(("comicsans",37)),
            width=100,
            height=60,
        )
        self.gui_label_1.place(relx=0.5, rely=0.065, relwidth=1.0, anchor="s")
        
        self.main_backround = tk.CTkImage(
        light_image=Image.open("image_files/wobbly_image.png"),
        dark_image=Image.open("image_files/wobbly_image.png"),
        size=(2000,1000)
        )
        
        self.image_label = tk.CTkLabel(master=self, 
            text="",
            width=650,
            height=650,
            image=self.main_backround,
        )
        self.image_label.place(relx=0.5, rely=0.5, relwidth=1.0, relheight=1.0, anchor="center")
        
        #tabview frame that holds the seprate tabs ans sections of my application allowing for easy navigation of the app gui
        self.large_frame = tk.CTkTabview(master=self,
            fg_color="black",
            #fg_color="#ff65f3",
            bg_color="black",
            width=100,
            height=100,
            border_color="white",
            corner_radius=30,
            segmented_button_fg_color="#343638",
            segmented_button_selected_color="black",
            segmented_button_unselected_hover_color="black",
            segmented_button_selected_hover_color="black",
            border_width=0.7
            #background_corner_colors=("black","black","black","black",)
            #background_corner_colors=("white","white","white","white",)
        )
        self.large_frame.place(rely=0.5, relx=0.5, relwidth=0.9, relheight=0.9, anchor="center")

   
        #weather tab elements
        self.weather_tab = self.large_frame.add("weather")
        
        #weather tab current day weather frame
        self.current_weather_frame = tk.CTkFrame(master=self.weather_tab,
            width=500,
            height=300,
            corner_radius=35,
            fg_color="#343638",
            bg_color="black"
        )
        self.current_weather_frame.place(relx=0.2, rely=0.3, anchor="s")

        self.weather_icon = tk.CTkLabel(master=self.current_weather_frame,
            width=100,
            height=100,
            fg_color="black",
            bg_color="#343638",
            text="",
            corner_radius=50  
        )
        self.weather_icon.place(relx=0.75, rely=0.58)
        
        #fits image processing elements
        self.fits_tab = self.large_frame.add("FITS PROCESSING")
        #test
        
        #calendar elements
        self.test_tab3 = self.large_frame.add("calendar")
        #test
        
        #diary elements
        self.test_tab4 = self.large_frame.add("Diary")
        #test
        
        #settings elements
        self.test_tab5 = self.large_frame.add("settings")
        #test
        
        
        
#runs app, by defining the class and running its contents

if __name__ == "__main__":
    app = titan_main()#titan_signup
    app.mainloop()

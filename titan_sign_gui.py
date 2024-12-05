import customtkinter as tk
from PIL import Image
import titan_main_gui

tk.set_appearance_mode("dark")
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
import titan_gui
import customtkinter as tk
from PIL import Image

#used customtkinter documentation to help with multiwindow development
#used to help with ctk classes: https://www.youtube.com/watch?v=GPcCLiOYVe4
tk.set_appearance_mode("dark")#"light"
#---------------------------------------------------------------------------#


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
        
        self.large_frame = tk.CTkTabview(master=self,
            fg_color="black",
            #fg_color="#ff65f3",
            bg_color="black",
            width=1000,
            height=500,
            border_color="white",
            corner_radius=0,
            segmented_button_fg_color="#343638",
            segmented_button_selected_color="#343638",
            segmented_button_unselected_hover_color="grey",
            segmented_button_selected_hover_color="#343638",
            border_width=0.5
            #background_corner_colors=("black","black","black","black",)
            #background_corner_colors=("white","white","white","white",)
        )
        self.large_frame.place(rely=0.5, relx=0.5, relwidth=0.9, relheight=0.9, anchor="center")

   
        #weather tab elements
        self.weather_tab = self.large_frame.add("weather")
        self.weather_test_btn = tk.CTkButton(master=self.weather_tab,
                text="hello world",
        )
        self.weather_test_btn.place(relx=0.5, rely=0.5, anchor="center")

        self.forgot_pass_button = tk.CTkButton(master=self.weather_tab, 
            text="forgot password",
            font=(("comicsans",20)),
            text_color="white",
            fg_color="#343638",
            #fg_color="#d622dc",
            hover_color="black",
            corner_radius=30,
            height=65,
            width=45,
            
        )
        self.forgot_pass_button.place(relx=0.5, rely=0.82, relwidth=0.97, anchor="n")
        
        #fits image processing elements
        self.test_tab2 = self.large_frame.add("FITS PROCESSING")
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
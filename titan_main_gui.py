import customtkinter as tk
from PIL import Image
from titan_moon_sun import get_sunset, m_img, m_txt, user_longitude, user_latitude
from titan_FITS import display_fits, display_folder, current_path
from titan_planets import planets, get_planets
from pytube import *
from datetime import date
import os 

#class for main page and tabs of the appilcation
class titan_main(tk.CTk):
    def __init__(self):
        
        super().__init__()
        self.title("TITAN")
        self.geometry("1500x900")#1000x700
        self.resizable(True,True
                       )#(True,True)
       
        self.gui_label_1 = tk.CTkLabel(master=self,
            bg_color="black",
            text="TITAN",
            text_color="white",
            font=(("Comic Sans",37)),
            width=100,
            height=60,
        )
        self.gui_label_1.place(relx=0.5, rely=0.065, relwidth=1.0, anchor="s")
        
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
        
        self.current_weather_frame = tk.CTkFrame(master=self.weather_tab,
            width=500,
            height=100,
            corner_radius=35,
            fg_color="#343638",
            bg_color="black",
        )
        self.current_weather_frame.place(relx=0.2, rely=0.2, anchor="s")
        
        self.weather_info = tk.CTkLabel(master=self.current_weather_frame,
            text="Current Weather: Not Calculated",
            font=(("Comic Sans",19)),
            width=90,
            height=80,
            bg_color="#343638",
            fg_color="#343638",
        )
        self.weather_info.place(relx=0.05, rely=0.5, anchor="w")
        
        self.telescope_img = "image_files/telescope.png"
        self.telescope_TF = tk.CTkImage(
            light_image=Image.open(self.telescope_img),
            dark_image=Image.open(self.telescope_img),
            size=(80,80)
        )
        
        self.telescope_icon = tk.CTkLabel(master=self.current_weather_frame,
            width=80,
            height=80,
            text="",
            image=self.telescope_TF,
            corner_radius=35,
            fg_color="#27962f",
            bg_color="#343638"
        )
        self.telescope_icon.place(relx=0.98, rely=0.5, anchor="e")
        
        
        self.moon_frame = tk.CTkFrame(master=self.weather_tab,
            width=500,
            height=150,
            corner_radius=35,
            fg_color="#343638",
            border_width=8,
            border_color="#343638"
        )
        self.moon_frame.place(relx=0.2, rely=0.45, anchor="s")
        
        #variable for changing moon phases
        
        self.moon_config = tk.CTkImage(
            light_image=Image.open(m_img),
            dark_image=Image.open(m_img),
            size=(130,130)
        )
        
        self.moon_label = tk.CTkLabel(master=self.moon_frame, 
            text="",
            width=50,
            height=100,
            image=self.moon_config,
            fg_color="black",
            corner_radius=30,
            bg_color="transparent"
            
        )
        self.moon_label.place(relx=0.02, rely=0.06 )
        
        self.moon_tf = tk.CTkLabel(master=self.moon_frame, 
            text="Not Visible",
            font=(("Comic Sans",20)),
            width=275,
            height=75,
            fg_color="#1a1b1c",
            corner_radius=25
        )
        self.moon_tf.place(relx=0.43, rely=0.06)
        
        self.moon_phase = tk.CTkLabel(master=self.moon_frame, 
            text=m_txt,
            font=(("Comic Sans",20)),
            width=275,
            height=50,
            fg_color="#1a1b1c",
            corner_radius=20,
        )
        self.moon_phase.place(relx=0.43, rely=0.6)
        
        
        #frame for the planet widgets, shwoing you what planets are visible on that current day
        #contains all of the planet tabs
        self.planet_vision = tk.CTkScrollableFrame(master=self.weather_tab,
            width=675,
            height=555,
            bg_color="black",
            fg_color="#343638",
            corner_radius=30,
            orientation="vertical",
            scrollbar_button_color="#242526",
            scrollbar_button_hover_color="#242526",
            scrollbar_fg_color="#343638",
            
        )
        self.planet_vision.place(relx=0.41, rely=0.52, anchor="w")
    
    #planet_vision elements
        
        #toggle for using gps to track location   
        self.toggle_var = tk.StringVar(value=False)
        self.location_toggle = tk.CTkSwitch(master=self.weather_tab,
            text="location",
            width= 90,
            height=90,
            switch_width=100,
            switch_height=45,
            corner_radius=40,
            progress_color="lightgreen",
            border_color="white",
            border_width=0.4,
            onvalue=True,
            offvalue=False,
            fg_color="#f04832",
            bg_color="black",
            font=(("Comic Sans",25)),
            command=self.planet_visible
            #command=self.location_check
        )
        self.location_toggle.place(relx=0.004, rely=0.89)
        
        #self.api_entry = tk.CTkEntry(comamnd=)
        
        #tab that will display the time that mercury will appera at night connection with skyfield
        #frame within a scrollable frame
        
        #for loop for all tabs in the scrollable tab planet vision frame
    
    # mercury elements-------------------------------------------
        self.mercury_tab = tk.CTkFrame(master=self.planet_vision,
            width=650,
            height=150,
            fg_color="#242526",
            bg_color="#343638",
            corner_radius=50,
            border_color="#242526",
            border_width=5
        )
        self.mercury_tab.grid(pady=10, row=1, column=0)
        
        self.mercury_img = "image_files\mercury.png"
        
        #configuration of the mercury image
        self.mercury_config = tk.CTkImage(
            light_image=Image.open(self.mercury_img),#sets light mode image to path
            dark_image=Image.open(self.mercury_img),#sets dark mode image to path
            size=(125,125)#size of image relative to frame its in
        )
        
        #label that contains the image for mercury
        self.mercury_label = tk.CTkLabel(master=self.mercury_tab, 
            text="",#empty as only image is present
            width=100,#width of label
            height=100,#height of label
            image=self.mercury_config,#image defined in mercury_config
            fg_color="#242526"#colour of the backround
        )
        #placement of the murcury label using .place and rely/relx
        self.mercury_label.place(relx=0.03, rely=0.095)
        
        self.mercury_text = tk.CTkLabel(master=self.mercury_tab, 
            text="MERCURY",
            font=(("Comic Sans",35)),
            width=100,
            height=100
        )
        self.mercury_text.place(relx=0.25, rely=0.15)
        
        self.mercury_tf = tk.CTkLabel(master=self.mercury_tab, 
            text="Not Visible",
            font=(("Comic Sans",30)),
            width=175,
            height=120,
            fg_color="#1a1b1c",
            corner_radius=35,
            anchor="w"
        )
        self.mercury_tf.place(relx=0.65, rely=0.1)
        
        
    #venus elements---------------------------------------------
        #tab that will contain the venus icon and text i have created
        self.venus_tab = tk.CTkFrame(master=self.planet_vision,
            width=650,#width of tab
            height=150,#height of tab
            fg_color="#242526",#forrground colour
            bg_color="#343638",#backround colour
            corner_radius=50,#corner rounding
            border_color="#242526",#colour of border
            border_width=5# width of border
        )
        #placement of the tab using "grid" and rows/columns
        self.venus_tab.grid(pady=10, row=2, column=0)
        
        self.venus_img = "image_files\\venus.png"
        self.venus_config = tk.CTkImage(
            light_image=Image.open(self.venus_img),
            dark_image=Image.open(self.venus_img),
            size=(125,125)
        )
        
        self.venus_label = tk.CTkLabel(master=self.venus_tab, 
            text="",
            width=100,
            height=100,
            image=self.venus_config,
            fg_color="#242526"
        )
        self.venus_label.place(relx=0.03, rely=0.095)
        
        self.venus_text = tk.CTkLabel(master=self.venus_tab, 
            text="VENUS",
            font=(("Comic Sans",35)),
            width=100,
            height=100
        )
        self.venus_text.place(relx=0.25, rely=0.15)
        
        self.venus_tf = tk.CTkLabel(master=self.venus_tab, 
            text="Not Visible",
            font=(("Comic Sans",30)),
            width=175,
            height=120,
            fg_color="#1a1b1c",
            corner_radius=35,
            anchor="center"
        )
        self.venus_tf.place(relx=0.65, rely=0.1)
        
    #mars elements------------------------------------------
        self.mars_tab = tk.CTkFrame(master=self.planet_vision,
            width=650,
            height=150,
            fg_color="#242526",
            bg_color="#343638",
            corner_radius=50,
            border_color="#242526",
            border_width=5
        )
        self.mars_tab.grid(pady=10, row=3, column=0)
        
        self.mars_img = "image_files\\mars.png"
        self.mars_config = tk.CTkImage(
            light_image=Image.open(self.mars_img),
            dark_image=Image.open(self.mars_img),
            size=(125,125)
        )
        
        self.mars_label = tk.CTkLabel(master=self.mars_tab, 
            text="",
            width=100,
            height=100,
            image=self.mars_config,
            fg_color="#242526"
        )
        self.mars_label.place(relx=0.03, rely=0.095)
        
        self.mars_text = tk.CTkLabel(master=self.mars_tab, 
            text="MARS",
            font=(("Comic Sans",35)),
            width=100,
            height=100
        )
        self.mars_text.place(relx=0.25, rely=0.15)
        
        self.mars_tf = tk.CTkLabel(master=self.mars_tab, 
            text="Visible",
            text_color="black",
            font=(("Comic Sans",30)),
            width=215,
            height=120,
            fg_color="green", #27962f
            corner_radius=35,
            anchor="center",
        )
        self.mars_tf.place(relx=0.65, rely=0.1)
        
    #jupiter elements-----------------------------------------
        self.jupiter_tab = tk.CTkFrame(master=self.planet_vision,
            width=650,
            height=150,
            fg_color="#242526",
            bg_color="#343638",
            corner_radius=50,
            border_color="#242526",
            border_width=5
        )
        self.jupiter_tab.grid(pady=10, row=4, column=0)
        
        self.jupiter_img = "image_files\\jupiter.png"
        self.jupiter_config = tk.CTkImage(
            light_image=Image.open(self.jupiter_img),
            dark_image=Image.open(self.jupiter_img),
            size=(125,125)
        )
        
        self.jupiter_label = tk.CTkLabel(master=self.jupiter_tab, 
            text="",
            width=100,
            height=100,
            image=self.jupiter_config,
            fg_color="#242526"
        )
        self.jupiter_label.place(relx=0.03, rely=0.095)
        
        self.jupiter_text = tk.CTkLabel(master=self.jupiter_tab, 
            text="JUPITER",
            font=(("Comic Sans",35)),
            width=100,
            height=100
        )
        self.jupiter_text.place(relx=0.25, rely=0.15)
        
        self.jupiter_tf = tk.CTkLabel(master=self.jupiter_tab, 
            text="Not Visible",
            font=(("Comic Sans",30)),
            width=175,
            height=120,
            fg_color="#1a1b1c",
            corner_radius=35,
            anchor="w"
        )
        self.jupiter_tf.place(relx=0.65, rely=0.1)
        
    #saturn elements------------------------------------------
        self.saturn_tab = tk.CTkFrame(master=self.planet_vision,
            width=650,
            height=150,
            fg_color="#242526",
            bg_color="#343638",
            corner_radius=50,
            border_color="#242526",
            border_width=5
        )
        self.saturn_tab.grid(pady=10, row=5, column=0)
        
        self.saturn_img = "image_files\\saturn.png"
        self.saturn_config = tk.CTkImage(
            light_image=Image.open(self.saturn_img),
            dark_image=Image.open(self.saturn_img),
            size=(125,125)
        )
        
        self.saturn_label = tk.CTkLabel(master=self.saturn_tab, 
            text="",
            width=100,
            height=100,
            image=self.saturn_config,
            fg_color="#242526"
        )
        self.saturn_label.place(relx=0.03, rely=0.095)
        
        self.saturn_text = tk.CTkLabel(master=self.saturn_tab, 
            text="SATURN",
            font=(("Comic Sans",35)),
            width=100,
            height=100
        )
        self.saturn_text.place(relx=0.25, rely=0.15)
        
        self.saturn_tf = tk.CTkLabel(master=self.saturn_tab, 
            text="Not Visible",
            font=(("Comic Sans",30)),
            width=175,
            height=120,
            fg_color="#1a1b1c",
            corner_radius=35,
            anchor="w"
        )
        self.saturn_tf.place(relx=0.65, rely=0.1)
        
    #uranus elements-----------------------------------------------
        self.uranus_tab = tk.CTkFrame(master=self.planet_vision,
            width=650,
            height=150,
            fg_color="#242526",
            bg_color="#343638",
            corner_radius=50,
            border_color="#242526",
            border_width=5
        )
        self.uranus_tab.grid(pady=10, row=6, column=0)
        
        self.uranus_img = "image_files\\uranus.png"
        self.uranus_config = tk.CTkImage(
            light_image=Image.open(self.uranus_img),
            dark_image=Image.open(self.uranus_img),
            size=(125,125)
        )
        
        self.uranus_label = tk.CTkLabel(master=self.uranus_tab, 
            text="",
            width=100,
            height=100,
            image=self.uranus_config,
            fg_color="#242526"
        )
        self.uranus_label.place(relx=0.03, rely=0.095)
        
        self.uranus_text = tk.CTkLabel(master=self.uranus_tab, 
            text="URANUS",
            font=(("Comic Sans",35)),
            width=100,
            height=100
        )
        self.uranus_text.place(relx=0.25, rely=0.15)
        
        self.uranus_tf = tk.CTkLabel(master=self.uranus_tab, 
            text="Not Visible",
            font=(("Comic Sans",30)),
            width=175,
            height=120,
            fg_color="#1a1b1c",
            corner_radius=35,
            anchor="w"
        )
        self.uranus_tf.place(relx=0.65, rely=0.1)
        
    #neptune elements----------------------------------------------
        self.neptune_tab = tk.CTkFrame(master=self.planet_vision,
            width=650,
            height=150,
            fg_color="#242526",
            bg_color="#343638",
            corner_radius=50,
            border_color="#242526",
            border_width=5
        )
        self.neptune_tab.grid(pady=10, row=7, column=0)
        
        self.neptune_img = "image_files\\neptune.png" 
        self.neptune_config = tk.CTkImage(
            light_image=Image.open(self.neptune_img),
            dark_image=Image.open(self.neptune_img),
            size=(125,125)
        )
        
        self.neptune_label = tk.CTkLabel(master=self.neptune_tab, 
            text="",
            width=100,
            height=100,
            image=self.neptune_config,
            fg_color="#242526"
        )
        self.neptune_label.place(relx=0.03, rely=0.095)
        
        self.neptune_text = tk.CTkLabel(master=self.neptune_tab, 
            text="NEPTUNE",
            font=(("Comic Sans",35)),
            width=100,
            height=100
        )
        self.neptune_text.place(relx=0.25, rely=0.15)

        self.neptune_tf = tk.CTkLabel(master=self.neptune_tab, 
            text="Not Visible",
            font=(("Comic Sans",30)),
            width=175,
            height=120,
            fg_color="#1a1b1c",
            corner_radius=35,
            anchor="w"
        )
        self.neptune_tf.place(relx=0.65, rely=0.1)


    #actual current weather tab for briefly shwoing weather condins, there are 4 widgets for it
    #weather conditons are temperature, cloud cover, wind speed, and humidity
        
        #setting location to calculated location from get loc
        set = get_sunset(user_longitude,user_latitude)
        print (set)#for testing
    
        #label wich displays the time of sunset on the current day
        self.sunset_label = tk.CTkLabel(master=self.weather_tab,
            text=("Sunset Today at  "+set),
            font=(("Comic Sans",25)),
            fg_color="#343638",
            text_color="white",
            width=220,
            height=80,
            corner_radius=30
        )
        self.sunset_label.place(relx=0.005, rely=0.47)
        
        
        #fits image processing elements
        self.fits_tab = self.large_frame.add("FITS PROCESSING")
        
        self.fits_display = tk.CTkLabel(master=self.fits_tab,
            width=635,
            height=635,
            fg_color="#343638",
            text="",
            corner_radius=35,
            image=""
        )
        self.fits_display.place(relx=0.01, rely=0.02)
        
        
        self.file_text = tk.CTkEntry(master=self.fits_tab,
            placeholder_text="Enter Filepath",
            placeholder_text_color="grey",
            width=275,
            height=50,
            fg_color="#343638",
            font=(("Comic Sans",25)),
            corner_radius=35
        )
        self.file_text.place(relx=0.78, rely=0.05)
        
        self.file_enter = tk.CTkButton(master=self.fits_tab,
            width=275,
            height=50,
            text="Enter",
            text_color="white",
            fg_color="#343638", 
            font=(("Comic Sans",25)),
            hover_color="black",
            corner_radius=35
        )
        self.file_enter.place(relx=0.78, rely=0.14)
        
        #dropdown menu that shows the files in the folder
        #using the passed in values in "values"
        self.file_dropdown = tk.CTkOptionMenu(master=self.fits_tab,
            width=300,#width of menu
            height=50,#height of menu
            dynamic_resizing=True,#resiazable for more files
            corner_radius=35,#corner rounding
            values=display_folder(current_path),#passes in the files 
            fg_color="#343638",#forgroubd colour
            button_color="#242526",#colour of button
            command=self.update_img#command to update the fits image
        )
        #placement of dropdown using place
        self.file_dropdown.place(relx=0.525, rely=0.05)
                
        self.edit_frame = tk.CTkFrame(master=self.fits_tab,
            width=600,
            height=420,
            corner_radius=35,
            fg_color="#343638"
        )
        self.edit_frame.place(relx=0.525, rely=0.35)
        
        edit_options = ["Blue","Green","red"]
        self.green_b = tk.CTkSegmentedButton(master=self.edit_frame,
            width=550,
            height=290,
            corner_radius=30,
            values=edit_options,
            selected_hover_color="#343638",
            selected_color="#343638",
            dynamic_resizing=True,
            font=(("Comic Sans",25))
        )
        self.green_b.place(relx=0.015, rely=0.02)

        self.save_b = tk.CTkButton(master=self.edit_frame,
            text = "Save",
            font=(("Comic Sans",25)),
            fg_color="#242526",
            bg_color="#2b2b2b",
            hover_color="black",
            width=225,
            height=100,
            corner_radius=30,
            command=self.save_text                                          
        )
        self.save_b.place(relx=0.015, rely=0.74)  
        
        self.open_b = tk.CTkButton(master=self.edit_frame,
            text = "Open",
            font=(("Comic Sans",25)),
            fg_color="#242526",
            hover_color="black",
            width=225,
            height=100,
            corner_radius=30,
            command=self.update_img                                         
        )
        self.open_b.place(relx=0.4, rely=0.74)
        
        self.exit_b = tk.CTkButton(master=self.edit_frame,
            text = "Exit",
            font=(("Comic Sans",25)),
            fg_color="#242526",
            hover_color="black",
            width=100,
            height=100,
            corner_radius=30                                            
        )
        self.exit_b.place(relx=0.8, rely=0.74)  
        
        #test
        
        
        #calendar elements
        self.test_tab3 = self.large_frame.add("calendar")
        #test
        
        #diary elements
        self.diary_tab = self.large_frame.add("Diary")
        
        self.text_frame = tk.CTkFrame(master=self.diary_tab,
            width =1225,
            height=600,
            corner_radius=35,
        )
        self.text_frame.place(relx=0.01, rely=0.05)
        
        #input for the diary feture, allows text to be entered
        self.diary_inp = tk.CTkTextbox(master=self.text_frame,
            width=630,#width of entry
            height=650,#height of entry 
            fg_color="#fbe982",#foreground colour
            corner_radius=30,#corner rounding
            text_color="black",#colour of text
            scrollbar_button_color="#d4c46c",#colour of scrollbar
            scrollbar_button_hover_color="#d4c46c",#hover colour
            wrap = "word"
            
        )
        self.diary_inp.place(relx=0.25, rely=0.02)
        
        #option menu to select the size of font for entry
        self.font_size = tk.CTkOptionMenu(master=self.text_frame,
            width=250,#width of menu
            height=40,#height of menu
            values=[str(i) for i in range(1,51)],#iteration for values
            fg_color="#343638",#forground colour
            corner_radius=35,#corner rounding
            command=self.update_font#function to update the dairy font 
        )
        self.font_size.place(relx=0.01, rely=0.03)
        
        self.font_label = tk.CTkLabel(master=self.text_frame,
            fg_color="#343638",
            text_color="white",
            width=40,
            height=40,
            text="Font size",
            font=(("Comic Sans",15))
        )
        self.font_label.place(relx=0.1, rely=0.03)
        
        #avaliable fonts that users can choose from outlined in a list
        #values for dropdown menu
        self.active_fonts = ["Arial", "Times New Roman", "Verdana", "Courier New", "Comic Sans"]
        
        #dropdown menu to select the font from preset options
        self.font_option = tk.CTkOptionMenu(master=self.text_frame,
            width=250,#width of menu
            height=40,#height if menu
            values=self.active_fonts,#values being passed in from list
            fg_color="#343638",#forground colour
            corner_radius=35,#corner rounding
            command=self.update_font#command to update the font in real
        )
        self.font_option.place(relx=0.01, rely=0.11)
        
        self.colour_options = ["black", "white", "blue", "red", "green", "purple"]
        self.text_colour = tk.CTkOptionMenu(master=self.text_frame,
            width=250,
            height=40,
            values=self.colour_options,
            fg_color="#343638",
            corner_radius=35,
            command=self.update_font
        )
        self.text_colour.place(relx=0.01, rely=0.19)
        
        self.colour_label = tk.CTkLabel(master=self.text_colour,
            fg_color="#343638",
            text_color="white",
            width=40,
            height=35,
            text="Text colour",
            font=(("Comic Sans",15))
        )
        self.colour_label.place(relx=0.1, rely=0.23)
        
        self.type_label = tk.CTkLabel(master=self.text_frame,
            fg_color="#343638",
            text_color="white",
            width=40,
            height=40,
            text="Font",
            font=(("Comic Sans",15))
        )
        self.type_label.place(relx=0.1, rely=0.11)
      
        self.page_colour_options = ["default", "white", "black", "darkgreen"]
        self.page_colour = tk.CTkOptionMenu(master=self.text_frame,
            width=250,
            height=40,
            values=self.page_colour_options,
            fg_color="#343638",
            corner_radius=35,
            command=self.update_font
        )
        self.page_colour.place(relx=0.01, rely=0.27)
        
        self.page_label = tk.CTkLabel(master=self.text_frame,
            fg_color="#343638",
            text_color="white",
            width=40,
            height=40,
            text="Page colour",
            font=(("Comic Sans",15))
        )
        self.page_label.place(relx=0.1, rely=0.27)
        
        self.save_dairy = tk.CTkButton(master=self.diary_tab,
            width=250,
            height=150,
            corner_radius=35,
            fg_color="#343638",
            text="Save as .txt",
            command=self.save_text,
            bg_color="#2b2b2b",
            font=(("Comic Sans",20))
        )
        self.save_dairy.place(relx=0.775, rely=0.7)
        
        self.file_frame = tk.CTkFrame(master=self.text_frame,
            width=250,
            height=150,
            corner_radius=35,
            fg_color="#343638"
        )
        self.file_frame.place(relx=0.78, rely=0.45)
        
        self.txt_entry = tk.CTkEntry(master=self.file_frame,
            width=225,
            height=75,
            corner_radius=35,
            placeholder_text="Enter file name",
            font=(("Comic Sans",20)),
            state="disabled"
        )
        self.txt_entry.place(relx=0.05, rely=0.08)
        
        self.text_button = tk.CTkButton(master=self.file_frame,
            width=225,
            height=50,
            text="Enter",
            fg_color="green",
            corner_radius=35,
            font=(("Comic Sans",20)),
            state="disabled",
            command=self.create_file
        )
        self.text_button.place(relx=0.05, rely=0.6)
        
        self.file_label = tk.CTkLabel(master=self.text_frame,
            width=250,
            text="",
            text_color="green", 
            height=75,
            font=(("Comic Sans",20)),
            bg_color="#2b2b2b",
            fg_color="#2b2b2b",
            corner_radius=35
        )
        self.file_label.place(relx=0.78, rely=0.32)
        #settings elements
        self.test_tab5 = self.large_frame.add("settings")
        
        self.open_diary = tk.CTkButton(master=self.diary_tab,
            width=250,
            height=75,
            corner_radius=35,
            fg_color="#343638",
            text="open .txt",
            bg_color="#2b2b2b",
            font=(("Comic Sans",20)),
            command=self.open_txt
        )
        self.open_diary.place(relx=0.775, rely=0.1)
        
        
        self.file_path = (r"C:\\Users\\leeca\\OneDrive\\Desktop\\courswork_code\\text_files")
        self.file_list = tk.CTkOptionMenu(master=self.text_frame,
            width=240,
            height=50,
            corner_radius=35,
            fg_color="#343638",
            bg_color="#2b2b2b",
            font=(("Comic Sans",20)),
            values=display_folder(self.file_path)
        )
        self.file_list.place(relx=0.785, rely=0.179)
        
        
    #funtion zone --------------------------------------------------------
    def planet_visible(self):
            self.venus_tf.configure(
                text="Visible",
                text_color="black",
                font=(("Comic Sans",30)),
                width=215,
                height=120,
                fg_color="green", #27962f
                corner_radius=35,
                anchor="center",
                )
            for planet in planets:
                if planet(0).alt > get_planets.min_altitude:
                    self.mercury_tf.configure(text="Visible",fg="green")
                elif planet(0).alt > get_planets.min_altitude:
                    self.venus_tf.configure(text="Visible",fg="green")

    
    
    def open_txt(self):
        selected_file = self.file_list.get()
        contents = (f"r","text_files\\{selected_file}")
    
        if contents in self.diary_inp:
           self.diary_inp.insert("0.0", "\n" + "Text already on page..(delete me)") 
        else:
            self.diary_inp.insert("1.0",contents)
          

    def create_file(self):
        txt_name = self.txt_entry.get() #gets text that will be used as file name
        text_inp = self.diary_inp.get(0.0, "end") #gets current text in diary entry
        #gets the current date using date from datetime lib
        current_day = date.today()
        #created the text file using the name given by user as well as the current date
        #to make indexing faster when looking for files
        with open(f"text_files\\{txt_name},{current_day}.txt", "w") as text_file:#opens/creates a text file with input passed into it
            text_file.write(text_inp)
            self.txt_entry.configure(state="disabled")
            self.text_button.configure(state="disabled")
            self.txt_entry.configure(placeholder_text="")
            self.file_label.configure(text="", fg_color="#2b2b2b")

    def save_text(self):
        self.txt_entry.configure(state="normal")
        self.text_button.configure(state="normal")
        self.file_label.configure(text="Input file name below", fg_color="#343638")
           
    #this fucntion update the font type and font size for the diary input 
    def update_font(self, _=None):
        current_size = int(self.font_size.get()) # current selected number
        current_font = (self.font_option.get())  # selected item from list
        current_colour = (self.text_colour.get())# selected colour from list
        current_page_colour = (self.page_colour.get())
        
        #configures the "font" to current_size, current font
        if current_page_colour == "default":
            self.diary_inp.configure(
            font=(current_font, 
            (current_size)), 
            text_color=current_colour,
            fg_color="#fbe982"#set default colour since this colour uses a colour code
                            #and is not built into custom tkinter
        )
        
        else:
            self.diary_inp.configure(
                font=(current_font, 
                (current_size)), 
                text_color=current_colour,
                fg_color=current_page_colour
        )
            
    def get_value (self,current_value):
        self.file_dropdown.get(current_value)
        return

    def update_img(self, selected_file):
        selected_file = self.file_dropdown.get()
        png_path = display_fits(current_path, selected_file)
        image = tk.CTkImage(file=png_path)
        self.fits_display.configure(image=image)
    #funtion that will eventually check if switch is on and turn
    #location tracking on/off
    '''
    def location_check(self):
        longitude = 0
        latitude = 0
        toggle = self.location_toggle.get()
        if toggle == True:
            longitude, latitude = pw.get_loc()
            print (longitude)
            print (latitude)
                
        elif toggle == False:
            print (longitude)
            print (latitude)
           
        self.api_entry = tk.CTkEntry(master=self.weather_tab,
           width=240,
           height=65,
           placeholder_text="Enter API",
           corner_radius=35,
           fg_color="#343638",  
           bg_color="black",
           font=(("Comic Sans",22))   
        )
        self.api_entry.place(relx=0.18, rely=0.90)
        
        '''
#runs app, by defining the class and running its contents

if __name__ == "__main__":
    app = titan_main()#titan_signup
    app.mainloop()



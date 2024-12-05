from astropy.io import fits 
import matplotlib.pyplot as pt 
import os


#shows the current or changing file path and passes it into current fits
current_path = "FITS_storage\\"

def check_path(current_path):
    #user input for path
    path_inp = input ("enter path please: ")
    file_path = ((current_path)+path_inp)
    #os library argument listdir checks length of directory
    check_path = os.listdir(file_path)
    file_num = len(check_path)
    if len(check_path) == 0:
        return("<folder is empty>") #will be devloped into an error message
    else:
        name_num = [current_path,file_num]
        return(name_num) #retuns the amount of files in the folder and path used
    
def display_folder(current_path):
    check_path = os.listdir(current_path)
    file_list = [] #list to hold files
    #iteration to pass each item in folder into list
    #for use in customtkinter
    for item in check_path:
        file_list.append(item)
    return (file_list)
   
def display_fits(current_path):
    #fit file thats selected in custom tkinter will
    #be passed into "file_inp"
    file_inp = input ("selected fits passed here: ")
     
    file_path = ((current_path)+file_inp)
    current_fit = fits.open(file_path)
    current_img = current_fit[0].data
    pt.figure
    pt.imshow(current_img, origin="lower")
    if os.path.exists(file_path+".png"):
        return (file_path+".png")
    else:
        pt.savefig(file_path+".png")
        return (file_path+".png")


#list = display_folder(current_path)
#check = check_path(current_path)

#shows the current fits file that is open
#current_fits = fits.open()

from astropy.io import fits 
import matplotlib.pyplot as pt 
import os

#shows the current or changing file path and passes it into current fits
current_path = "C:\\Users\\leeca\\OneDrive\\Desktop\\courswork_code\\FITS_storage\\"
'''
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
'''
   
def display_folder(current_path):
    return os.listdir(current_path)

#titan = titan_main()
#dropdown_val = titan.get_value

def display_fits(current_path, dropdown_val):
    file_path = os.path.join(current_path, dropdown_val)
    
    current_fit = fits.open(file_path)
    current_img = current_fit[0].data
    pt.color_sequences
    pt.figure
    pt.imshow(current_img, origin="lower")
    png_path = f"{file_path}.png"
   
    if os.path.exists(png_path):
        return png_path
    else:
        pt.savefig(png_path)
        return png_path



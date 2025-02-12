from titan_login_gui import titan_login
from titan_main_gui import titan_main
from titan_sign_gui import titan_signup

m = titan_main()#runs the main window for testing
l = titan_login()#runs the login window for testing
s = titan_signup()#runs the sign up window for testing

#initiates the application
if __name__ == "__main__":
    app = l# m, l, s
    app.main

    
def temp_converter():
    not_quit = True
    while not_quit:
        choice = input("C:celsius, F:farenhiet, X:quit: ")
        if choice.upper() == "C":
            num = int(input("enter celsius to convert to farehiet: "))
            new_num = ((num*1.8)+32)
            print(new_num)
        elif choice.upper() == "F":
            num = int(input("enter fareinhiegt to convert to celsius: "))
            new_num = ((num-32)/1.8)
            print(new_num)
        elif choice.upper() == "X":
            print("session ended")
            not_quit = False
        else:
            print("error unknown input")    
            
print (temp_converter())
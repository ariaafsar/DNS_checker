def start_menu():
    print("hello world!")
    while True :
        
        choice = input("choose you option please: \n 1.check system dns \n 2.check bypass 403 error")
        if choice == 1 or choice == "1" :
            check_os_dns()
        elif choice == 2 or choice == "2" :
            bypass_403()
        else:
            print("bad request")

def check_os_dns():
    pass

def bypass_403():
    pass
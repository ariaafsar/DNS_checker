import platform

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

def check_os():
    os_family = platform.system()
    return os_family

def check_os_dns(os_family):
    if os_family == "Linux":
        check_linux_dns()
    elif os_family == "Windows":
        check_windows_dns()
    else:
        print("operating system is not supported")

def check_windows_dns():
    pass

def check_linux_dns():
    pass

def bypass_403():
    pass
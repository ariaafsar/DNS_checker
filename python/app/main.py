from .os_dns_checker import Os_dns

class menu :
    def start_menu():
        print("Hello World!")
        print("#################################################")
        while True :
            print("choose you option please: \n 1.check system dns \n 2.set dns from list \n 3.check fastest dns")
            print("#################################################")
            choice = input()
            print("#################################################")
            if choice == 1 or choice == "1" :
                Os_dns.check_os()
            elif choice == 2 or choice == "2" :
                pass
            elif choice == 3 or choice == "3" :
                pass
            else:
                print("bad request")

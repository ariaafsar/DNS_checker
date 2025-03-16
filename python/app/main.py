from os_dns_checker import Os_dns

class menu :
    def start_menu():
        print("Hello World!")
        while True :
            print("#################################################")
            print("choose you option please: \n 1.check system dns \n 2.set dns from list \n 3.check fastest dns \n 4.exit")
            print("#################################################")
            choice = input()
            print("#################################################")
            if choice == 1 or choice == "1" :
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                Os_dns.check_os()
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            elif choice == 2 or choice == "2" :
                pass
            elif choice == 3 or choice == "3" :
                pass
            elif choice == 4 or choice == "4" :
                break
            else:
                print("bad request")

    def main() :
        menu.start_menu()
if __name__ == "__main__" :
    menu.start_menu()
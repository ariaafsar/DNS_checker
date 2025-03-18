from os_dns_checker import Os_dns
from dns_seter import Seter
import sys
class menu :
    def start_menu():
        print("Hello World!")
        while True :
            print("#################################################")
            print("choose you option please: \n 1.check system dns \n 2.set dns \n 3.check fastest dns \n 4.exit")
            print("#################################################")
            choice = input()
            print("#################################################")
            if choice == 1 or choice == "1" :
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                Os_dns.check_os()
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            elif choice == 2 or choice == "2" :
                while True :
                    print("#################################################")
                    print("choose you option please: \n 1.entering you own dns nameserver \n 2.choose from dns list \n 3.back")
                    print("#################################################")
                    choice1 = input()
                    print("#################################################")
                    if choice1 == "1" or choice1 == 1 :
                        print("enter your dns ip")
                        dns_ip = input()
                        if not Seter.dns_validator(dns_ip) :
                            print("invalid dns ip")
                            sys.exit(1)
                        else :
                            Seter.set_dns(dns_ip)
                    elif choice1 == "2" or choice == 2 :
                        pass
                    elif choice1 == "3" or choice == 3 :
                        break
            elif choice == 3 or choice == "3" :
                pass
            elif choice == 4 or choice == "4" :
                break
            else:
                print("bad request")
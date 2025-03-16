import os
import subprocess
import time
import platform

class Seter:
    def os_detector():
        operating_system = platform.system()
        if operating_system == "Linux" :
            pass
        elif operating_system == "Windows" :
            pass
        else :
            return "operating system is not supported"
        
    def linux_seter():
        print("enter your dns ip:\n")
        dns_nameserver = input()
        dns_file = "/etc/resolv.conf"
        


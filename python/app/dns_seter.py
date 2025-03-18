import os
import subprocess
import time
import platform
import sys
class Seter:
    def os_detector():
        operating_system = platform.system()
        if operating_system == "Linux" :
            pass
        elif operating_system == "Windows" :
            pass
        else :
            return "operating system is not supported"
        
    def dns_validator(dns_ip) :
        ip_parts = dns_ip.strip().split(".")
        if len(ip_parts) != 4 :
            return False
        for ip in ip_parts :
            if not ip.isdigit() :
                return False
            num = int(ip)
            if num < 0 or num > 255 :
                return False
        return True 
    
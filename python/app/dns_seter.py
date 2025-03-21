import os
import platform
import sys
from importlib import util
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
    def set_dns(dns_ip) :
        dns_file_path = '/etc/resolv.conf'
        backup_file_path = '/etc/resolv.conf.bak'

        if not os.access(dns_file_path , os.W_OK) :
            print("Error: No write permission for " + dns_file_path + ". Run as root")
            sys.exit(1)
        
        if os.path.exists(dns_file_path) :
            file_in = open(dns_file_path , "r")
            orginal_content = file_in.read()
            file_in.close()
            backup = open(backup_file_path , "w")
            backup.write(orginal_content)
            backup.close()
            print("backup created at " + backup_file_path)
        else :
            print(dns_file_path + " not found")
            sys.exit(1)
        
        file_out = open(dns_file_path , "w")
        file_out.write("nameserver " + dns_ip + "\n")
        file_out.close()
        print("dns set to " + dns_ip + " successfully")

    def read_dns_list_file(file) :
        if not os.path.isfile(file) :
            print(f"Error: {file} not found")
            sys.exit(1)
        
        spec = util.spec_from_file_location("dns_list" , file)
        dns_list_module = util.module_from_spec(spec)
        spec.loader.exec_module(dns_list_module)

        if not hasattr(dns_list_module , "dns_list") :
            print(f"Error: dns_list not found in {file}")
            sys.exit(1)
        
        return dns_list_module.dns_list
    
    def show_dns_options(dns_list) :
        print("Avable DNS Servers:")
        for idx , dns in enumerate(dns_list , start=1) :
            print(f"{idx}. {dns}")

        choice = input(f"Select a DNS server (1-{len(dns_list)}): ").strip()
        if not choice.isdigit() or not (1 <= int(choice) <= len(dns_list)) :
            print("Invalid choice. Please select a valid option.")
            sys.exit(1)

        return dns_list[int(choice) - 1]



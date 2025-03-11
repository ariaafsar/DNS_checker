import platform
import subprocess

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
    result = subprocess.run(["nmcli" , "dev" , "show"] , capture_output=True , text=True)
    dns_servers = []
    for line in result.stdout.splitlines() :
        if "DNS" in line :
            parts = line.split(":" , 1)
            if len(parts) > 1:
                dns_servers.append(parts[1].split())

    if dns_servers :
        return dns_servers
    
    else :
        return "no DNS nameserver is set"
    
def bypass_403():
    pass
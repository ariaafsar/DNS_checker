import platform
import subprocess

def start_menu():
    print("#################################################")
    print("hello world!")

    while True :
        print("#################################################")
        print("choose you option please: \n 1.check system dns \n 2.check bypass 403 error")
        choice = input()
        print("#################################################")
        if choice == 1 or choice == "1" :
            print(check_os_dns())
            break
#        elif choice == 2 or choice == "2" :
#            bypass_403()
        else:
            print("bad request")

def check_os_dns() :
    os_family = platform.system()
    if os_family == "Linux" :
        print(check_linux_dns())
    elif os_family == "Windows" :
        print(check_windows_dns())
    else :
        print("operating system is not supported")
        print("#################################################")
def check_windows_dns() :
    dns_servers = []
    result = subprocess.run(["ipconfig" , "/all"] , capture_output = True , text = True , check = True)
    capture = False
    for line in result.stdout.splitlines() :
        if "DNS SEVERS" in line :
            capture = True
            dns_servers.append(line.split(':' , 1)[1].strip())
        elif capture and line.strip() :
            dns_servers.append(line.strip())
        elif capture and not line.split() :
            break
    if dns_servers :
        return dns_servers
    else :
        return "no DNS nameserver is set"
    
def check_linux_dns() :
    result = subprocess.run(["nmcli" , "dev" , "show"] , capture_output = True , text = True)
    dns_servers = []
    file = open("/etc/resolv.conf" , "r")
    lines = file.readlines()
    file.close()
    for line in lines :
        if line.startswith("nameserver") :
            dns_servers.append(line.split()[1])
    for line in result.stdout.splitlines() :
        if "DNS" in line :
            parts = line.split(":" , 1)
            if len(parts) > 1 and parts[1].strip() :
                dns_servers.extend(parts[1].split())
    
    if dns_servers :
        for index , server in enumerate(dns_servers) :
            if server != "192.168.0.125" :
                print(server)
    
    else :
        return "no DNS nameserver is set"

#def bypass_403():
#    pass

start_menu()
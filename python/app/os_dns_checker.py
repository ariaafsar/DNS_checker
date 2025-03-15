import platform
import subprocess

class Os_dns :

    def check_os() :
        os = platform.system()

    def linux_dns_checker() :
        dns_servers = []
        result = subprocess.run(["nmcli" , "dev" , "show"] , capture_output=True , text=True)
        for line in result.stdout.splitlines() :
            if "DNS" in line :
                parts = line.split(":" , 1)
                if len(parts) > 1 and parts[1].split() :
                    dns_servers.extend(parts[1].split())
        return dns_servers
    
    def linux_dns_file_checker():
        dns_file_servers = []
        file = open("/etc/resolv.conf" , "r")
        lines = file.readline()
        file.close

        for line in lines :
            if line.startswith("nameserver") :
                dns_file_servers.append(line.split()[1])
        return dns_file_servers
    
    def windows_dns_checker() :
        dns_servers = []
        result = subprocess.run(["ipconfig" , "/all"] , capture_output=True , text=True)
        capture = False
        for line in result.stdout.splitlines() :
            if "DNS SERVER" in line :
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
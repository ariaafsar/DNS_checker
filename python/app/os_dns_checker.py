import platform
import subprocess

class Os_dns :

    def check_os() :
        os = platform.system()
        if os == "Linux" :
            Os_dns.linux_dns_checker()
        elif os == "Windows" :
            Os_dns.windows_dns_checker()
        else :
            print("sorry but operating system is not supported")

    def linux_dns_checker() :
        dns_server = []
        dns_servers = Os_dns.linux_subproccess_dns_checker()
        for line in dns_servers.splitlines() :
            if line == "127.0.0.53" :
                continue
            else :
                dns_server.append(line.split()[1])    
            return dns_server
    def linux_subproccess_dns_checker() :
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
    
    def linux_dns_checker_result_cominer() :
        dns_server_list_1 = Os_dns.linux_dns_checker()
        dns_server_list_2 = Os_dns.linux_dns_file_checker()
        dns_servers = list(set(dns_server_list_1 + dns_server_list_2))
        return dns_servers()


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
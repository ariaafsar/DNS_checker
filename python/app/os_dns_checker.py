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
        
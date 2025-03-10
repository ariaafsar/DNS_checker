#!/bin/bash

dns_file="${1:=dns_list.txt}"
best_dns=""
best_time=10000

while IFS= read -r dns; do
    # Skip empty lines or lines starting with '#' (comments)
    if [[ -z "$dns" || "$dns" =~ ^# ]]; then
      continue
    fi

    echo "checking DNS Server : $dns"
    ping_out=$(ping -c 3 -w 5 "$dns" 2>&1)

    if [ $? -ne 0 ]; then
	echo "  DNS $dns is unreachable."
	continue
    fi

    avg_time=$(echo "$ping_output" | tail -1 | awk -F '/' '{print $5}')
    
    echo "best DNS server is: $best_dns with an average ping of ${best_time}ms"
    read -p "Do you want to apply this DNS server? (y/n)" answer
    if [[ "$answer" =~ ^[Yy]$ ]]; then 
	echo "applying $best_dns "
	sudo bash -c "echo '$best' > /etc/resolv.conf"
    else 
	echo "DNS configuration not applied."
    fi

#!/bin/bash

# Set the test URL to Epic Games (hardcoded)
test_url="https://www.epicgames.com"

# Extract protocol, hostname, and port from the test URL
proto=$(echo "$test_url" | awk -F:// '{print $1}')
rest=$(echo "$test_url" | awk -F:// '{print $2}')
hostport=$(echo "$rest" | cut -d'/' -f1)
host=$(echo "$hostport" | cut -d':' -f1)
port=$(echo "$hostport" | cut -d':' -f2)
if [ -z "$port" ]; then
    if [ "$proto" == "http" ]; then 
        port=80
    elif [ "$proto" == "https" ]; then 
        port=443
    else
        port=80
    fi
fi

echo "Using test URL: $test_url"
echo "Extracted host: $host, port: $port"

# Use the first argument as the DNS file; if not provided, default to dns_list.txt
dns_file="${1:-dns_list.txt}"
if [[ ! -f "$dns_file" ]]; then
    echo "DNS file '$dns_file' not found!"
    exit 1
fi

best_dns=""
best_time=10000

# Loop over each DNS server in the list file
while IFS= read -r line; do
    # Skip empty lines or lines starting with '#' (comments)
    if [[ -z "$line" || "$line" =~ ^# ]]; then
        continue
    fi

    # Extract the DNS IP from a line formatted like "nameserver 8.8.8.8"
    dns=$(echo "$line" | awk '{print $NF}')
    if [ -z "$dns" ]; then
        continue
    fi

    echo "-------------------------------------"
    echo "Testing DNS server: $dns"
    
    # Resolve the hostname using this DNS server via dig
    resolved_ip=$(dig @"$dns" "$host" +short | head -n1)
    if [ -z "$resolved_ip" ]; then
        echo "  Failed to resolve $host using DNS $dns"
        continue
    fi

    echo "  Resolved IP: $resolved_ip"
    
    # Use curl with --resolve to force connection to the resolved IP and get HTTP status
    http_status=$(curl -s -o /dev/null -w "%{http_code}" --resolve "$host:$port:$resolved_ip" "$test_url")
    echo "  HTTP status from $test_url: $http_status"
    if [ "$http_status" == "403" ]; then
        echo "  DNS $dns did not bypass the 403 error."
        continue
    fi

    # DNS bypassed the 403 error, so now test its response time via ping
    ping_output=$(ping -c 3 -w 5 "$resolved_ip" 2>&1)
    if [ $? -ne 0 ]; then
        echo "  Ping to $resolved_ip failed."
        continue
    fi

    # Extract the average ping time from the summary (e.g., "rtt min/avg/max/mdev = 1.500/1.600/1.700/0.100 ms")
    avg_time=$(echo "$ping_output" | tail -1 | awk -F'/' '{print $5}')
    if ! [[ "$avg_time" =~ ^[0-9.]+$ ]]; then
        echo "  Could not parse ping time for $resolved_ip"
        continue
    fi

    echo "  Average ping for DNS $dns ($resolved_ip): $avg_time ms"

    # If this DNS has a lower average ping than the best found so far, update best_dns and best_time
    if (( $(echo "$avg_time < $best_time" | bc -l) )); then
        best_time=$avg_time
        best_dns=$dns
    fi

done < "$dns_file"

echo "-------------------------------------"
# After processing all DNS servers, check if any were found that bypassed the 403 error
if [[ -n "$best_dns" ]]; then
    echo "Best DNS server that bypasses the 403 error is: $best_dns with an average ping of ${best_time} ms"
    read -p "Do you want to apply this DNS server? (y/n): " answer
    if [[ "$answer" =~ ^[Yy]$ ]]; then 
        echo "Applying DNS server $best_dns to /etc/resolv.conf..."
        sudo bash -c "echo 'nameserver $best_dns' > /etc/resolv.conf"
    else
        echo "DNS configuration not applied."
    fi
else
    echo "No DNS server in the list bypassed the 403 error."
fi


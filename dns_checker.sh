#!/bin/bash

# Use the first argument as the DNS file; if not provided, default to dns_list.txt
dns_file="${1:-dns_list.txt}"

# Check if the file exists
if [[ ! -f "$dns_file" ]]; then
    echo "DNS file '$dns_file' not found!"
    exit 1
fi

best_dns=""
best_time=10000

# Read each line from the file
while IFS= read -r line; do
    # Skip empty lines or comment lines
    if [[ -z "$line" || "$line" =~ ^# ]]; then
        continue
    fi

    # Extract the DNS IP address; assuming the line is like: "nameserver 8.8.8.8"
    dns=$(echo "$line" | awk '{print $NF}')
    if [[ -z "$dns" ]]; then
        continue
    fi

    echo "Checking DNS server: $dns"
    ping_output=$(ping -c 3 -w 5 "$dns" 2>&1)

    if [ $? -ne 0 ]; then
        echo "  DNS $dns is unreachable."
        continue
    fi

    # Extract the average ping time from the ping summary.
    # The output usually has a line like:
    # "rtt min/avg/max/mdev = 1.500/1.600/1.700/0.100 ms"
    avg_time=$(echo "$ping_output" | tail -1 | awk -F'/' '{print $5}')
    
    # Check that avg_time is a valid number
    if ! [[ "$avg_time" =~ ^[0-9.]+$ ]]; then
        echo "  Failed to parse average ping for $dns."
        continue
    fi

    echo "  Average ping for $dns: ${avg_time}ms"

    # Compare the current average with the best time found so far
    if (( $(echo "$avg_time < $best_time" | bc -l) )); then
        best_time=$avg_time
        best_dns=$dns
    fi
done < "$dns_file"

# After processing all DNS servers, ask the user if they want to apply the best one.
if [[ -n "$best_dns" ]]; then
    echo "Best DNS server is: $best_dns with an average ping of ${best_time}ms"
    read -p "Do you want to apply this DNS server? (y/n): " answer
    if [[ "$answer" =~ ^[Yy]$ ]]; then 
        echo "Applying $best_dns to /etc/resolv.conf..."
        sudo bash -c "echo 'nameserver $best_dns' > /etc/resolv.conf"
    else 
        echo "DNS configuration not applied."
    fi
else
    echo "No reachable DNS servers found."
fi


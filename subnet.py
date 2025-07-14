import ipaddress

def calculate_network(cidr_input):
    try:
        interface = ipaddress.ip_interface(cidr_input)
        network = interface.network
        # Calculate subnet mask
        subnet_mask = network.netmask
        # Calculate number of usable hosts
        num_hosts = network.num_addresses - 2 if network.num_addresses > 2 else 0
        # Calculate default gateway (first usable IP)
        default_gateway = list(network.hosts())[0] if num_hosts > 0 else None
        # Display results
        print(f"IP: {interface.ip}")
        print(f"Subnet mask: {subnet_mask}")
        print(f"Hosts number: {num_hosts}")
        print(f"GW: {default_gateway}")

    except ValueError as e:
        print(f"Erorr: {e}")

if __name__ == "__main__":
    subnet = input("IP address in CIDR format: ")
    calculate_network(subnet)
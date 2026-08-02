# Create a network access configuration map
firewall = {
    "HTTP": 80,
    "HTTPS": 443,
    "SSH": 22,
    "PostgreSQL": 5432,
    "info" : {
    "name" : "Bakshi",
    "marks" : 87,
    "cgpa" : 9.1      
    }
}
ssh_port = firewall["SSH"] 

# 2. Production Standard Lookup: The .get() method
# This prevents code crashes. If the protocol isn't found, it returns your default string.
active_port = firewall.get("MySQL", "PORT_NOT_CONFIGURED")
print(f"The port for MYSQL is : ")
print(f"[SYSTEM] Secure SSH port allocation: {ssh_port}")
# print(firewall["HTTP"]) this can cause error if we print the wrong name
# print(firewall.get("HTTP")) no error simply return none if we enter the wrong value
print(list(firewall["info"]))

#sets 
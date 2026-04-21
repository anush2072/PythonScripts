import socket

def print_hostname():
    hostname = socket.gethostname()
    print("Hostname:", hostname)

# Call the function to print the hostname
print_hostname()

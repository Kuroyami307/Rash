import socket

HOST = "127.0.0.1"
PORT = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    while True:
        inp = input("$ ")

        if "start" in inp.strip().lower():
            args = inp.split(" ")

            if len(args) == 1:
                print("Invalid Arguments.\nInclude the ip and port number.\n")
            
            elif len(args) == 2:
                print("Invalid Arguments.\nInclude the port number.\n")
            
            elif len(args) > 3:
                print("Invalid Arguments.\nCan only have ip address and port number.\n")
            
            
            host_address = args[1]
            port_address = int(args[2])
        
            s.connect((host_address, port_address))
            break

        else:
            print("Wrong Command.\nPlease type 'start' followed the ip and port number.\n")

        
    s.sendall(b"start_terminal")
    response = s.recv(1024)
    response_str = response.decode('utf-8')

    if "config" in response_str:
        response_args = response_str.split("|")
        server_name = response_args[1]
        path = response_args[2]


    while True:
        display_name = f"\033[31m{server_name}:\033[0m\033[36m~{path}\033[0m$ "
        command = input(display_name)

        s.sendall(b"{command}")
    
    
    


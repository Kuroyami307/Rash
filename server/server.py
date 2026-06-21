import subprocess
import os
import psutil

shell_executable = "/bin/bash"

home_dir = os.path.expanduser("~")

terminal = subprocess.Popen(
    [shell_executable],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
    bufsize=1,
    cwd = home_dir,
)

terminal_pid = psutil.Process(terminal.pid)
server_name = "utsav_307"

while True:

    path = terminal_pid.cwd()

    display_name = f"\033[31m{server_name}:\033[0m\033[36m~{path}\033[0m$ "
    command = input(display_name)

    if command.lower().strip() == "exit":
        print("...Exiting Terminal...\n")
        break

    # if "upload" in command:

    # if "download" in command:
    
    # fname = command.split(" ")[1]

    # print(fname)

    marker = "cmd_end"
    terminal.stdin.write(f"{command}\n echo {marker}\n")
    terminal.stdin.flush()

    output = []
    while True:
        line = terminal.stdout.readline()
        if marker in line:
            break
        
        output.append(line)

    print("".join(output).strip())

    # send this result = "".join(output).strip() from the server to the client after running the program
    # we should also send the path from the server to the client so 
    # the structure will be like: 
    # path | output    so split on the basis of | will be a good idea ig
    # after initial connection setup however we should send the name of the server to the client
    # so after client starts a connection with the server then the server sends its username and the default path to the client
    # so its like after connection estalishment only the Popen will run and then we will send the reqd info back to the client and close the connection
    # after that client will send the command and server will run it and send the path and output back.

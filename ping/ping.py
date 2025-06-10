import socket
import time

def ping(host, port=53, timeout=3):

    try:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        start = time.time()
        sock.connect((host, port))
        end = time.time()

        sock.close()
        
        time_ms = (end - start) * 1000
        
        return True,time_ms
        
    except socket.timeout:
        return False,None
    
    except Exception as e:
        return False,None
    

ip = input("enter ip(default: 8.8.8.8): ")
if ip == "":
    ip = "8.8.8.8"

fail_count = 0

for i in range(10):
    success, time_ms = ping(ip)
    time.sleep(1)
    
    if success:
        if time_ms < 100:
            print(f"🟢connected to {ip} in {time_ms:.1f} ms")
        else:
            print(f"🟡connected to {ip} in {time_ms:.1f} ms")

    else:
        fail_count +=1
        print(f"🔴can't connect to {ip}")


print(f"packet loss: {fail_count * 10}%")



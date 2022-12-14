from utils import *
from concurrent.futures import ProcessPoolExecutor

file_name = menu()
ip_address = "udp://127.0.0.1:23000"

# open_livestream(ip_address) don't work because I wasn't able to prompt the command in another terminal
live_stream(file_name, ip_address)


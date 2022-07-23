import psutil
import time

def dispalyUsage(cpu_usage, mem_usage, bars = 50):
    cpu_percent = (cpu_usage)
    cpu_bar = '█' * int((cpu_percent / 100.0) * bars) + '-' * int(bars - int((cpu_percent/100.0) * bars))
    mem_percent = (mem_usage)
    mem_bar = '█' * int((mem_percent / 100.0) * bars) + '-' * int(bars - int((mem_percent/100.0) * bars))

    print(f"\rCPU Usage: |{cpu_bar}| {cpu_percent}%  ", end="")
    print(f"MEM Usage: |{mem_bar}| {mem_percent}%  ", end = "\r")


while True:
    dispalyUsage(psutil.cpu_percent(), psutil.virtual_memory().percent, 30)
    time.sleep(1)
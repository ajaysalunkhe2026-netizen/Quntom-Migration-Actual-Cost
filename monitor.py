import psutil

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

print("=== System Monitoring ===")
print(f"CPU Usage: {cpu}%")
print(f"RAM Usage: {memory}%")
print(f"Disk Usage: {disk}%")

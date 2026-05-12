import random

cpu_load = random.randint(10, 100)

print("=== Optimization Engine ===")
print(f"Current CPU Load: {cpu_load}%")

if cpu_load > 70:
    print("High load detected")
    print("Suggested Action: Migrate workload")
else:
    print("System Stable")
    print("No migration needed")
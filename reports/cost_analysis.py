migration_cost = 120
optimized_cost = 85

cost_reduction = migration_cost - optimized_cost
reduction_percent = (cost_reduction / migration_cost) * 100

print("=== Cost Analysis Report ===")
print(f"Initial Cost: ${migration_cost}")
print(f"Optimized Cost: ${optimized_cost}")
print(f"Cost Reduced: ${cost_reduction}")
print(f"Reduction Percentage: {reduction_percent:.2f}%")
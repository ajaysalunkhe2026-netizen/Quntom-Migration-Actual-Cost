import shutil
import time
import os

source_folder = "dummy_files"
destination_folder = "database"

start_time = time.time()

files = os.listdir(source_folder)

for file in files:
    source_path = os.path.join(source_folder, file)
    destination_path = os.path.join(destination_folder, file)

    shutil.copy(source_path, destination_path)

end_time = time.time()

migration_time = end_time - start_time

print("=== Migration Complete ===")
print(f"Total Files Migrated: {len(files)}")
print(f"Migration Time: {migration_time:.2f} seconds")
log_file = open("logs/migration_log.txt", "w")

log_file.write(f"Total Files Migrated: {len(files)}\n")
log_file.write(f"Migration Time: {migration_time:.2f} seconds\n")

log_file.close()
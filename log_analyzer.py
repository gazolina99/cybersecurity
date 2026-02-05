# Simple log analyzer for failed login attempts
# Tested on Linux systems using /var/log/auth.log


from collections import Counter


log_file = "/var/log/auth.log"



failed_ips = []


with open(log_file, "r") as f:
for line in f:
if "Failed password" in line:
failed_ips.append(line.split()[0])


for ip, count in Counter(failed_ips).items():
if count > 5:
print(f"Possible brute force from {ip}: {count} attempts")
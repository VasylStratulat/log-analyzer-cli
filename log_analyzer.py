import argparse
parser = argparse.ArgumentParser()
parser.add_argument("logfile")
parser.add_argument(
    "--level",
    choices=["INFO", "WARNING", "ERROR"],
    default="ERROR"
)
args = parser.parse_args()
filter_level = args.level

warning_count = 0
info_count = 0
error_count = 0
total_lines = 0
error_messages = {}
ip_addresses = {}
filtered_logs = []


with open(args.logfile, "r") as file:
    for line in file:
        total_lines += 1
        if  filter_level in line:
            filtered_logs.append(line.strip())
        if "INFO" in line:
            info_count += 1

        if "WARNING" in line:
            warning_count += 1

        if "ERROR" in line:
            error_count += 1
            error_message = line.split("ERROR", 1)[1].strip()
            if "IP=" in error_message:
                error_message = error_message.split("IP=", 1)[0].strip()
            if error_message in error_messages:
               error_messages[error_message] += 1
            else:
               error_messages[error_message] = 1
        if "IP=" in line:
            ip_address = line.split("IP=", 1)[1].strip()
            if ip_address in ip_addresses:
                ip_addresses[ip_address] +=1
            else:
                ip_addresses[ip_address] = 1


print("Log Analysis Report")
print("-------------------")
print("Total lines:",total_lines)
print("INFO:", info_count)
print("WARNING:", warning_count)
print("ERROR:", error_count)

print("Error details")
print("-------------")
for error, count in error_messages.items():
    print(f"{error}: {count}")

print("")
print("IP statistics")
print("-------------")
print("Unique IP addresses:", len(ip_addresses))
for ip, count in ip_addresses.items():
    print(f"{ip}: {count}")

print("")
print(f"Filtered logs ({filter_level})")
print("-------------------")
for log in filtered_logs:
    print(log)

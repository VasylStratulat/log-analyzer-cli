warning_count = 0
info_count = 0
error_count = 0
total_lines = 0
error_messages = {}

with open("sample.log", "r") as file:
    for line in file:
        total_lines += 1

        if "INFO" in line:
            info_count += 1

        if "WARNING" in line:
            warning_count += 1

        if "ERROR" in line:
            error_count += 1
            error_message = line.split("ERROR", 1)[1].strip()
            if error_message in error_messages:
               error_messages[error_message] += 1
            else:
               error_messages[error_message] = 1

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

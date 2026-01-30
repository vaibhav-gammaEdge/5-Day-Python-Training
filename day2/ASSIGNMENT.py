import logging

sample_logs = [
    {
        "timestamp": "2026-01-30 09:00:01",
        "log_level": "INFO",
        "message": "User logged in",
        "user_id": 101
    },
    {
        "timestamp": "2026-01-30 09:01:12",
        "log_level": "DEBUG",
        "message": "Fetching user profile from database",
        "user_id": 101
    },
    {
        "timestamp": "2026-01-30 09:02:05",
        "log_level": "WARNING",
        "message": "Password attempt failed",
        "user_id": 102
    },
    {
        "timestamp": "2026-01-30 09:02:30",
        "log_level": "INFO",
        "message": "User logged in",
        "user_id": 102
    },
    {
        "timestamp": "2026-01-30 09:05:44",
        "log_level": "ERROR",
        "message": "Database connection timeout",
        "user_id": None
    },
    {
        "timestamp": "2026-01-30 09:06:10",
        "log_level": "INFO",
        "message": "User logged out",
        "user_id": 101
    },
    {
        "timestamp": "2026-01-30 09:07:55",
        "log_level": "CRITICAL",
        "message": "Payment service unavailable",
        "user_id": 103
    }
]
error_logs = [log for log in sample_logs if log["log_level"] == "ERROR"]
warning_logs = [log for log in sample_logs if log["log_level"] == "WARNING"]
info_logs = [log for log in sample_logs if log["log_level"] == "INFO"]
print(error_logs)
dict ={}
ls=[i['log_level'] for i in sample_logs]
# for i in sample_logs:
#      ls.append(i["log_level"])

for i in ls:
     if i in dict:
          dict[i]+=1
     else:
          dict[i]=1

print(dict)
freq={ }
for log in sample_logs:
     user=log['user_id']

     freq[user]=freq.get(user,0)+1
     
print (freq)  
active_user=None 
m=max(freq.values())
for i,j in freq.items():
    if j==m:
        active_user=i
        break

print(active_user)


from datetime import datetime

errors_by_hour = {}

for log in sample_logs:
    if log["log_level"] == "ERROR":
        dt = datetime.strptime(log["timestamp"], "%Y-%m-%d %H:%M:%S")
        hour = dt.hour
        errors_by_hour[hour]=freq.get(hour,0)+1

for hour, count in sorted(errors_by_hour.items()):
    print(f"{hour}:00 - {count} error(s)")


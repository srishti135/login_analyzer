from file_handler import group_by_user, load_logs

df = load_logs("logs/login_logs.csv")
print(df)
df1 = group_by_user(df)

from login_analyzer import LoginAnalyzer
analyzer = LoginAnalyzer(df1)

all_findings = []
all_findings += analyzer.check_failed_logins()
all_findings += analyzer.check_suspicious_hours()
all_findings += analyzer.check_multiple_ips()

from file_handler import write_report
write_report(all_findings)
from db_handler import insert_flagged_user, clear_flagged_users

clear_flagged_users()  # clear old data first
for finding in all_findings:
    username = finding.split()[1]
    reason = finding.replace(f"[!] {username} — ", "")
    insert_flagged_user(username, reason)

print("All flagged users saved to MongoDB.")
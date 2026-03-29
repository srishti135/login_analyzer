from file_handler import group_by_user, load_logs

df = load_logs("logs/login_logs.csv")
print(df)
df1 = group_by_user(df)
print(df1)
'''
for name, group in df1:
    print(name)
    print(group)
    print("---")
'''
from login_analyzer import LoginAnalyzer
analyzer = LoginAnalyzer(df1)
analyzer.check_failed_logins()

analyzer.check_suspicious_hours()
analyzer.check_multiple_ips()
analyzer.get_stats()
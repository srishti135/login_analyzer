import pandas
class LoginAnalyzer:
    def __init__(self, grouped_data):
        self.data = grouped_data 
    def check_failed_logins(self):
        for name, group in self.data:
            failed_logins = group[group["status"] == "FAILED"]
            if not failed_logins.empty:
                print(f"User: {name} has {len(failed_logins)} failed login attempts.")
                if len(failed_logins) > 3:
                    print(f"Alert: User {name} has more than 3 failed login attempts!")
    
    def check_suspicious_hours(self):
        for name, group in self.data:
            group["timestamp"] = pandas.to_datetime(group["timestamp"])
            hour = group["timestamp"].dt.hour
            if (hour < 6).any() or (hour >= 23).any():
                 print(f"{name} is suspicious")
    def check_multiple_ips(self):
        for name, group in self.data:
            unique_ips = group["ip_address"].nunique()
            if unique_ips > 2:
                print(f"{name} logged in from {unique_ips} different IPs — suspicious")
    def get_stats(self):
        import numpy
        failed_counts = []
        for name, group in self.data:
            count = len(group[group["status"] == "FAILED"])
            failed_counts.append(count)
        print("Mean failed logins:", numpy.mean(failed_counts))
        print("Std deviation:", numpy.std(failed_counts))
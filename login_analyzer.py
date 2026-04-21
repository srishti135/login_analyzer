import pandas
import numpy

class LoginAnalyzer:

    # Stores the grouped login data when analyzer is created
    def __init__(self, grouped_data):
        self.data = grouped_data

    # Flags users with 3 or more failed login attempts
    def check_failed_logins(self):
        findings = []
        for name, group in self.data:
            failed_logins = group[group["status"] == "FAILED"]
            if len(failed_logins) >= 3:
                findings.append(f"[!] {name} — {len(failed_logins)} failed login attempts")
        return findings

    # Flags users who logged in before 6AM or after 11PM
    def check_suspicious_hours(self):
        findings = []
        for name, group in self.data:
            group["timestamp"] = pandas.to_datetime(group["timestamp"])
            hour = group["timestamp"].dt.hour
            if (hour < 6).any() or (hour >= 23).any():
                findings.append(f"[!] {name} — login at unusual hour")
        return findings

    # Flags users who logged in from more than 2 different IPs
    def check_multiple_ips(self):
        findings = []
        for name, group in self.data:
            unique_ips = group["ip_address"].nunique()
            if unique_ips > 2:
                findings.append(f"[!] {name} — login from multiple ips")
        return findings

    # Calculates mean and std deviation of failed logins using Numpy
    def get_stats(self):
        failed_counts = []
        for name, group in self.data:
            count = len(group[group["status"] == "FAILED"])
            failed_counts.append(count)
        print("Mean failed logins:", numpy.mean(failed_counts))
        print("Std deviation:", numpy.std(failed_counts))
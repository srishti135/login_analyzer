import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from file_handler import load_logs
import pandas
import os
os.makedirs("static", exist_ok=True)
# Bar chart of failed logins per user
def plot_failed_logins():
    df = load_logs("logs/login_logs.csv")
    failed = df[df["status"] == "FAILED"]
    counts = failed.groupby("username")["status"].count()
    
    counts.plot(kind="bar", color="red", title="Failed Logins Per User")
    plt.xlabel("Username")
    plt.ylabel("Failed Attempts")
    plt.tight_layout()
    plt.savefig("static/failed_logins.png")


# Pie chart of suspicious vs normal users
def plot_suspicious_ratio():
    df = load_logs("logs/login_logs.csv")
    total_users = df["username"].nunique()
    suspicious_users = 5  # alice, eve, bob, charlie, henry
    normal_users = total_users - suspicious_users

    labels = ["Suspicious", "Normal"]
    sizes = [suspicious_users, normal_users]
    colors = ["red", "green"]

    plt.figure()
    plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%")
    plt.title("Suspicious vs Normal Users")
    plt.savefig("static/suspicious_ratio.png")


# Line graph of login attempts over time
def plot_login_timeline():
    df = load_logs("logs/login_logs.csv")
    df["timestamp"] = pandas.to_datetime(df["timestamp"])
    df["hour"] = df["timestamp"].dt.hour
    hourly_counts = df.groupby("hour")["username"].count()

    plt.figure()
    plt.plot(hourly_counts.index, hourly_counts.values, marker="o", color="blue")
    plt.title("Login Attempts Over Time")
    plt.xlabel("Hour of Day")
    plt.ylabel("Number of Attempts")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("static/login_timeline.png")


plot_failed_logins()
plot_suspicious_ratio()
plot_login_timeline()
from flask import Flask, render_template, request
from file_handler import load_logs, group_by_user
from login_analyzer import LoginAnalyzer
from visualizer import plot_failed_logins, plot_suspicious_ratio, plot_login_timeline

# Generate graphs when app starts
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    username = request.form["username"]

    df = load_logs("logs/login_logs.csv")
    df1 = group_by_user(df)
    analyzer = LoginAnalyzer(df1)

    findings = analyzer.check_failed_logins()
    findings += analyzer.check_suspicious_hours()
    findings += analyzer.check_multiple_ips()

    flagged_users = [f.split()[1] for f in findings]

    # Get this user's specific stats
    user_findings = [f for f in findings if username in f]

    if username in flagged_users:
        result = f"Access Denied — {username} is flagged as suspicious!"
    else:
        result = f"Access Granted — Welcome {username}!"

    return render_template("result.html", result=result, username=username, user_findings=user_findings)
@app.route("/dashboard")
def dashboard():
    return render_template("admin_login.html")

@app.route("/admin_login", methods=["POST"])
def admin_login():
    password = request.form["password"]
    if password == "admin123":
        # Generate graphs fresh
        plot_failed_logins()
        plot_suspicious_ratio()
        plot_login_timeline()
        
        df = load_logs("logs/login_logs.csv")
        df1 = group_by_user(df)
        analyzer = LoginAnalyzer(df1)
        all_findings = analyzer.check_failed_logins()
        all_findings += analyzer.check_suspicious_hours()
        all_findings += analyzer.check_multiple_ips()
        return render_template("dashboard.html", all_findings=all_findings)
    else:
        return render_template("admin_login.html", error="Wrong password!")
        if __name__ == "__main__":
            import os
            port = int(os.environ.get("PORT", 5000))
            app.run(host="0.0.0.0", port=port)
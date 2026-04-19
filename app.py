from flask import Flask, render_template, request
from file_handler import load_logs, group_by_user
from login_analyzer import LoginAnalyzer

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
    
    if username in flagged_users:
        result = f"Access Denied — {username} is flagged as suspicious!"
    else:
        result = f"Access Granted — Welcome {username}!"
    
    return render_template("result.html", result=result)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
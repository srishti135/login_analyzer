import tkinter as tk 
window = tk.Tk()
window.title("Login Security System")
window.geometry("400x500")
title = tk.Label(window, text="Login Security System", font=("Arial", 16, "bold"))
title.pack(pady=20)

tk.Label(window, text="Username:").pack()
username_entry = tk.Entry(window, width=30)
username_entry.pack(pady=5)

tk.Label(window, text="Password:").pack() 
password_entry = tk.Entry(window, width=30, show="*")
password_entry.pack(pady=5)

def on_login():
    username = username_entry.get()
    from file_handler import load_logs, group_by_user
    from login_analyzer import LoginAnalyzer
    
    df = load_logs("logs/login_logs.csv")
    df1 = group_by_user(df)
    analyzer = LoginAnalyzer(df1)
    
    findings = analyzer.check_failed_logins()
    findings += analyzer.check_suspicious_hours()
    findings += analyzer.check_multiple_ips()
    
    flagged_users = [f.split()[1] for f in findings]
    
    if username in flagged_users:
        tkinter.messagebox.showerror("Access Denied", f"{username} is flagged as suspicious!")
    else:
        tkinter.messagebox.showinfo("Access Granted", f"Welcome {username}!")

import tkinter.messagebox
btn = tk.Button(window, text="Login", command=on_login)
btn.pack(pady=20)
window.mainloop()

import tkinter as tk 
window = tk.Tk()
window.title("Login Security System")
window.geometry("400x500")
title = tk.Label(window, text="Login Security System", font=("Arial", 16, "bold"))
title.grid(row=0, column=0, columnspan=2, pady=20)

tk.Label(window, text="Username:").grid(row=1, column=0)
username_entry = tk.Entry(window, width=30)
username_entry.grid(row=1, column=1)

tk.Label(window, text="Password:").grid(row=2,column=0) 
password_entry = tk.Entry(window, width=30, show="*")
password_entry.grid(row=2, column=1)

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
    listbox.delete(0, tk.END)  # clear previous results
    for finding in findings:
        listbox.insert(tk.END, finding)

import tkinter.messagebox
btn = tk.Button(window, text="Login", command=on_login)
btn.grid(row=3, column=0, columnspan=2, pady=10)

tk.Label(window, text="Flagged Users:").grid(row=4, column=0, columnspan=2)

listbox = tk.Listbox(window, width=50, height=10)
listbox.grid(row=5, column=0, columnspan=2, pady=10)
window.mainloop()

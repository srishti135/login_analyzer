import pandas 

#reads the csv file and returns a pandas df 
def load_logs(filepath):
    df = pandas.read_csv(filepath)
    return df
#groups login data by username 
def group_by_user(df):
    grouped = df.groupby("username")
    return grouped
#writes all suspicious findings to a text report file
def write_report(findings):
    with open("reports/suspicious_report.txt", "w") as f:
        f.write("SUSPICIOUS ACTIVITY REPORT\n\n")
        for finding in findings:
            f.write(finding + "\n")
        f.write("\nTotal flagged: " + str(len(findings)))
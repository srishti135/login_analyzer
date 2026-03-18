import pandas

def load_logs(filepath):
    df = pandas.read_csv(filepath)
    return df

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from ydata_profiling import ProfileReport

DATA_PATH = "data/insurance.csv"
REPORT_DIR = "reports"


def load_data(path=DATA_PATH):

    try:
        data = pd.read_csv(path)
        print(f"Data loaded successfully from {path}")
        return pd.read_csv(path)
    except FileNotFoundError:
        print(f"Error: File not found at {path}")
        return None
    


if __name__ == "__main__":

    df = load_data()
    

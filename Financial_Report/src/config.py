import os

# Directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.normpath(os.path.join(BASE_DIR, "../data"))
REPORT_DIR = os.path.normpath(os.path.join(BASE_DIR, "../reports"))

# Data file
EXCEL_FILE = os.path.normpath(os.path.join(DATA_DIR, "financial_data.xlsx"))
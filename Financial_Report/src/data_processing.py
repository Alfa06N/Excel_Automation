import pandas as pd
import os

def load_excel_file(file_path):
  if not os.path.exists(file_path):
    raise FileNotFoundError(f"file not found: {file_path}")
  
  file_extension = os.path.splitext(file_path)[1].lower()
  print(file_path)
  
  if file_extension == ".xlsx":
    engine = "openpyxl"
  elif file_extension == ".xls":
    engine = "xlrd"
  elif file_extension == ".csv":
    return pd.read_csv(file_path)
  else:
    raise ValueError(f"Unsupported file extension: {file_extension}")
  
  try:
    return pd.read_excel(file_path, engine=engine)
  except Exception as e:
    raise ValueError(f"Error loading file: {e}")
  
def calculate_totals(df):
  try:
    total_income = df[df["Type"] == "Income"]["Amount"].sum()
    total_expenses = df[df["Type"] == "Expense"]["Amount"].sum()
    balance = total_income + total_expenses
    
    return total_income, total_expenses, balance
  except Exception as err:
    print(f"Error in calculate_totals: {err}")
    raise
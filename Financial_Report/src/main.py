from config import EXCEL_FILE
from data_processing import load_excel_file, calculate_totals
from visualization import plot_income_expense_bar, plot_income_expense_pie, plot_income_expense_trend
import os
import pandas as pd

def main():
  try:
    df = load_excel_file(EXCEL_FILE)
    print("Datos cargados")
    print(df.head(2))
    
    total_income, total_expenses, balance = calculate_totals(df)
    
    print(f"\nTotal Incomes: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Balance: ${balance:.2f}")
    
    # Plots
    plot_income_expense_bar(total_income, total_expenses)
    plot_income_expense_pie(df)
    plot_income_expense_trend(df)
  except Exception as err:
    # print(f"Error: {err}")
    raise

if __name__ == "__main__":
  main()
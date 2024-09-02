import matplotlib.pyplot as plt
import pandas as pd

def plot_income_expense_bar(total_income, total_expenses):
  try:
    categories = ["Income", "Expenses"]
    values = [total_income, abs(total_expenses)]
    
    plt.figure(figsize=(8,6))
    plt.bar(categories, values, color=["green", "red"])
    plt.title("Income vs Expenses")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.show()
    
  except Exception as err:
    print(f"Error in plot_income_expense_bar: {err}")
    
def plot_income_expense_trend(df):
  try:
    df["Date"] = pd.to_datetime(df["Date"])
    df.sort_values("Date", inplace=True)
    
    income_trend = df[df["Type"] == "Income"].groupby("Date")["Amount"].sum()
    expense_trend = df[df["Type"] == "Expense"].groupby("Date")["Amount"].sum()
    
    plt.figure(figsize=(10, 6))
    plt.plot(income_trend.index, income_trend.values, label="Income", color="green", marker="o")
    plt.plot(expense_trend.index, expense_trend.values, label="Expenses", color="red", marker="o")
    plt.title("Income and Expense Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.legend()
    plt.show()
  except Exception as err:
    print(f"Erros in plot_income_expense_trend: {err}")
    raise
  
def plot_income_expense_pie(df):
  try:
    total_income = df[df["Type"] == "Income"]["Amount"].sum()
    total_expenses = df[df["Type"] == "Expense"]["Amount"].sum()
    
    labels = ["Income", "Expenses"]
    sizes = [total_income, abs(total_expenses)]
    colors = ["green", "red"]
    
    plt.figure(figsize=(8,8))
    plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=140)
    plt.title("Income vs Expenses Distribution")
    plt.show()
  except Exception as err:
    print(f"Error in plot_income_expense_pie: {err}")
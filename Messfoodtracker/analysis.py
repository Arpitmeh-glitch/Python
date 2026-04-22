import pandas as pd
import numpy as np

def load_data():
    try:
        df = pd.read_csv("meals.csv", header=None)
        df.columns = ["date", "day", "meal", "calories", "protein", "carbs"]

        # convert to numeric
        df["calories"] = pd.to_numeric(df["calories"])
        df["protein"] = pd.to_numeric(df["protein"])
        df["carbs"] = pd.to_numeric(df["carbs"])

        return df
    except FileNotFoundError:
        print("❌ No data found. Add meals first.")
        return None
def daily_calories(df):
    result = df.groupby("date")["calories"].sum()
    print("\n📅 Daily Calories:\n", result)
def protein_analysis(df):
    avg_protein = np.mean(df["protein"])
    
    print(f"\n💪 Average Protein Intake: {avg_protein:.2f}")

    if avg_protein < 50:
        print("⚠️ Low protein intake! Try eggs, paneer, chicken.")
    else:
        print("✅ Good protein intake!")
def carb_analysis(df):
    avg_carbs = np.mean(df["carbs"])
    print(f"\n🍞 Average Carbs: {avg_carbs:.2f}")

    if avg_carbs > 250:
        print("⚠️ High carb diet detected!")
def health_score(df):
    daily = df.groupby("date").sum()

    best_day = daily["protein"].idxmax()
    worst_day = daily["calories"].idxmax()

    print(f"\n🏆 Best Day (High Protein): {best_day}")
    print(f"⚠️ Worst Day (High Calories): {worst_day}")
import matplotlib.pyplot as plt

def plot_calories(df):
    daily = df.groupby("date")["calories"].sum()
    daily.plot(kind="bar")
    plt.title("Daily Calories")
    plt.show()
def full_report():
    df = load_data()
    if df is None:
        return
    print(df.columns)
    daily_calories(df)
    protein_analysis(df)
    carb_analysis(df)
    health_score(df)
    plot_calories(df)
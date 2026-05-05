import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data():
    try:
        df = pd.read_csv("meals.csv", header=None)
        df.columns = ["date", "day", "meal", "calories", "protein", "carbs"]

        df["calories"] = pd.to_numeric(df["calories"])
        df["protein"] = pd.to_numeric(df["protein"])
        df["carbs"] = pd.to_numeric(df["carbs"])

        return df
    except:
        print("No data found")
        return None


def daily_calories(df):
    try:
        result = df.groupby("date")["calories"].sum()
        print("\nDaily Calories")
        print(result)
    except:
        print("Error in daily calories")


def protein_analysis(df):
    try:
        avg = np.mean(df["protein"])
        print("\nAverage Protein:", round(avg, 2))

        if avg < 50:
            print("Low protein intake")
        else:
            print("Good protein intake")
    except:
        print("Error in protein analysis")


def carb_analysis(df):
    try:
        avg = np.mean(df["carbs"])
        print("\nAverage Carbs:", round(avg, 2))

        if avg > 250:
            print("High carb diet")
        else:
            print("Balanced carbs")
    except:
        print("Error in carb analysis")


def health_score(df):
    try:
        daily = df.groupby("date").sum()
        best_day = daily["protein"].idxmax()
        worst_day = daily["calories"].idxmax()

        print("\nBest Day:", best_day)
        print("Worst Day:", worst_day)
    except:
        print("Error in health score")


def weekly_trend(df):
    try:
        df["date"] = pd.to_datetime(df["date"])
        weekly = df.groupby(df["date"].dt.isocalendar().week)["calories"].mean()

        print("\nWeekly Calories")
        print(weekly)
    except:
        print("Error in weekly trend")


def smart_insights(df):
    try:
        p = df["protein"].mean()
        c = df["carbs"].mean()

        print("\nInsights")

        if p < 50:
            print("Protein low")
        else:
            print("Protein ok")

        if c > 250:
            print("Carbs high")
        else:
            print("Carbs ok")
    except:
        print("Error in insights")


def diet_recommendation(df):
    try:
        cal = df["calories"].mean()
        p = df["protein"].mean()
        c = df["carbs"].mean()

        print("\nRecommendations")

        if cal < 1800:
            print("Increase calories")
        elif cal > 2500:
            print("Reduce calories")
        else:
            print("Calories ok")

        if p < 50:
            print("Increase protein")
        else:
            print("Protein ok")

        if c > 250:
            print("Reduce carbs")
        else:
            print("Carbs ok")
    except:
        print("Error in recommendations")


def plot_calories(df):
    try:
        daily = df.groupby("date")["calories"].sum()
        daily.plot(kind="bar")
        plt.title("Daily Calories")
        plt.xlabel("Date")
        plt.ylabel("Calories")
        plt.show()
    except:
        print("Error in plotting")


def full_report():
    try:
        df = load_data()
        if df is None:
            return

        print("\nREPORT")

        daily_calories(df)
        protein_analysis(df)
        carb_analysis(df)
        health_score(df)
        weekly_trend(df)
        smart_insights(df)
        diet_recommendation(df)
        plot_calories(df)

    except:
        print("Error generating report")
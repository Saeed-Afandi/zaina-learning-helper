import pandas as pd

DATA_PATH = "data/zaina_progress.csv"


def load_data(path=DATA_PATH):
    return pd.read_csv(path)


def subject_growth(data, subject):
    subject_data = data[data["subject"] == subject].reset_index(drop=True)
    first = subject_data.iloc[0]
    last = subject_data.iloc[-1]

    return {
        "subject": subject,
        "start_score": int(first["rit_score"]),
        "latest_score": int(last["rit_score"]),
        "growth": int(last["rit_score"] - first["rit_score"]),
        "latest_percentile": (
            int(last["achievement_percentile"])
            if pd.notna(last["achievement_percentile"])
            else None
        ),
    }


def main():
    data = load_data()

    print("Zaina Learning Helper")
    print("=====================")

    for subject in ["Math", "Reading"]:
        result = subject_growth(data, subject)
        print(f"\n{result['subject']}")
        print(f"Starting RIT score: {result['start_score']}")
        print(f"Latest RIT score: {result['latest_score']}")
        print(f"Total growth: +{result['growth']} points")
        if result["latest_percentile"] is not None:
            print(f"Latest achievement percentile: {result['latest_percentile']}th")


if __name__ == "__main__":
    main()

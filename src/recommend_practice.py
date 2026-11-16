import pandas as pd

DATA_PATH = "data/zaina_progress.csv"


def latest_subject_data(data, subject):
    return data[data["subject"] == subject].iloc[-1]


def recommendation(subject, percentile):
    if percentile < 40:
        return f"Give {subject} extra practice time and review the basics slowly."
    if percentile < 60:
        return f"Keep practicing {subject} regularly and focus on weaker question types."
    return f"Continue normal {subject} practice and add a few harder questions each week."


def main():
    data = pd.read_csv(DATA_PATH)

    print("Practice Suggestions")
    print("====================")

    for subject in ["Math", "Reading"]:
        latest = latest_subject_data(data, subject)
        percentile = int(latest["achievement_percentile"])
        print(f"\n{subject}: {percentile}th percentile")
        print(recommendation(subject, percentile))


if __name__ == "__main__":
    main()

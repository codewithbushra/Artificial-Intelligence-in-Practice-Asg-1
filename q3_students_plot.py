"""
Question 3 - Read students data and plot Math, Reading, Writing scores.
Run:  python q3_students_plot.py
Make sure 'students data.csv' is in the same folder as this script.
Each figure is SAVED as a PNG and also shown on screen.
"""
import pandas as pd
import matplotlib.pyplot as plt

# 1. Read and display the data
df = pd.read_csv('students data.csv')
print("=" * 60)
print("QUESTION 3 - Students Data")
print("=" * 60)
print(df.to_string(index=False))
print()

# 2. Three separate plots, one per subject
for subject in ['Math', 'Reading', 'Writing']:
    plt.figure(figsize=(8, 4.5))
    bars = plt.bar(df['Name'], df[subject],
                   color={'Math': '#4C72B0', 'Reading': '#DD8452', 'Writing': '#55A868'}[subject])
    plt.title(f'{subject} Scores by Student')
    plt.xlabel('Student Name')
    plt.ylabel(f'{subject} Score')
    plt.ylim(0, 105)
    plt.xticks(rotation=45)
    for bar, value in zip(bars, df[subject]):       # label each bar with its value
        plt.text(bar.get_x() + bar.get_width()/2, value + 1, str(value),
                 ha='center', fontsize=9)
    plt.tight_layout()

    filename = f'{subject}_scores.png'              # e.g. Math_scores.png
    plt.savefig(filename, dpi=150)                  # SAVE the figure as PNG
    print(f"Figure saved: {filename}")

    plt.show()                                      # also display on screen
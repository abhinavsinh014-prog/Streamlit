import os
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix,
    ConfusionMatrixDisplay
)

np.random.seed(42)

n = 500

study_hours = np.random.uniform(1, 10, n)
attendance = np.random.uniform(50, 100, n)
previous_score = np.random.uniform(30, 100, n)
sleep_hours = np.random.uniform(4, 9, n)
assignments = np.random.randint(0, 11, n)
extracurricular = np.random.randint(0, 2, n)

performance_score = (
    0.35 * study_hours
    + 0.25 * attendance
    + 0.25 * previous_score
    + 0.05 * sleep_hours
    + 0.08 * assignments
    + 0.02 * extracurricular * 100
)

threshold = np.median(performance_score)

passed = (performance_score >= threshold).astype(int)

df = pd.DataFrame({
    "StudyHours": study_hours,
    "Attendance": attendance,
    "PreviousScore": previous_score,
    "SleepHours": sleep_hours,
    "AssignmentsCompleted": assignments,
    "Extracurricular": extracurricular,
    "Passed": passed
})

sns.countplot(
    x="Passed",
    data=df
)

plt.title("Student Pass/Fail Distribution")
plt.xlabel("Passed")
plt.ylabel("Number of Students")
plt.savefig("student_pass_fail.png")

sns.scatterplot(
    x="StudyHours",
    y="PreviousScore",
    hue="Passed",
    data=df
)

plt.title("Study Hours vs Previous Score")
plt.savefig("study_hours_vs_previous_score.png")

X = df.drop("Passed", axis=1)

y = df["Passed"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

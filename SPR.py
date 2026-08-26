import os
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
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
    "Assignments": assignments,
    "Extracurricular": extracurricular,
    "Passed": passed
})

st.title("Student Performance Prediction")

st.subheader("Dataset")

st.dataframe(df.head(10))


st.subheader("Dataset Statistics")

st.write(df.describe())


st.subheader("Correlation Heatmap")

fig, ax = plt.subplots(figsize=(10, 6))

sns.heatmap(
    df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    ax=ax
)

ax.set_title("Correlation Heatmap")

st.pyplot(fig)

plt.close(fig)


st.subheader("Study Hours vs Previous Score")

fig, ax = plt.subplots(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="StudyHours",
    y="PreviousScore",
    hue="Passed",
    ax=ax
)

ax.set_title("Study Hours vs Previous Score")

st.pyplot(fig)

plt.close(fig)

X = df.drop("Passed", axis=1)
y = df["Passed"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = DecisionTreeClassifier(
    random_state=42
)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)

st.subheader("Model Performance")

st.write(f"Accuracy: {accuracy:.2%}")


st.subheader("Classification Report")

report = classification_report(
    y_test,
    y_pred,
    target_names=["Failed", "Passed"],
    output_dict=True
)

report_df = pd.DataFrame(report).transpose()

st.dataframe(report_df)

st.subheader("Confusion Matrix")

cm = confusion_matrix(y_test, y_pred)

fig, ax = plt.subplots(figsize=(6, 5))

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Failed", "Passed"]
)

disp.plot(ax=ax)

ax.set_title("Confusion Matrix")

st.pyplot(fig)

plt.close(fig)

st.subheader("Decision Tree")

fig, ax = plt.subplots(figsize=(20, 10))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=["Failed", "Passed"],
    filled=True,
    rounded=True,
    ax=ax
)

st.pyplot(fig)

plt.close(fig)


st.subheader("Decision Tree Depth Analysis")

depths = range(1, 16)

train_scores = []
test_scores = []

for depth in depths:

    depth_model = DecisionTreeClassifier(
        max_depth=depth,
        random_state=42
    )

    depth_model.fit(X_train, y_train)

    train_scores.append(
        depth_model.score(X_train, y_train)
    )

    test_scores.append(
        depth_model.score(X_test, y_test)
    )

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(
    depths,
    train_scores,
    marker="o",
    label="Training Accuracy"
)

ax.plot(
    depths,
    test_scores,
    marker="o",
    label="Testing Accuracy"
)

ax.set_xlabel("Tree Depth")
ax.set_ylabel("Accuracy")

ax.set_title("Decision Tree Depth vs Accuracy")

ax.legend()

ax.grid(True)

st.pyplot(fig)

plt.close(fig)


best_index = np.argmax(test_scores)

best_depth = list(depths)[best_index]

best_accuracy = test_scores[best_index]

st.write(
    f"Best Tree Depth: **{best_depth}**"
)

st.write(
    f"Best Test Accuracy: **{best_accuracy:.2%}**"
)


model = DecisionTreeClassifier(
    max_depth=best_depth,
    random_state=42
)

model.fit(X_train, y_train)


st.subheader("Predict Student Performance")

study_hours_input = st.number_input(
    "Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=5.0
)

attendance_input = st.number_input(
    "Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=75.0
)

previous_score_input = st.number_input(
    "Previous Score",
    min_value=0.0,
    max_value=100.0,
    value=60.0
)

sleep_hours_input = st.number_input(
    "Sleep Hours",
    min_value=0.0,
    max_value=24.0,
    value=7.0
)

assignments_input = st.number_input(
    "Assignments Completed",
    min_value=0,
    max_value=10,
    value=5
)

extracurricular_input = st.number_input(
    "Extracurricular Activities",
    min_value=0,
    max_value=1,
    value=0
)


if st.button("Predict Performance"):

    input_data = pd.DataFrame({
        "StudyHours": [study_hours_input],
        "Attendance": [attendance_input],
        "PreviousScore": [previous_score_input],
        "SleepHours": [sleep_hours_input],
        "Assignments": [assignments_input],
        "Extracurricular": [extracurricular_input]
    })

    prediction = model.predict(input_data)

    probability = model.predict_proba(input_data)

    if prediction[0] == 1:

        st.success("The predicted performance is: PASSED")

        st.write(
            f"Probability of Passing: "
            f"{probability[0][1]:.2%}"
        )

    else:

        st.error("The predicted performance is: FAILED")

        st.write(
            f"Probability of Passing: "
            f"{probability[0][0]:.2%}"
        )
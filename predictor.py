import pandas as pd
import joblib
import warnings
from sklearn.exceptions import InconsistentVersionWarning


warnings.filterwarnings("ignore", category=InconsistentVersionWarning)

model = joblib.load("career-predictor-model.joblib")
columns = joblib.load("columns.joblib")

print("\n       Career Domain Predictor\n")


data = {
    "Gender": [input("Gender (Male/Female): ").strip()],
    "Age": [int(input("Age: "))],
    "GPA": [float(input("GPA: "))],
    "Major": [input("Major: ").strip()],
    "Projects": [input("Projects: ").strip()],
    "Future Career": [input("Future Career: ").strip()],
    "Python": [input("Python (Weak/Average/Strong): ").strip()],
    "SQL": [input("SQL (Weak/Average/Strong): ").strip()],
    "Java": [input("Java (Weak/Average/Strong): ").strip()]
}


df = pd.DataFrame(data)

df = pd.get_dummies(df)

df = df.reindex(columns=columns, fill_value=0)


prediction = model.predict(df)

print("\nPredicted Domain:", prediction[0])
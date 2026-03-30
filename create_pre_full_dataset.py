import numpy as np

np.random.seed(42)
N = 400

data = pd.DataFrame()

# ===== оценки по четвертям =====
for i in range(1, 5):
    data[f"grade_q{i}"] = np.clip(np.random.normal(3.8, 0.7, N), 2.5, 5)

# ===== предметы =====
data["math_grade"] = np.clip(np.random.normal(3.8, 0.8, N), 2.5, 5)
data["language_grade"] = np.clip(np.random.normal(3.8, 0.8, N), 2.5, 5)
data["science_grade"] = np.clip(np.random.normal(3.8, 0.8, N), 2.5, 5)
data["art_grade"] = np.clip(np.random.normal(3.8, 0.8, N), 2.5, 5)

# ===== посещаемость =====
for i in range(1, 5):
    data[f"attendance_q{i}"] = np.random.uniform(70, 100, N)

# ===== тест Филлипса (8 шкал) =====
data["phillips_general_anxiety"] = np.random.uniform(20, 80, N)
data["phillips_social_stress"] = np.random.uniform(20, 80, N)
data["phillips_frustration"] = np.random.uniform(20, 80, N)
data["phillips_self_expression_fear"] = np.random.uniform(20, 80, N)
data["phillips_exam_fear"] = np.random.uniform(20, 80, N)
data["phillips_expectation_fear"] = np.random.uniform(20, 80, N)
data["phillips_low_resistance"] = np.random.uniform(20, 80, N)
data["phillips_teacher_fear"] = np.random.uniform(20, 80, N)

# ===== кружки =====
data["clubs_math"] = np.random.randint(0, 2, N)
data["clubs_art"] = np.random.randint(0, 2, N)
data["clubs_sport"] = np.random.randint(0, 2, N)
data["clubs_science"] = np.random.randint(0, 2, N)

data["clubs_count"] = (
    data["clubs_math"] +
    data["clubs_art"] +
    data["clubs_sport"] +
    data["clubs_science"]
)

# ===== портфолио =====
wins = np.random.poisson(1, N)
participations = np.random.poisson(5, N)
cultural = np.random.poisson(6, N)

data["portfolio_score"] = (
    wins * 50 +
    participations * 10 +
    cultural * 5 +
    data["clubs_count"] * 15
)
data["competitions"] = participations

data["wins"] = wins

data["portfolio_score"] = np.clip(data["portfolio_score"], 0, 500)

# ===== социометрия =====
data["sociometry_status"] = np.random.randint(0, 3, N)

data["avg_grade"] = data[[f"grade_q{i}" for i in range(1,5)]].mean(axis=1)
data["avg_attendance"] = data[[f"attendance_q{i}" for i in range(1,5)]].mean(axis=1)

# ===== индекс Филлипса =====
phillips_cols = [
    "phillips_general_anxiety",
    "phillips_social_stress",
    "phillips_frustration",
    "phillips_self_expression_fear",
    "phillips_exam_fear",
    "phillips_expectation_fear",
    "phillips_low_resistance",
    "phillips_teacher_fear"
]

data["phillips_total"] = data[phillips_cols].mean(axis=1)
data

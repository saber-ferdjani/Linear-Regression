import numpy as np
import pandas as pd

np.random.seed(42)

n = 500
years = np.random.uniform(2, 18, n)          # سنوات الخبرة من 2 إلى 18

# المعادلة الخطية: 60000 عند 2 و 200000 عند 18
slope = (200000 - 60000) / (18 - 2)          # 8750
salary = 60000 + slope * (years - 2)

# ضجيج صغير باش الداتا تبان واقعية
noise = np.random.normal(0, 8000, n)
salary = salary + noise

df = pd.DataFrame({
    "years": years.round(1),
    "salary": salary.round(0)
})

print(df.shape)
print(df.head())

# df.to_csv("salary_data.csv", index=False)
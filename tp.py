import numpy as np
import pandas as pd

np.random.seed(42)

n = 500
years = np.random.uniform(2, 18, n)       
slope = (200000 - 60000) / (18)         
salary = 60000 + slope * years

noise = np.random.normal(0, 5000, n)
salary = salary + noise

df = pd.DataFrame({
    "years": years.round(1),
    "salary": salary.round(0)
})

print(df.shape)
print(df.head())

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))


plt.scatter(df["years"], df["salary"], alpha=0.5, color="steelblue",
            edgecolor="white", s=40, label="Data points")

m, b = np.polyfit(df["years"], df["salary"], 1)
x_line = np.linspace(0, 18, 100)
plt.plot(x_line, m * x_line + b, color="red", linewidth=3,
         label=f"Fitted line: y = {m:.0f}x + {b:.0f}")

plt.title("Relationship Between Years of Experience and Salary", fontsize=14)
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.xlim(0, 18)  
plt.grid(True, alpha=0.3)
plt.legend(fontsize=11)
plt.tight_layout()
plt.show()
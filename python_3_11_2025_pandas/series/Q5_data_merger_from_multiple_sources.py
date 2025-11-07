'''
Q5. ETL Simulation — Data Merge from Multiple Sources
Two branches reported sales in different days:
branch_a = pd.Series({'Mon': 1000, 'Tue': 1200, 'Wed': 900})
branch_b = pd.Series({'Tue': 1500, 'Wed': 1100, 'Thu': 1300})


Tasks:

Combine both Series using addition (branch_a + branch_b)
Observe how Pandas aligns data by index automatically
Replace missing values with 0 before addition (.fillna(0))
Final output should show total combined sales per day.
'''
import pandas as pd
branch_a = pd.Series({'Mon': 1000, 'Tue': 1200, 'Wed': 900})
branch_b = pd.Series({'Tue': 1500, 'Wed': 1100, 'Thu': 1300})

print(f"Addition of both branches:\n{branch_a.fillna(0) + branch_b.fillna(0)}")


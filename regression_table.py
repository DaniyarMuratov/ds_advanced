import pandas as pd
import statsmodels.formula.api as smf

anime_data = pd.read_csv("anime_info.csv")

model = smf.ols('rating ~ vote + view', data = anime_data)
results = model.fit()
print(results.summary())
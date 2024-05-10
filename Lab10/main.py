import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 7)
pd.set_option('display.width', 200)
df = pd.read_csv("penguins.csv")
print(df)
print(df.groupby(["species", "sex"])["body_mass_g"].mean().round(decimals=2), '\n')
print(df[df["body_mass_g"] == max(df["body_mass_g"])], '\n')
print(df[df["body_mass_g"] == min(df["body_mass_g"])], '\n')
print(df.groupby(["species", "island"])["species"].count(), '\n')
print(df[df["species"] == 'Adelie'].groupby(["species", "island"])["species"].count(), '\n')
plot = df.groupby(["island"])["species"].count().plot(kind="bar", title="DataFrameGroupBy Plot")
plt.xticks(rotation=0)
plot2 = df.plot.scatter(x="bill_length_mm", y="bill_depth_mm")
plt.show()

colors = np.where(df["sex"] == "MALE", 'b', 'r')
sz = [((df["body_mass_g"][i]/2000)**5) for i in range(len(df["body_mass_g"]))]
m = []
for i in range(0, len(df["species"])):
    if df["species"][i] == "Adelie":
        m += "<"
    elif df["species"][i] == "Chinstrap":
        m += "s"
    else:
        m += "o"
print(len(sz))
for i in range(len(df["bill_length_mm"])):
    plt.scatter(x=df["bill_length_mm"][i], y=df["bill_depth_mm"][i], marker=m[i], c=colors[i], s=5)
plt.show()

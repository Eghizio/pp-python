import pandas as pd
from webscraping import get_olympics_data
from datavis import visualize_medals


data = get_olympics_data() 

df = pd.DataFrame(data, columns=["Place", "Country", "Gold", "Silver", "Bronze"])

def get_medal_data(dataframe, medal = "Gold"):
    column = dataframe[medal]
    return {
        "Min": column.min(),
        "Max": column.max(),
        "Average": column.mean(),
        "Median": column.median(),
        "Total": column.sum(),
    }

gold = get_medal_data(df, "Gold")
silver = get_medal_data(df, "Silver")
bronze = get_medal_data(df, "Bronze")

print(gold, silver, bronze)


visualize_medals("Average medals", gold["Average"], silver["Average"], bronze["Average"])

visualize_medals("Total medals", gold["Total"], silver["Total"], bronze["Total"])

visualize_medals("Medals median", gold["Median"], silver["Median"], bronze["Median"])

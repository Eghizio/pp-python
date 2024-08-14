import matplotlib.pyplot as plt
from webscraping import get_olympics_data
from random import randint

def visualize_medals(title, gold, silver, bronze):
    categories = ["Gold", "Silver", "Bronze"]
    values = [gold, silver, bronze]
    plt.bar(categories, values, color=["#d4af37", "#c0c0c0", "#cd7f32"])

    plt.title(title)
    plt.xlabel("Medals")
    plt.ylabel("Amount")

    plt.show()

if __name__ == "__main__":
    data = get_olympics_data() 
    # index = 0
    index = randint(0, len(data)-1)
    country = data[index] # place, name, gold, silver, bronze
    print(country)

    place, name, gold, silver, bronze = country

    visualize_medals(f"Olympic Medals 2024 - {name} #{place}", gold, silver, bronze)

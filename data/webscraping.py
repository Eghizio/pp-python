import requests
from bs4 import BeautifulSoup

def try_int(x):
    try: 
        return int(x)
    except:
        return 0

def get_olympics_data():
    url = "https://pl.wikipedia.org/wiki/Klasyfikacja_medalowa_Letnich_Igrzysk_Olimpijskich_2024"
    req = requests.get(url)

    soup = BeautifulSoup(req.content, "html.parser")

    result = soup.find("table")
    table_rows = result.find_all("tr")

    # heading = table_rows[0]
    rows = table_rows[1:-1]

    def extract_text(row, selector):
        return [th.getText().strip() for th in row.find_all(selector)]

    # headings = extract_text(heading, selector="th")
    # # print(headings)

    def get_row_data(row):
        country = extract_text(row, selector="th")[0]
        place, gold, silver, bronze = extract_text(row, selector="td")[:4]
        return try_int(place), country, try_int(gold), try_int(silver), try_int(bronze)

    rows_cells = [get_row_data(row) for row in rows]
    # print(rows_cells)
    return rows_cells



if __name__ == "__main__":
    data = get_olympics_data()
    print(data)
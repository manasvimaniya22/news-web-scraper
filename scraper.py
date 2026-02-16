import requests
from bs4 import BeautifulSoup

URL = "https://www.hindustantimes.com/latest-news"

def fetch_headlines():
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(URL, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            headlines = soup.find_all("h2")

            with open("headlines.txt", "w", encoding="utf-8") as file:
                for i, headline in enumerate(headlines[:10], 1):
                    text = headline.get_text(strip=True)
                    if text:
                        file.write(f"{i}. {text}\n")

            print("Headlines saved successfully in headlines.txt")

        else:
            print("Failed to fetch page. Status code:", response.status_code)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    fetch_headlines()
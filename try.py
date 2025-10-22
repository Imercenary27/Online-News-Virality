import requests

def fetch_top_news(api_key):
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'apiKey': api_key,
        'country': 'us',  # Change this to the country code you want
        'pageSize': 100   # Change this if you want a different number of articles
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        articles = data['articles']
        return articles
    else:
        print(f"Error: {response.status_code} - {response.reason}")
        return []

if __name__ == "__main__":
    api_key = "207a0289ae3d42cc9989b83d2f50083e"
    top_news = fetch_top_news(api_key)
    for idx, article in enumerate(top_news):
        print(f"Article {idx+1}: {article['title']}")

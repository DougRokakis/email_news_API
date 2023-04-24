import requests
from send_email import send_email

topic = "tesla"
api_key="d0c130f79d144908a2a6cc98e38fe404"
url = f"https://newsapi.org/v2/everything?q={topic}&from=2023-02-28&sortBy=publishedAt&apiKey={api_key}&language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body=""
# Access the article titles and description and append the info you want from the articles to the body variable
for article in content["articles"][:20]:
    body = "Subject: Today's news" + "\n" + body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(body)
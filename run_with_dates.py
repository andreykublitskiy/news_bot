import argparse
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta

# Configuration
NEWS_API_KEY = '<api_key>'
EMAIL_ADDRESS = '<email>@gmail.com'
EMAIL_PASSWORD = '<email_password>'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

def fetch_news_articles(keywords, from_date, to_date):
    articles = []

    for keyword in keywords:
        url = f'https://newsapi.org/v2/everything?q={keyword}&from={from_date}&to={to_date}&sortBy=popularity&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            articles.extend(response.json()['articles'])
    return articles

def send_email(articles, to_email):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    msg['Subject'] = 'News Articles Update'

    body = ''
    for article in articles:
        body += f"{article['title']}\n{article['url']}\n\n"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.send_message(msg)
    server.quit()

def main():
    parser = argparse.ArgumentParser(description='Search news articles for keywords and email the results')
    parser.add_argument('keywords', metavar='keyword', type=str, nargs='+',
                        help='keywords to search for in news articles')
    parser.add_argument('--to', dest='to_email', type=str, required=True,
                        help='email address to send the articles to')
    parser.add_argument('--from_date', dest='from_date', type=str, required=True,
                        help='date range to start looking from')
    parser.add_argument('--to_date', dest='to_date', type=str, required=True,
                        help='date range to look to')

    args = parser.parse_args()

    keywords = args.keywords
    to_email = args.to_email
    from_date = args.from_date
    to_date = args.to_date

    articles = fetch_news_articles(keywords, from_date, to_date)
    send_email(articles, to_email)

if __name__ == "__main__":
    main()


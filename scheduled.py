import argparse
import requests
import schedule
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# Configuration
NEWS_API_KEY = '<key>'
EMAIL_ADDRESS = '<email>@gmail.com'
EMAIL_PASSWORD = '<email_password>'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

def fetch_news_articles(keywords):
    articles = []
    for keyword in keywords:
        url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey={NEWS_API_KEY}'
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

def job(keywords, to_email):
    print(f"Searching news articles for {', '.join(keywords)}...")
    articles = fetch_news_articles(keywords)
    if articles:
        print("Sending email...")
        send_email(articles, to_email)
        print("Email sent.")
    else:
        print("No articles found.")

def main():
    parser = argparse.ArgumentParser(description='Search news articles for keywords and email the results every morning')
    parser.add_argument('keywords', metavar='keyword', type=str, nargs='+',
                        help='keywords to search for in news articles')
    parser.add_argument('--to', dest='to_email', type=str, required=True,
                        help='email address to send the articles to')
    args = parser.parse_args()

    keywords = args.keywords
    to_email = args.to_email

    job(keywords, to_email)

    # Schedule job to run every morning at 8 AM
    schedule.every().day.at("11:45").do(job, keywords, to_email)

    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()


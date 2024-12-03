from newspaper import Article
from bs4 import BeautifulSoup
import requests
import openai
import smtplib
from email.mime.text import MIMEText

# Replace with your API keys and GMAIL login information
newsapi_key = ""
openai_key = ""

GMAIL_USERNAME = ""
GMAIL_APP_PASSWORD = ""

client = openai.OpenAI(api_key=openai_key)
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi_key}"
newsforSummary = ''


def fetch_with_newspaper(url):
    """
    Fetch article content using newspaper3k.
    """
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        return f"Failed to fetch with newspaper: {e}"

def fetch_with_beautifulsoup(url):
    """
    Fetch article content using BeautifulSoup.
    """
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        return " ".join([p.get_text() for p in paragraphs])
    except Exception as e:
        return f"Failed to fetch with BeautifulSoup: {e}"

# Fetch news and process content
response = requests.get(url)
if response.status_code == 200:
    news_data = response.json()
    for article in news_data['articles'][:50]:  # Limit articles
        title = article['title']
        link = article['url']
        print(f"Title: {title}")
        print(f"Link: {link}")

        # Fetch content using newspaper3k or BeautifulSoup as a fallback
        content = fetch_with_newspaper(link)
        if content.startswith("Failed"):
            content = fetch_with_beautifulsoup(link)
            if content.startswith("Failed"):
                content = 'Skip'
        if content != 'Skip':
            addContent = f'| Article Title: {title}, Article Content: {content} |'
            newsforSummary = newsforSummary + addContent
        
        print(f"Content:\n{content}\n")
else:
    print("Failed to fetch news.")

try:
    # OpenAI API call
    completion = openai.OpenAI(api_key=openai_key).chat.completions.create(
    model="gpt-4o-mini",
    messages=[
       {"role": "system", "content": "You are a newsletter generator."},
           {
             "role": "user",
            "content": 'Please summarize the following list of articles and generate a daily newsletter, please format it so that it readable and similiar to a regular newsletter (Should be 2-4 pages max). Generate and include a morning greeting for Myles. The output of this completion should ONLY be HTML code for the newsletter to be a page on a website, do not include anything else in your response. Please theme the HTML code so the lewsletter is winter themed. Double check for formatting errors that may make it hard to read (Example: Text and background color being the same). Make sure to include a snowman emoji somewhere. Remove the ```html and ``` at the end of your response, it is not needed. Here are the articles: '+newsforSummary
            }
            ]
        )
    print('Newsletter: \n', completion.choices[0].message.content)
    recipients = [f"{GMAIL_USERNAME}@gmail.com"]
    msg = MIMEText(completion.choices[0].message.content, "html")
    msg["Subject"] = "AI Morning Newsletter!"
    msg["To"] = ", ".join(recipients)
    msg["From"] = f"{GMAIL_USERNAME}@gmail.com"

    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(GMAIL_USERNAME, GMAIL_APP_PASSWORD)
    smtp_server.sendmail(msg["From"], recipients, msg.as_string())
    smtp_server.quit()
except Exception as e:
    print("API Error", f"An error occurred: {e}")

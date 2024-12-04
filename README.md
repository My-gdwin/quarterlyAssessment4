# quarterlyAssessment4
# AI-Powered Daily Newsletter Generator 📬

## Overview

This Python project generates a daily newsletter using the latest news headlines. The process includes:

1. Fetching top news articles from the NewsAPI.
2. Summarizing article content using OpenAI's GPT API.
3. Formatting the summarized content into a winter-themed HTML newsletter.
4. Sending the newsletter via email using Gmail.

---

## Features

- **Article Scraping**: Uses `newspaper3k` and `BeautifulSoup` to extract content from news articles.
- **Summarization**: OpenAI's GPT model generates summaries and formats them as newsletters.
- **HTML Formatting**: The newsletter is outputted in a winter-themed HTML design, complete with a snowman emoji ☃️.
- **Email Delivery**: Sends the generated newsletter directly to specified recipients via Gmail.

---

## Setup

1. Open the `main.py` file and replace the placeholders with your credentials:
   ```python
   newsapi_key = "your_newsapi_key"
   openai_key = "your_openai_key"

   GMAIL_USERNAME = "your_gmail_username"
   GMAIL_APP_PASSWORD = "your_gmail_app_password"
   ```

2. Ensure Gmail App Passwords are enabled. Follow [this guide](https://support.google.com/mail/answer/185833?hl=en) to generate an app password.

---

## Usage

Run the script to generate and send the newsletter:
```bash
python main.py
```

### Workflow:

1. **Fetch Top Headlines**: Retrieves the latest news using the NewsAPI.
2. **Extract Content**:
   - First attempts to use `newspaper3k`.
   - Falls back to `BeautifulSoup` if needed.
3. **Summarize & Generate Newsletter**:
   - Summarizes articles and generates an HTML newsletter.
   - Includes a morning greeting and winter theme.
4. **Send via Email**:
   - The generated newsletter is emailed to recipients.

---

## Example Output

### Email:
- **Subject**: "AI Morning Newsletter!"
- **Body**: A winter-themed, HTML-formatted newsletter summarizing the latest news.

### HTML Content:
- A visually appealing layout with:
  - A morning greeting for the user.
  - News summaries.
  - A winter-themed design featuring ❄️ snowflakes and ☃️ a snowman.

---

## Dependencies

The project requires the following Python libraries:
- `newspaper3k`
- `beautifulsoup4`
- `requests`
- `openai`
- `smtplib` (built-in)

Install all dependencies via pip:
```bash
pip install REQUIREMENT_HERE
```

---

## File Structure

```
newsletter-generator/
├── script.py          # Main script to fetch, summarize, and email the newsletter
├── README.md          # Project documentation
└── requirements.txt   # Python dependencies (optional)
```

---

## Troubleshooting

1. **NewsAPI Key Issues**:
   - Ensure your NewsAPI key is valid and has sufficient access.

2. **OpenAI Errors**:
   - Ensure your OpenAI key is active and has access to GPT.

3. **Gmail Issues**:
   - Double-check your Gmail username and app password.
   - Ensure your Gmail account has "Allow Less Secure Apps" or App Passwords enabled.

4. **Dependencies**:
   - Use `pip install` to install any missing libraries.

---

## License

This project is licensed under the MIT License.

---

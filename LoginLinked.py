import requests
from bs4 import BeautifulSoup

# Get Credentials
username = str(input("Enter your email: "))
password = str(input("Enter your password: "))

# Set Headers
login_page_url = "https://www.linkedin.com/login"
feed_url = "https://www.linkedin.com/feed/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

login_data = {
    'session_key': username,
    'session_password': password,
    'loginCsrfParam': '',
}

# Get Session Ready


def Login():
    session = requests.Session()
    session.headers = headers

    login_page = session.get(login_page_url)
    soup = BeautifulSoup(login_page.text, 'html.parser')

    login_data['loginCsrfParam'] = Get_Csrf_Token(soup)
    post_login_url = "https://www.linkedin.com/checkpoint/lg/login-submit"
    response = session.post(post_login_url, data=login_data)

    feed_page = session.get(feed_url)
    if "feed" in feed_page.url:
        print("Login successful!")
        return session
    else:
        return 'something went wrong!'


# Get CSRF
def Get_Csrf_Token(soup):
    csrf_token = soup.find('input', {'name': 'loginCsrfParam'})['value']
    return csrf_token


# if __name__ == "__main__":
#     Login()

import requests
import secrets
from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69'}


def bump():
    username = secrets.username
    login_payload = {
        'username': username,
        'password': secrets.password
    }

    base_url = "https://www.depop.com/"
    auth_url = "https://webapi.depop.com/api/auth/v1/"

    with requests.Session() as s:
        s.headers.update(header)
        s.get(base_url + "login/")

        # Login Options and Post
        s.options(url=auth_url + "login", headers=header)
        login = s.post(url=auth_url + "login", data=login_payload)
        print(login)

        # Me options and post
        # (Not sure exactly what this is? Keeping to replicate the browser login flow)
        s.options(url=auth_url + "me")
        s.post(url=auth_url + "me")

        s.get(base_url)
        my_page = s.get(base_url + username)

        soup = BeautifulSoup(my_page.text, 'html.parser')

        x = soup.find("div", {"id": "products-tab"})
        print(soup.prettify())




if __name__ == '__main__':
    bump()

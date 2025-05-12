import random, string, requests


charsets = [string.ascii_lowercase, string.ascii_uppercase, string.digits]
def get_randRoute():
    route = ""
    for x in range(6):
        route += random.choice(random.choice(charsets))
    return route

def get_URL(domain):
    return "https://" + domain + "/" + get_randRoute()

def Mine_Image(domain):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    } # Used to fool Cloudflare

    URL = get_URL(domain)
    def try_URL():
        response = requests.get(URL, headers=headers, timeout=5)
        if response.status_code == 200 and response.url == URL and "img" in response.text:
            return True
        else:
            return False

    if try_URL():
        print('Valid URL: ' + URL)
    else:
        print('Not Valid URL: ' + URL)
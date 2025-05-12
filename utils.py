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

    URL = ""
    def try_URL():
        URL = get_URL(domain)
        response = requests.get(URL, headers=headers, timeout=5)
        if response.status_code == 200 and response.url == URL and int(len(response.content)) == 16328:
            print(str(len(response.content)))
            return URL
        else:
            return try_URL()

    return try_URL()
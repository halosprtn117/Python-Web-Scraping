import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError


def download(url):
    print("Downloading:", url)
    try:
        html = urllib.request.urlopen(url).read()
    except(URLError, HTTPError, ContentTooShortError) as e:
        print("Download error:", e.reason)
        html = None
    return html


def main():
    download("http://example.webscraping.com")


if __name__ == "__main__":
    main()

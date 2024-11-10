import urllib.request
request_url = urllib.request.urlopen('https://buynothingproject.org/')
print(request_url.read())
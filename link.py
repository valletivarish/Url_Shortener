import pyshorteners

class LinkShortener:
    def __init__(self):
        self.s = pyshorteners.Shortener()
        self.url_mapping = {}  # Placeholder for link storage, replace it with your actual implementation

    def shorten_url(self, original_url):
        short_url = self.s.tinyurl.short(original_url)
        short_code = short_url.split("/")[-1]
        self.url_mapping[short_code] = original_url
        return short_url

    def get_original_url(self, short_code):
        return self.url_mapping.get(short_code, None)

from flask import Flask, render_template, request, redirect
from link import LinkShortener

app = Flask(__name__)
link_shortener = LinkShortener()

def get_form():
    return (
        "<div style='text-align: center; padding: 50px; background-color: #3498db; color: white; animation: fadeIn 1s;'>"
        "<h1 style='color: #2c3e50; font-size: 2em; margin-bottom: 20px;'>Welcome to the Link Shortener</h1>"
        "<p style='font-size: 1.2em; margin-bottom: 20px;'>Enter a URL to shorten:</p>"
        "<form method='post' action='/shorten'>"
        "<input type='url' name='original_url' required style='padding: 10px; width: 300px; border: none; border-radius: 5px; font-size: 1em; transition: all 0.3s;'>"
        "<br><br>"
        "<button type='submit' style='padding: 10px; background-color: #2c3e50; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 1.2em; transition: all 0.3s;'>Shorten Link</button>"
        "</form>"
        "</div>"
        "<style>"
        "body { margin: 0; font-family: 'Arial', sans-serif; background-color: #3498db; animation: fadeIn 1s; }"
        "a { color: #2c3e50; }"
        "@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }"
        "input:focus, button:focus { outline: none; box-shadow: 0 0 5px rgba(44, 62, 80, 0.8); }"
        "</style>"
    )

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form.get('original_url')
        short_url = link_shortener.shorten_url(original_url)
        return (
            f"<div style='color: #2c3e50; font-size: 1.2em; animation: fadeIn 1s; margin-top: 20px;'>"
            f"Original URL: {original_url}<br>Short URL: {short_url}</div>"
            + get_form()
        )
    else:
        return get_form()

@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form.get('original_url')
    short_url = link_shortener.shorten_url(original_url)
    return f"<div style='color: #2c3e50; font-size: 1.2em; animation: fadeIn 1s;'>Original URL: {original_url}<br>Short URL: {short_url}</div>"

@app.route('/<short_code>')
def redirect_to_original(short_code):
    original_url = link_shortener.get_original_url(short_code)
    if original_url:
        return redirect(original_url)
    else:
        return "<div style='color: #2c3e50; font-size: 1.2em; animation: fadeIn 1s;'>Not Found: The requested short URL was not found.</div>"

if __name__ == '__main__':
    app.run(debug=True)

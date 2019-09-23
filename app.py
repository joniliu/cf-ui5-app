import os

from flask import Flask, render_template, make_response, send_from_directory

app = Flask(__name__)


# Render index.html initially
@app.route('/')
def render_index():
    return render_template('index.html')


# Render stylings
@app.route('/css/style.css', methods=["GET"])
def render_style():
    try:
        response = make_response(render_template('css/style.css'))
        response.headers['Content-type'] = "text/css; charset=utf-8"
        return response
    except Exception as e:
        print("\033[93m" + str(e) + "\033[0m")
        return 'OK'


# Render SAPUI5 web app files from templates folder
@app.route('/<path:path>')
def render_path(path):
    if "img" in path or ".js" in path or "i18n" in path or "favicon" in path or ".json" in path or ".css" in path:
        return send_from_directory('templates', path)
    else:
        return render_template(path)


port = int(os.getenv("PORT", 0))
if __name__ == '__main__':
    if port != 0:
        app.run(host='0.0.0.0', port=port)
    else:
        app.run()

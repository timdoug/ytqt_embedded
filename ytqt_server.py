import urlparse
import subprocess

from flask import Flask, make_response, request

app = Flask(__name__)

@app.route("/")
def hello():
    yt_url = request.args.get('url', '')
    if len(urlparse.parse_qs(urlparse.urlparse(yt_url).query).get('v', [''])[0]) != 11:
        return 'Bad URL'
    vid_url = subprocess.Popen('youtube-dl -g -f 38/37/22/18 "%s"' % yt_url, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()
    return make_response(vid_url[0].strip(), 200, {'Access-Control-Allow-Origin': '*'})

if __name__ == "__main__":
    app.run(debug=True)

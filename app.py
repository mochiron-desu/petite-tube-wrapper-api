from flask import Flask, jsonify, render_template_string
import requests
from bs4 import BeautifulSoup
from pytube import YouTube

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    documentation = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>PetitTube API</title>
            </head>
            <body>
                <h1>Welcome to the PetitTube API!</h1>
                <p>Use the following endpoint to get PetitTube URL, YouTube title, and views:</p>
                <code>/geturl</code>
                <h2>Example Result:</h2>
                <pre>
    {
      "petittube_url": "https://www.youtube.com/embed/example_video_id",
      "youtube_title": "Example YouTube Title",
      "views": 12345
    }
                </pre>
            </body>
            </html>
        """
    return render_template_string(documentation)

@app.route('/geturl', methods=['GET'])
def get_petittube_url():
    url = "https://petittube.com/index.php"

    # Make a request to the PetitTube website
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the iframe element with the YouTube video
        iframe = soup.find("iframe")

        # Extract the src attribute containing the YouTube video URL
        video_url = iframe["src"]

        # Use pytube to get the YouTube title
        try:
            youtube = YouTube(video_url)
            youtube_title = youtube.title
            views = youtube.views
        except Exception as e:
            return jsonify({"error": f"Failed to retrieve YouTube title: {str(e)}"})

        return jsonify({
            "petittube_url": video_url, 
            "youtube_title": youtube_title,
            "views": views
        })

    else:
        return jsonify({"error": "Failed to retrieve data from PetitTube"})

if __name__ == '__main__':
    app.run(debug=True)

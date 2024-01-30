from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import os
from moviepy.editor import VideoFileClip

app = Flask(__name__)

@app.route('/scrape-reel', methods=['POST'])
def scrape_reel():
    # Get the tag from the request
    data = request.get_json()
    tag = data.get('tag')

    # Scrape the reel link
    url = f'https://www.instagram.com/reels{tag}/'
    r = requests.get(url)
    r.raise_for_status()

    # Create a Reel object
    soup = BeautifulSoup(r.text, 'html.parser')
    reel = soup.find('a', {'class': 'V1Nh3'})  # Change the class name here

    if reel:  # Check if the element exists
        reel_link = reel['href']

        # Download the video
        response = requests.get(reel_link)
        response.raise_for_status()

        # Save the video to the project directory
        with open('reel.mp4', 'wb') as f:
            f.write(response.content)

        # Convert the video to .mpg format
        clip = VideoFileClip('reel.mp4')


        # Return the downloadable link as a response
        return jsonify({'downloadable_link': 'reel.mpg'})
    else:
        return jsonify({'error': 'Reel link not found'})

if __name__ == '__main__':
    app.run()
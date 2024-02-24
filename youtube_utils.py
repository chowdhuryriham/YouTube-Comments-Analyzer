from googleapiclient.discovery import build
from bs4 import BeautifulSoup
import re

def get_video_comments(api_key,video_id, max_results=100):
    youtube = build('youtube', 'v3', developerKey=api_key)

    comments = []
    nextPageToken = None

    while True:
        response = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=max_results,
            pageToken=nextPageToken
        ).execute()

        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']
            commenter_name = comment['authorDisplayName']
            comment_text = comment['textDisplay']
            soup = BeautifulSoup(comment_text, 'html.parser')
            comment_text = re.sub(r'[^\w\s]', '', soup.get_text(strip=True))  # Remove non-alphanumeric characters
            comments.append({'commenter': commenter_name, 'comment': comment_text})

        nextPageToken = response.get('nextPageToken')

        if not nextPageToken:
            break

    return comments

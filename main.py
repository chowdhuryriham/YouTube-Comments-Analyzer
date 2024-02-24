from youtube_utils import get_video_comments
from sentiment_analysis import sentiment_score, process_comments
from topic_modeling import topic_modeling, extract_topics
from output_utils import save_to_excel

def determine_sentiment(sentiment_score):
    if sentiment_score <= 2:
        return 'Negative'
    elif sentiment_score <= 3:
        return 'Neutral'
    else:
        return 'Positive'

def main(api_key, video_id, output_excel):
    # Retrieve video comments
    video_comments = get_video_comments(api_key,video_id)

    # Process comments
    processed_comments = process_comments(video_comments)

    # Print the first 10 comments with sentiment analysis and sentiment determination
    print("First 10 comments with sentiment analysis and sentiment determination:")
    for i, comment in enumerate(processed_comments[:10]):
        sentiment = determine_sentiment(comment['sentiment'])
        print(f"Comment {i+1}: {comment['comment']} - Sentiment: {sentiment}")

    # Perform topic modeling
    lda_model = topic_modeling([comment['comment'] for comment in processed_comments])

    # Extract topics from the LDA model
    topics = extract_topics(lda_model)

    # Print topics
    print("\nTopics:")
    for topic in topics:
        print(topic)

    # Save DataFrame to Excel file
    save_to_excel(processed_comments, output_excel)
    print(f"Output saved to {output_excel}")

if __name__ == "__main__":
    # YouTube API key and video ID
    api_key = 'AIzaSyAFmImey5MdQd3dX4qXpibPzUhTEF7bxOU'
    video_id = 'srt4COKMVx8'
    output_excel = 'youtube_comments_analysis.xlsx'
    main(api_key, video_id, output_excel)

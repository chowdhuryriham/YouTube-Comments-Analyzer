from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

def sentiment_score(comment):
    tokens = tokenizer.encode(comment, return_tensors='pt')
    result = model(tokens)
    return int(torch.argmax(result.logits)) + 1

def process_comments(video_comments):
    processed_comments = []
    for comment in video_comments:
        processed_comment = process_comment(comment)
        processed_comments.append(processed_comment)
    return processed_comments

def process_comment(comment):
    comment_text = comment['comment']
    sentiment = sentiment_score(comment_text)
    return {'commenter': comment['commenter'], 'comment': comment_text, 'sentiment': sentiment}

from gensim import corpora, models

def preprocess_text(comment):
    # Perform text preprocessing steps such as tokenization, lowercasing, removing stop words, etc.
    # Example:
    processed_comment = [token.lower() for token in comment.split() if token.isalpha()]
    return processed_comment

def topic_modeling(comments):
    # Preprocess comments
    processed_comments = [preprocess_text(comment) for comment in comments]

    # Create dictionary and corpus
    dictionary = corpora.Dictionary(processed_comments)
    corpus = [dictionary.doc2bow(comment) for comment in processed_comments]

    # Build LDA model
    lda_model = models.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=10, iterations=100)

    return lda_model

def extract_topics(lda_model):
    topics = lda_model.print_topics(num_words=5)
    extracted_topics = [{'topic': topic[0], 'keywords': topic[1]} for topic in topics]
    return extracted_topics

import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from collections import defaultdict

def summarize_text(text):
    """
    Summarize the extracted text.

    Args:
        text (str): Input text.

    Returns:
        str: Summarized text.
    """
    # Define stopwords and tokenize text
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)
    sentences = sent_tokenize(text)
    
    # Calculate word frequencies (excluding stopwords)
    freq_table = defaultdict(int)
    for word in words:
        word = word.lower()
        if word not in stopWords:
            freq_table[word] += 1
    
    # Calculate sentence scores based on word frequencies
    sentence_scores = defaultdict(int)
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in freq_table:
                sentence_scores[sentence] += freq_table[word]
    
    # Determine the average score
    avg_score = sum(sentence_scores.values()) / len(sentence_scores)
    
    # Select sentences with a score above the average
    summary_sentences = [sentence for sentence in sentences if sentence_scores[sentence] > avg_score]
    summary = ' '.join(summary_sentences)
    
    return summary

def analyze_sentiment(summary):
    """
    Analyze the sentiment of the text.

    Args:
        summary (str): Summarized text.

    Returns:
        str: Sentiment label ('Positive', 'Negative', or 'Neutral').
    """
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(summary)
    
    if sentiment['compound'] >= 0.05:
        return 'Positive'
    elif sentiment['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# YouTube Comments Analysis

## Purpose
This project aims to analyze comments from a YouTube video to gain insights into viewer sentiment, identify common topics of discussion, and provide valuable feedback for content creators. The analysis includes sentiment analysis of comments, topic modeling to identify prevalent themes, and saving the raw sentiment analysis results to an Excel file for further examination.

## How to Run
To run the analysis, follow these steps:

1. Install the required libraries:
    ```
    pip install transformers torch google-api-python-client pandas numpy
    ```

2. Obtain a YouTube Data API key from the Google Cloud Console.

3. Replace `YOUR_API_KEY` in `main.py` with your API key.

4. Set the `video_id` variable in `main.py` to the ID of the YouTube video you want to analyze.

5. Run the `main.py` script:
    ```
    python main.py
    ```

6. The script will retrieve comments from the specified YouTube video, perform sentiment analysis, conduct topic modeling, print the results, and save them to an Excel file named `youtube_comments_analysis.xlsx`.

## Files
- `main.py`: Main script to run the analysis.
- `youtube_utils.py`: Utility functions for retrieving comments from YouTube.
- `sentiment_analysis.py`: Functions for sentiment analysis of comments.
- `topic_modeling.py`: Functions for topic modeling of comments.
- `output_utils.py`: Utility functions for saving the analysis results to Excel.

## Dependencies
- transformers
- torch
- google-api-python-client
- pandas
- numpy
- BeautifulSoup4

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

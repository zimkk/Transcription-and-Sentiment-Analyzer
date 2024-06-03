
```markdown
# Text Processing Application

This application processes text from various input sources (audio, images, text files, and websites) to provide summarized text and sentiment analysis. It leverages several Python libraries for text extraction, summarization, and sentiment analysis.

## Features

- Convert audio to text using Google Speech Recognition API.
- Extract text from images using Tesseract OCR.
- Scrape text content from websites.
- Summarize the extracted text.
- Analyze the sentiment of the summarized text.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/text-processing-application.git
   cd text-processing-application
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv env
   source env/bin/activate   # On Windows use `env\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Download NLTK data:

   ```python
   python -m nltk.downloader punkt vader_lexicon stopwords
   ```

## Usage

Run the main script:

```bash
python main.py
```

Follow the on-screen prompts to choose an input source and view the results.

## File Descriptions

- `main.py`: The main entry point of the application.
- `audio_processing.py`: Contains functions to convert audio to text.
- `image_processing.py`: Contains functions to extract text from images.
- `web_scraping.py`: Contains functions to scrape text from websites.
- `text_processing.py`: Contains functions to summarize text and analyze its sentiment.

## Dependencies

- Python 3.6+
- `pytesseract`
- `Pillow`
- `nltk`
- `requests`
- `beautifulsoup4`
- `speechrecognition`

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```

---

## Documentation.md

```markdown
# Text Processing Application Documentation

## Overview

This document provides detailed information about the Text Processing Application, including installation instructions, usage guidelines, and a description of the modules and their functions.

## Installation

### Prerequisites

- Python 3.6+
- `pip` (Python package installer)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/text-processing-application.git
   cd text-processing-application
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv env
   source env/bin/activate   # On Windows use `env\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Download NLTK data:

   ```python
   python -m nltk.downloader punkt vader_lexicon stopwords
   ```

## Usage

To run the application, execute the following command:

```bash
python main.py
```

### User Interaction

Upon running the script, users will be prompted to choose an input source:

- `'R'` - Record voice
- `'F'` - Input file name
- `'I'` - Input image path
- `'W'` - Input website URL

After processing the input, users can choose how to view the results:

- `'S'` - Summary only
- `'A'` - Complete analysis report (Original Text + Summary + Sentiment)
- `'B'` - Both Summary and Sentiment

## Module Descriptions

### `main.py`

The main script that manages user interaction and orchestrates the processing flow. It imports functions from other modules to handle different input types and perform text processing tasks.

### `audio_processing.py`

- **`convert_audio_to_text(filename=None)`**: Converts audio to text using Google Speech Recognition API. If a filename is provided, it processes the audio file. Otherwise, it records audio from the microphone.

### `image_processing.py`

- **`convert_image_to_text(image_path)`**: Uses Tesseract OCR to extract text from an image file and formats the extracted text into sentences.

### `web_scraping.py`

- **`scrape_text_from_website(url)`**: Scrapes text content from the given website URL and formats it into sentences. Extracts text from common text-containing HTML elements.

### `text_processing.py`

- **`summarize_text(text)`**: Summarizes the input text by calculating word frequencies and sentence scores. Returns the summarized text.
- **`analyze_sentiment(summary)`**: Analyzes the sentiment of the summarized text using NLTK's VADER sentiment analysis tool. Returns a sentiment label ('Positive', 'Negative', or 'Neutral').

## Dependencies

- `pytesseract`: Python-tesseract is an optical character recognition (OCR) tool for Python.
- `Pillow`: Python Imaging Library (PIL) fork that supports opening, manipulating, and saving many different image file formats.
- `nltk`: The Natural Language Toolkit is a platform for building Python programs to work with human language data.
- `requests`: A simple, yet elegant HTTP library for Python.
- `beautifulsoup4`: A library for parsing HTML and XML documents.
- `speechrecognition`: Library for performing speech recognition with support for several engines and APIs.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```

---

Feel free to modify these documents to better fit your specific project details and any additional information you may want to include.

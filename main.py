from audio_processing import convert_audio_to_text
from image_processing import convert_image_to_text
from web_scraping import scrape_text_from_website
from text_processing import summarize_text, analyze_sentiment

if __name__ == '__main__':
    print("Choose an option to provide input:")
    print("  'R' - Record voice")
    print("  'F' - Input file name")
    print("  'I' - Input image path")
    print("  'W' - Input website URL")
    
    choice = input("Enter your choice: ").upper()
    
    if choice == 'R':
        text = convert_audio_to_text()
    elif choice == 'F':
        filename = input("Enter the file name: ")
        text = convert_audio_to_text(filename)
    elif choice == 'I':
        image_path = input("Enter the image path: ")
        text = convert_image_to_text(image_path)
    elif choice == 'W':
        website_url = input("Enter the website URL: ")
        text = scrape_text_from_website(website_url)
    else:
        print("Invalid choice. Please enter 'R', 'F', 'I', or 'W'.")
        text = None

    if text:
        summary = summarize_text(text)
        sentiment = analyze_sentiment(summary)
        
        print("\nChoose an option to view the result:")
        print("  'S' - Summary only")
        print("  'A' - Complete analysis report (Original Text + Summary + Sentiment)")
        print("  'B' - Both Summary and Sentiment")
        
        report_choice = input("Enter your choice: ").upper()
        
        if report_choice == 'S':
            print("\nSummary:\n", summary)
        elif report_choice == 'A':
            print("\nOriginal Text:\n", text)
            print("\nSummary:\n", summary)
            print("\nSentiment:\n", sentiment)
        elif report_choice == 'B':
            print("\nSummary:\n", summary)
            print("\nSentiment:\n", sentiment)
        else:
            print("Invalid choice. Please enter 'S', 'A', or 'B'.")

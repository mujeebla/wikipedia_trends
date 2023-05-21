# Wikipedia Top 5 Trends

## Description
This project shows the top n (5 default) articles trending on Wikipedia for any given day. There's an API call at the beginning to get the top n articles by views. Subsequent API calls are made to get the recent daily views for each article, limited to the last week.

Line charts are generated for each article, showing daily values over the last 1 week. The remaining pages of the report provide context around why each article was trending, as provided by Chat-GPT.

A sample report is `Trending_Yesterday.pdf`

## Installation
I have shared a `requirements.txt` file showing all required libraries. To use this project, you also need API keys for OpenAi and SERPAPI.

The `WikipediaTrendsWithChatGPT.ipynb` notebook is the main notebook. There, I import all required libraries and functions to show a working example.

## Features
1. Retrieval and parsing of data from an API.
2. Extension of Python's Figure class to generate presentations using the matplotlib library.
3. Creative solutions to provide context around why an article might be trending, including the use of ChatGPT and obtaining images through Google.
4. Utilization of Wikipedia and Google as tools with Chat-GPT to find accurate answers.

## Next Steps
1. Build a Pipeline around this. I enjoy working with Apache Airflow and see how all these steps could be automated and set up to run daily.
2. Instead of generating PDF reports, an HTML file could be generated and shared as an email alert.
3. Refine the Chat-GPT prompt.
4. Package the application in a Docker container for easier deployment.
5. Develop an ML model to predict the decay of trending topics over time.

Please note that these are suggestions for future development and enhancement of the project. You can choose to prioritize and implement these steps based on your specific requirements and preferences.

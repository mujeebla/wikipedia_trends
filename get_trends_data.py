## Get Data

from requests import request
import pandas as pd
from datetime import datetime, timedelta

# yesterday = datetime.now() - timedelta(1)

headers = {'accept': 'application/json',
          'User-Agent': 'reachmujeebhere@gmail.com'}


def get_top_n_trending(n=5, day=None):
    """
    Retrieves the top N trending articles from the Wikimedia pageviews API.

    Parameters:
        n (int): The number of top articles to retrieve. Default is 5.
        day (datetime): The specific day for which to retrieve trending articles. 
                        If not provided, the previous day is used.

    Returns:
        numpy.ndarray: An array containing the top N trending article titles.

    """

    if day is None:
        day = datetime.now() - timedelta(1)
    url = f"https://wikimedia.org/api/rest_v1/metrics/pageviews/top-per-country/US/all-access/{day.strftime('%Y/%m/%d')}"
    r = request("get", url, headers=headers)
    df = pd.json_normalize(r.json()['items'][0]['articles'])

    filtered_df = df.loc[(~df.article.str.match('.*:.*')) & df.project.str.match('^en.*'), :]
    filtered_df = filtered_df.sort_values(by='views_ceil', ascending=False)
    filtered_df = filtered_df[filtered_df.article != 'Main_Page']
    return filtered_df.article.values[:n]


def get_a_weeks_data(article=None, day=None):
    """
    Retrieves a week's worth of data for a specific article from the Wikimedia pageviews API.

    Parameters:
        article (str): The title of the article for which to retrieve data.
        day (datetime): The specific day for which to retrieve data. 
                        If not provided, the previous day is used.

    Returns:
        pandas.DataFrame: A DataFrame containing the article title, timestamp, and views for each day.

    """

    if day is None:
        day = datetime.now() - timedelta(days=1)
    a_week_ago = day - timedelta(days=7)
    url = f'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/all-agents/{article}/daily/{a_week_ago.strftime("%Y%m%d")}/{day.strftime("%Y%m%d")}'
    response = request("get", url, headers=headers)
    data = response.json()

    df = pd.json_normalize(data["items"])
    return df[['article', 'timestamp', 'views']]


def create_table(articles):
    """
    Creates a table by retrieving a week's worth of data for a list of articles from the Wikimedia pageviews API.

    Parameters:
        articles (list): A list of article titles for which to retrieve data.

    Returns:
        pandas.DataFrame: A DataFrame containing the combined data for all articles, including the article title, timestamp, and views for each day.

    """
    all_tables = []
    
    for article in articles:
        df = get_a_weeks_data(article=article)
        all_tables.append(df)
    
    return pd.concat(all_tables, ignore_index=True)
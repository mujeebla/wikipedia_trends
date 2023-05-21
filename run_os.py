from datetime import datetime, timedelta
import subprocess
from subprocess import Popen, PIPE, DEVNULL
from io import BytesIO, StringIO
import pandas as pd
import gzip
import requests
import json


yesterday = datetime.now() - timedelta(1)
a_month_ago = yesterday - timedelta(7)
year = yesterday.year
month = yesterday.month
day = yesterday.day
date_string = yesterday.strftime("%Y%m%d")


file_name = f"pageviews-{date_string}-230000"

# url = f"https://dumps.wikimedia.org/other/pageviews/{year}/{year}-{month}/pageviews-{date_string}-230000.gz"
# get_data = Popen(["wget", url])
# get_data.wait()
# un_zip = Popen(["gunzip", f'{file_name}.gz'])
# un_zip.wait()



# curl -X 'GET' \
#   'https://wikimedia.org/api/rest_v1/metrics/pageviews/top-per-country/US/all-access/2022/11/05' \
#   -H 'accept: application/json'

sort_data = Popen(["sort", "-nr", "-k", "3,3", file_name], stdout=PIPE)
run_awk = Popen(["awk", "-F' '", r'$1 ~ /^en\.m*/ && !($2 ~ /.*:.*/) {print $0}'], stdin=sort_data.stdout, stdout=PIPE)


get_head = Popen(["head", "-10"], stdin=run_awk.stdout, stdout=PIPE)
out, err = get_head.communicate()



df = pd.read_csv(StringIO(out.decode("utf-8")), sep=" ", header=0, names=['domain','article','views','size'])
df = df[~df.article.str.contains(r":")]
df = df[df.article != 'Main_Page']

top_five = df.article.values[:5]
print(top_five)

# Get A months data for top 5 articles

def get_a_months_data(article=None):
	url = f'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/all-agents/{article}/daily/{a_month_ago.strftime("%Y%m%d")}/{yesterday.strftime("%Y%m%d")}'
	r = requests.get(url, allow_redirects=False, headers={'User-Agent': 'reachmujeebhere@gmail.com'})
	df = pd.json_normalize(r.json()["items"])
	return df[['article','timestamp','views']]

all_tables = pd.DataFrame(columns = ['article','timestamp','views'])

for article in top_five:
	df = get_a_months_data(article=article)
	all_tables = pd.concat([all_tables, df])

all_tables.to_csv("all_tables.csv", index=False)






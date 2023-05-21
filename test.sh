wget https://dumps.wikimedia.org/other/pageviews/2022/2022-10/pageviews-20221029-130000.gz
gunzip pageviews-20221029-130000.gz
head pageviews-20221029-130000

sort -nr -k 3,3 pageviews-20221029-130000
awk -F' ' '$1 ~ /^en.m*/ && !($2 ~ /.*:.*/) {print $0}'

curl -X 'GET' \
  'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/all-agents/Charles_Cullen/daily/20221025/20221029' \
  -H 'accept: application/json'
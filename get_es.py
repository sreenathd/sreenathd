import requests

headers = {
    'Content-Type': 'application/json',
}

json_data = { 'query': { 'match_all': {}, }, }

response = requests.get(
    'https://aos-c7ec1282e2ca-gunzs7qzpw4cqz4xbc5bzfwgeu.us-east-1.es.amazonaws.com/customer-rejection-event-caisetl/_search?pretty',
    headers=headers,
    json=json_data,
)
data1 = response.json()
for item in data1['hits']['hits']:
    print(item['_source']['initialCausedBySubmissionId'])

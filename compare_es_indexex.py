import requests

headers = {
    'Content-Type': 'application/json',
}
sub_ids = [13531]
for sub_id in sub_ids:
    json_data = { "query": { "bool": {"must": [ { "match": { "initialCausedBySubmissionId" : sub_id } } ] } }}

    response1 = requests.get(
        'https://aos-c7ec1282e2ca-gunzs7qzpw4cqz4xbc5bzfwgeu.us-east-1.es.amazonaws.com/customer-rejection-event-caisetl/_search?pretty',
        headers=headers,
        json=json_data,
    )

    response2 = requests.get(
        'https://aos-c7ec1282e2ca-gunzs7qzpw4cqz4xbc5bzfwgeu.us-east-1.es.amazonaws.com/customer-rejection-event/_search?pretty',
        headers=headers,
        json=json_data,
    )

    data1 = response1.json()
    data2 = response2.json()

    for item,item2 in zip(data1['hits']['hits'],data2['hits']['hits']):
        print(item['_source'])
        dict1 = item['_source']
        dict2 = item2['_source']
        if len(dict1)!=len(dict2):
            print("Not equal") 
        else:
            flag=0
            for i in dict1:
                if '_id' in i or '_index' in i or 'took' in i:
                    contine
                if dict1.get(i)!=dict2.get(i):
                    flag=1
                    print(i)
                    break
            if flag==0:
                print("Equal")
            else:
                print("Not equal")

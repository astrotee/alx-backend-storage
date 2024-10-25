#!/usr/bin/env python3
"pymongo"
import pymongo


if __name__ == "__main__":
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    total = logs.count_documents({})
    get = logs.count_documents({'method': 'GET'})
    post = logs.count_documents({'method': 'POST'})
    put = logs.count_documents({'method': 'PUT'})
    patch = logs.count_documents({'method': 'PATCH'})
    delete = logs.count_documents({'method': 'DELETE'})
    status = logs.count_documents({'method': 'GET', 'path': '/status'})
    ips = logs.aggregate([
        {'$group': {'_id': '$ip', 'count': {'$sum': 1}}},
        {'$sort': {'count': -1}},
        {'$limit': 10}
    ])

    print(f'''{total} logs
Methods:
\tmethod GET: {get}
\tmethod POST: {post}
\tmethod PUT: {put}
\tmethod PATCH: {patch}
\tmethod DELETE: {delete}
{status} status check''')
    print('IPs:')
    for row in ips:
        print(f"\t{row.get('_id')}: {row.get('count')}")

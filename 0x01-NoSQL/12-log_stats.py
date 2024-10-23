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

    print(f'''{total} logs
Methods:
\tmethod GET: {get}
\tmethod POST: {post}
\tmethod PUT: {put}
\tmethod PATCH: {patch}
\tmethod DELETE: {delete}
{status} status check''')

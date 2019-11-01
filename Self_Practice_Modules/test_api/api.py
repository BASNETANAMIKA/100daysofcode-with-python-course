import requests
from typing import List
import collections

Category_Details = collections.namedtuple("Category_Details","category,id,url,title,description")


def search_keyword(keyword:str) -> List[Category_Details]:
    response = requests.get(f"https://search.talkpython.fm/api/search?q={keyword}")
    print(response.status_code)
    results = response.json()
    entry = []
    for r in results.get('results'):
        entry.append(Category_Details(**r))
    return entry

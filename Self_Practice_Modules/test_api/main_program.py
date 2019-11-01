import api


def main():
    keyword = input("Enter keyword to search with:")
    print(f'searching for keyword {keyword}')
    results = api.search_keyword(keyword)

    print(f'There are {len(results)} results found.')
    for r in results:
        print(f'title: {r.title} falls under category: {r.category}')


if __name__ == '__main__':
    main()

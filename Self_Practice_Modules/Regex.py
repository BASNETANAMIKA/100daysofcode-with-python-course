import re

COURSE = ('Introduction 1 Lecture 01:47'
          'The Basics 4 Lectures 32:03'
          'Getting Technical!  4 Lectures 41:51'
          'Challenge 2 Lectures 27:48'
          'Afterword 1 Lecture 05:02')
TWEET = ('New PyBites article: Module of the Week - Requests-cache '
         'for Repeated API Calls - http://pybit.es/requests-cache.html '
         '#python #APIs')
HTML = ('<p>pybites != greedy</p>'
        '<p>not the same can be said REgarding ...</p>')


def extract_course_times(course=COURSE):
    """Return the course timings from the passed in
       course string. Timings are in mm:ss (minutes:seconds)
       format, so taking COURSE above you would extract:
       ['01:47', '32:03', '41:51', '27:48', '05:02']
       Return this list.
    """
    pat = re.compile(r'\d+:\d+')
    a = pat.findall(course)
    print(a)
    return a

def get_all_hashtags_and_links(tweet=TWEET):
    """Get all hashtags and links from the tweet text
       that is passed into this function. So for TWEET
       above you need to extract the following list:
       ['http://pybit.es/requests-cache.html',
        '#python',
        '#APIs']
       Return this list.
    """
    a = re.findall(r'((?:#|http)\S+)', tweet)
    print(a)
    return a


def match_first_paragraph(html=HTML):
    """Extract the first paragraph of the passed in
       html, so for HTML above this would be:
       'pybites != greedy' (= content of first paragraph).
       Return this string.
    """
    m = re.search('<p>.*?</p>', html)
    print(m.group())
    text = m.group()
    a = re.subn(r'<[/]p?>', '', text)
    print(a[0])
    b = re.subn(r'<p?>', '', a[0])
    print(b[0])
    return b[0]

extract_course_times(COURSE)
get_all_hashtags_and_links(TWEET)
match_first_paragraph(HTML)

import re
from urlparse import urlparse, parse_qs

def check_required(params, required):
    return all(x in params for x in required)

def test1(x):
    path = re.search(r'(?P<path>[^?]*)\?(?P<query>.+)', x)
    return path.group('query') if path and path.lastgroup == "query" else None

def test2(x):
    return parse_qs(urlparse(x).query)

if __name__ == '__main__':
    required = ['a', 'b']
    params = ['a', 'b', 'c']
    print check_required(params, required)

    print test1('/?hoge=1')
    print test2('/?hoge=1')

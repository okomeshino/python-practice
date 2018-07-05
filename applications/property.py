# encoding:utf-8
class PropertyTest(object):

    def url(self):
        return self._url

    def __init__(self, schema, host, url):
        self._url = url
        self.schema = schema
        self.host = host

    # getter
    def get_url(self):
        print('-- get_url --')
        # return self._url
        return '{}://{}/'.format(self.schema, self.host)

    # setter
    def set_url(self, url):
        print('-- set_url --')
        self._url = url

    # deleter
    def del_url(self):
        del self._url

    url = property(get_url, set_url, del_url, 'url Property')


prop = PropertyTest('https', 'www.python-izm.com', 'url')

# プロパティ「url」を取得
print(prop.url)

# setter(set_url)にアクセス
prop.url = 'python-izm'

# getter(get_url)にアクセス
print(prop.url)
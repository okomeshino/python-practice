# encoding:utf-8
import xmlrpc.client

server = xmlrpc.client.ServerProxy('http://b.hatena.ne.jp/xmlrpc')
print(server.bookmark.getCount('http://www.python-izm.com/'))
print(server.bookmark.getTotalCount('http://www.python-izm.com/'))

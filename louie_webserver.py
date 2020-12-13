from twisted.web import server, resource
from twisted.internet import reactor

from louie_ipsum import LouieIpsum

class LouieIpsumSite(resource.Resource):

    isLeaf = True

    def __init__(self):
        super().__init__()
        self.louie_ipsum = LouieIpsum()

    def render_GET(self, request):
          kw = request.args.get(b'kw')
          if kw and len(kw[0]) > 0:
              keyword = kw[0].decode('utf-8')
              louie_text = self.louie_ipsum.get(keyword=keyword)
              louie_text = '' if not louie_text else louie_text
          else:    
              louie_text = self.louie_ipsum.get()
          request.setResponseCode(200)
          request.setHeader('Content-Type', 'text/html')
          response_bytes = "\r\n".join([
              f"<p>{louie_text}</p>\r\n",
              '<form action="/" method="get">',
              '<input type="text" name="kw" />',
              '<input type="submit" />',
              '</form>'
          ]).encode('utf-8')
          return response_bytes

site = server.Site(LouieIpsumSite())
reactor.listenTCP(8000, site)
reactor.run()
        

# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:

        def get_hostname(url):
            # split url by slashes
            # for instance, "http://example.org/foo/bar" will be split into
            # "http:", "", "example.org", "foo", "bar"
            # the hostname is the 2-nd (0-indexed) element
            return url.split('/')[2]
        
        start_hostname = get_hostname(startUrl)
        visited = set()

        def dfs(url):
            visited.add(url)

            for next_url in htmlParser.getUrls(url):
                next_url_host_name = get_hostname(next_url)
                if next_url_host_name == start_hostname and next_url not in visited:
                    dfs(next_url)

        dfs(startUrl)

        return visited

        
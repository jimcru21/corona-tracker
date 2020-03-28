from django.contrib.sitemaps import Sitemap
import requests
from django.shortcuts import reverse

from corona.views import country_stat

api_url_base = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/"
headers = {
    'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
    'x-rapidapi-key': "23a2def8fbmshf7ae7a8212cce73p1bbd6ejsn5712b6b8672b"
}


class StaticViewSitemap(Sitemap):
    def items(self):
        return ['index']

    def location(self, item):
        return reverse(item)


class CountryStat(Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        api_url = '{0}cases_by_country.php'.format(api_url_base)
        response = requests.get(api_url, headers=headers)
        corona = response.json()
        urlcorona = corona['countries_stat']
        return urlcorona

    def location(self, items):
        url = '/' + 'country_stat' + '/' + str(items['country_name'])
        return url

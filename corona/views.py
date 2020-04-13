from django.shortcuts import render
import requests
import country_converter as coco
from django.core.cache import cache

# Create your views here.
from django.template import RequestContext
from django.views.decorators.cache import cache_page

api_url_base = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/"
headers = {
    'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
    'x-rapidapi-key': "23a2def8fbmshf7ae7a8212cce73p1bbd6ejsn5712b6b8672b"
}


def index(request):
    api_url = '{0}cases_by_country.php'.format(api_url_base)
    response = requests.get(api_url, headers=headers)
    corona = response.json()
    top20 = corona['countries_stat'][:10]

    api_url = '{0}worldstat.php'.format(api_url_base)
    response = requests.get(api_url, headers=headers)
    world_totals = response.json()

    context = {
        'corona': corona['countries_stat'][1:],
        'world_totals': world_totals,
        "top20": top20,
    }
    return render(request, 'corona/index.html', context)


def country_stat(request, pk):
    api_url = '{0}worldstat.php'.format(api_url_base)
    response = requests.get(api_url, headers=headers)
    world_totals = response.json()

    api_url = '{0}cases_by_particular_country.php'.format(api_url_base)
    querystring = {"country": "{}".format(pk)}
    response = requests.get(api_url, headers=headers, params=querystring)
    corona = response.json()
    country_stats = corona['stat_by_country']

    api_url = '{0}latest_stat_by_country.php'.format(api_url_base)
    querystring = {"country": "{}".format(pk)}
    response = requests.get(api_url, headers=headers, params=querystring)
    corona = response.json()
    country_stats1 = corona['latest_stat_by_country']

    context = {
        'world_totals': world_totals,
        'country_name': querystring,
        'country': country_stats,
        'country_latest1': country_stats1,
    }

    return render(request, 'corona/country_stat.html', context)

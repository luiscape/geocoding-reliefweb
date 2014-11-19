## Script to geocode ReliefWeb data
## to a sub-national level.

import geograpy as geo
import csv
import os
import requests as r
import pandas as pd

# base url
def getRwData(limit):

	# building the query
	base_url = 'http://api.rwlabs.org/v1/reports?profile=full'
	limit_url = '&limit=' + str(limit)
	query_url = base_url + limit_url

	# making the query
	doc = r.get(query_url)

	# storing the data in a data.frame

	# returning test output
	return doc.json()["data"][0]["fields"]["body"]


def findLocations(corpus):

	# parsing corpus with geograpy
	places = geo.get_place_context(text=corpus)

	# extracting locations
	print places.countries
	print places.regions
	print places.cities
	print places.other


findLocations(getRwData(1))

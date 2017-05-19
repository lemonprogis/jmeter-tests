import csv

links = ['/',
'/pages/biennial-review',
'/pages/change-management-reports',
'/pages/modeling-reports',
'/pages/operations-reports',
'/pages/pending-hub-changes',
'/pages/regulation-performance-by-mp',
'/pages/da-binding-constraints',
'/pages/congestion-by-constraint',
'/pages/da-lmp-by-bus',
'/pages/da-lmp-by-location',
'/pages/da-mcp',
'/pages/market-clearing',
'/pages/virtual-clearing-by-moa',
'/pages/virtual-reference-prices',
'/pages/rtbm-binding-constraints',
'/pages/fuel-on-margin',
'/pages/rtbm-lmp-by-bus',
'/pages/rtbm-lmp-by-location',
'/pages/rtbm-mcp',
'/pages/operating-reserves',
'/pages/allocations',
'/pages/ffe-on-m2m-flowgates',
'/pages/m2m-flowgate-list',
'/pages/energy',
'/pages/or',
'/pages/regdn',
'/pages/regup',
'/pages/headroom-and-floorroom',
'/pages/historical-offers',
'/pages/ramp-sharing',
'/pages/capacity-of-generation-on-outage',
'/pages/daily-metrics',
'/pages/day-ahead-wind-forecast',
'/pages/generation-mix-historical',
'/pages/hourly-load',
'/pages/mtlf-vs-actual',
'/pages/resource-forecast-by-reserve-zone',
'/pages/stlf-vs-actual',
'/pages/short-term-wind-forecast',
'/pages/tie-flow-historical',
'/pages/calendars',
'/pages/reports',
'/pages/daily-funding-by-constraint',
'/pages/electrically-equivalent-settlement-locations',
'/pages/faq',
'/pages/monthly-funding-by-constraint',
'/pages/reference-prices',
'/pages/tcr-allocation-historical-results',
'/pages/tcr-auction-historical-results',
'/pages/tcr-calendar',
'/pages/tcr-product-period-hours',
'/pages/ace-chart',
'/pages/forecast-vs-actual',
'/pages/generation-mix',
'/pages/generation-mix-rolling-365',
'/pages/generation-mix-ytd',
'/pages/hub-and-interface-prices',
'/pages/interchange-trend',
'/pages/market-monitoring-data-depository',
'/pages/your-certificate-information',
'/login',
'/terms-of-use',
'/sitemap'
]


def gen_csv(url_links):
	data = []
	for i, link in enumerate(url_links):
		item = {'index': i, 'uri': link}
		data.append(item)

	keys = data[0].keys()

	with open('links.csv', 'wb') as output_file:
		dw = csv.DictWriter(output_file, keys)
		#dw.writeheader()
		dw.writerows(data)


if __name__ == '__main__':
	gen_csv(links)
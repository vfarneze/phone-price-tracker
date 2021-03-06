from datetime import datetime
import os

class Params:
	"""
	Parameters for the jacotei extraction pipeline.
	"""
	#
	raw_data = '../data_storage/raw/jctraw' + datetime.now().strftime("%Y-%m-%d") + '.csv'
	trans_data = '../data_storage/transformed/jcttreated' + datetime.now().strftime("%Y-%m-%d") + '.csv'
	temp_data = '../data_storage/temp/toDB' + datetime.now().strftime("%Y-%m-%d") + '.csv'

	## Database connection params
	user = 'postgres'
	password = '123qweasd'
	host = 'localhost'
	database = 'Smartphones-DB'
	table_name = 'jacotei'
	#table_name='jct' + datetime.now().strftime("%Y-%m-%d")

	#Info specific about webscrapping
	force_execution = False

	# parameters for data_extraction
	page = 1
	page_limit=4
	number_per_page=2500
	url = 'https://www.jacotei.com.br/busca/?cids=57&bids=&fids=&o=2&p='
	#url = 'https://www.jacotei.com.br/busca/?cids=57&bids=&fids=&o=2' +  f'&p={page}' + f'&n={number_per_page}'
	#url = 'https://www.jacotei.com.br/busca/?cids=57&bids=&fids=&o=2&p=1&n=2500'

	#parameters for data_storage
	prefix=r'jct_data_'

	#time params
	t = datetime.now()
	year = f'{t.year}' 
	month = (lambda x: '0' + x if len(x) == 1 else x)(f'{t.month}')
	day = (lambda x: '0' + x if len(x) == 1 else x)(f'{t.day}')
	
	# YYYY-MM-DD
	timestamp = year + '-' + month + '-' + day
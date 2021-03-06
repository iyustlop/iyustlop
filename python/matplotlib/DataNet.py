import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates

def bytespdate2num(fmt,encoding='utf-8'):
	strconverter = mdates.strpdate2num(fmt)
	def bytesconverter(b):
		s = b.decode(encoding)
		return strconverter(s)
	return bytesconverter
	

def graph_data(stock):
	
	stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'
	source_code = urlib.request.urlopen(stock_price_url).read().decode()

	stock_data = []
	split_source = source_code.split('\n')

	for line in split_source:
		split_line = line.split(',')
		if len(split_line) == 6:
			if 'values' not in line and 'labels' not in line:
				stock_data.append(line)
	
	date,closep,highp,lowp,openp,volume = np.loadtxt(stock_data,
							delimeter=',',
							unpack=True,
							converters={0: bytespdate2num('%Y%m%d')}
							)

	plt.plot_date(date, closep)
	plt.xlabel('date')
	plt.ylabel('price')
	plt.title('Repositioner Demand\n Position')
	plt.legend()
	plt.show()


graph_data('TSLA')

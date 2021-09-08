import streamlit as st
import plotly.figure_factory as ff
import pandas as pd
#import matplotlib.pyplot as plt 
import requests	
from bokeh.plotting import figure
from bokeh.models import DatetimeTickFormatter

ticker = st.sidebar.text_input("Please enter a ticker symbol","").upper()
start_date = st.sidebar.text_input("Please enter a start date","2021-01-01")
end_date = st.sidebar.text_input("Please enter an end date","2021-03-01")

api = '7LWQX624YP1KQI3S'

r4 = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&outputsize=full&output_format=json&symbol=GOOG&apikey=api')
json_to_read = r4.json()

#st.write(api)

if ticker: 
	json_to_list = []
	for key, value in json_to_read.items():
	    json_to_list.append([key, value])
	    
	#len(json_to_list)



	df_from_json = pd.DataFrame.from_dict(json_to_list[1][1], orient = 'index')

	df_from_json = df_from_json[(df_from_json.index > start_date) & (df_from_json.index <= end_date)].sort_index(ascending=True)


	for column in df_from_json.columns:
	    df_from_json[column] = df_from_json[column].astype(float)
	#df_from_json['5. adjusted close'] = df_from_json['5. adjusted close'].astype(float)

	df_from_json.index = pd.to_datetime(df_from_json.index)

	#fig, ax = plt.subplots(figsize=(10, 10))

	#st.write(df_from_json)

	# Add x-axis and y-axis
	#ax.plot(df_from_json['5. adjusted close'])

	# Set title and labels for axes

	#plt.show()



	x = df_from_json.index
	y = df_from_json['5. adjusted close']
	p = figure(title='Adjusted Closing Price',
		x_axis_label='Time',
		x_axis_type = 'datetime')

	p.title.align = 'center'
	p.title.text_font_size = '1.5em'

	p.xaxis.axis_label_text_font_style = "normal"
	p.xaxis.axis_label_text_font_size = "1em"


	p.line(x, y, line_width=2)

	st.bokeh_chart(p, use_container_width=True)

	#st.write(type(df_from_json.index[2]))
	p.xaxis.formatter=DatetimeTickFormatter(
	        hours=["%d %B %Y"],
	        days=["%d %B %Y"],
	        months=["%d %B %Y"],
	        years=["%d %B %Y"])
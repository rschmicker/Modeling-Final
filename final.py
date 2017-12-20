#!/usr/bin/env python
import math
import plotly
import plotly.graph_objs as go

quan = 865
ys = []
prices = []

for i in range(10):
	prices.append(i * ((5000/quan) - i))
	ys.append(i)

hawks = go.Scatter(
	x = prices,
	y = ys,
	#mode = 'markers',
)

data = [hawks]

plot_url = plotly.offline.plot(data, filename='basic-line.html')

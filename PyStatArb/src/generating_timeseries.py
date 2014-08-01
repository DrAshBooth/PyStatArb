import numpy as np


def gaussian_white_noise(n, mu, sigma):
	return np.random.normal(mu, sigma, n)

def moving_average(n, mu, sigma, beta):
	wn = gaussian_white_noise(n+1, mu, sigma)
	ma = wn[1:] + beta*wn[:-1]
	return ma

if __name__ == "__main__":
	import matplotlib.pyplot as plt
	import pandas as pd
	
	ts = pd.Series(moving_average(100,0,0.5,0.8), index=pd.date_range('1/1/2000', periods=100))
	
	ts.plot()
	
	plt.show()
	

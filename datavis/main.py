import matplotlib.pyplot as pyplot

years = [ 1950, 1955 ,1960 ,1965 ,1970 ,1975 ,1980 ,1985 ,1990 ,1995 ,2000 ,2005 ,2010 ,2015  ]
pops =  [ 2525, 2758, 3018, 3322, 3682, 4061, 4440, 4853, 5310, 5735, 6127, 6520, 6930, 7349]


pyplot.plot(years, pops, color=(1, 0.3, 0.3))

pyplot.ylabel("Population in millions")
pyplot.xlabel("Years")
pyplot.title("Population growth")

pyplot.show()
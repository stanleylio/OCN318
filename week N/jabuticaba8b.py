# More plotting
#
# You'd better know how to use a list.
#
# Reading (optional):
#   filter()
#       https://docs.python.org/3/library/functions.html#filter
#   lambda:
#       https://www.python-course.eu/lambda.php
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18




# this is how you fetch a file from the internet
#import requests
#url = 'https://www.ncei.noaa.gov/data/global-hourly/access/2017/02020099999.csv'
#lines = requests.get(url).text.split('\n')
#print('{} rows, {} columns (variables)'.format(len(lines), len(lines[0])))

# or if you don't want to hammer NOAA's server
lines = open('02020099999.csv').readlines()


import csv
f = open('02020099999.csv', newline='')
reader = csv.reader(f, delimiter=',', quotechar='"')
lines = list(reader)
f.close()
# now "lines" is a LIST of LISTs, each containing the fields in a row


# extract the 11th item of every row in "lines"
wind = []
for line in lines[1:]:      # (starts from the second line)
    wind.append(line[10])   # again, index starts from 0
# now "wind" contains the 11th column in a list of STRINGs


# extract the 4th item in that column - "looks like wind speed"
V = []
for r in wind:
    V.append(float(r.split(',')[3]))
# now "V" is a list of wind speed readings


import matplotlib.pyplot as plt
plt.figure()
plt.plot(V, 'r.')
plt.show()
# what does the data mean? I have no idea. Go look it up if you are interested.
# https://www.ncdc.noaa.gov/data-access/quick-links#loc-clim


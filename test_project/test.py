from urllib.request import urlopen

# write in
url = 'http://aima.cs.berkeley.edu/data/iris.csv'
u = urlopen(url)
content = u.read()
localFile = open('iris.csv', 'wb')
localFile.write(content)
localFile.close()


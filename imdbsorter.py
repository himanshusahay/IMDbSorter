# IMDB Sorter
# Written By: Himanshu Sahay


import requests
import csv
import json
import operator

# There are 2 modes to view program output - CONDENSED MODE and DENSE MODE.
# In condensed mode, only the sorted movie titles and ratings are shown.
# In dense mode, the file entries are shown as they are read in from the file, along with a counter of the entry number.
# To turn on condensed mode, simply changed the value of the variable 'condensedMode' to True.
# DEFAULT: DENSE MODE
condensedMode = False

# List of dictinaries to store movies when reading from CSV file
listMovies = []
notFoundRatings = []

# To track index number of movie while reading file in dense mode
count = 0

# Reading from movies.csv 
if condensedMode == False:
	print "\nOUTPUT MODE: DENSE\n"
	print "Reading movie titles from file: \n"

with open('movies.csv', 'rb') as csvfile:
	imdbReader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in imdbReader:
	
		count+= 1
		if condensedMode == False:
		# Print the entry number of the movie in the csv file
			print "Num: "+str(count)
		# Printing movie title and year
			print ' '.join(row)
		row0Decoded = row[0].decode('utf-8')
		row1Decoded = row[1].decode('utf-8')

		# Store movie title and year to be used as a kay in the dictionary
		title_year = row0Decoded+', '+row1Decoded
		
		row[0] = "+".join( row[0].split() )
		url = "http://www.omdbapi.com/?"
		# Querying the OMDb API by title and year with result in JSON format
		url+= "t="
		url+=''+row[0]
		url+='&y='+row[1]+'&plot=short&r=json'
		# Printing URL for debugging purposes only
		# print url

		# No API key required
		endpoint = url
		response = requests.get(url)

		data = json.loads(response.content)

		# Edge case - example - All That Money Can Buy 1941 does not exist in the OMDb API database
		# Solution - Look for IMDB rating only if 'Response' != 'False' 
		if data['Response'] != 'False':
			imdbRating = data['imdbRating']
			if condensedMode == False:
				print "Rating: "+imdbRating+"\n"

			if imdbRating == 'N/A':
				notFoundRatings.append({'movie': title_year, 'rating': imdbRating})

			else: 
				listMovies.append({'movie': title_year, 'rating': imdbRating})

		else:
			# print "Rating not found in the OMDb API database"
			# !Edge case!
			# dictionary[title_year] = -1 
			# Append to list of movies as invalid entry
			imdbRating = 'Error - entry does not exist'
			if condensedMode == False:
				print "Rating: "+imdbRating+"\n"
			notFoundRatings.append({'movie': title_year, 'rating': imdbRating})

# Sorting the list of movies with valid ratings in descending order of rating
listMovies.sort(key=operator.itemgetter('rating'), reverse=True)
# Sorting the invalid ratings in ascending order of movie name
notFoundRatings.sort(key=operator.itemgetter('movie'))

if condensedMode == False:
	print "--------------------------------------------"

print '\nOutput has been stored to file "movies_sorted.html" in the same directory as this program file'
print "\n--------------------------------------------"

# Opening new html file to write results to
f = open("movies_sorted.html", mode = 'wb')

# Counters for movie titles in both lists
lCount = 0
naCount = 0

# Writing results to html page

f.write('''<!DOCTYPE html>
<html lang="en">

<head>
	<head>
    <title>IMDb Sorter</title>
    <!-- Meta -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
	<!-- Global CSS -->
    <link rel="stylesheet" href="bootstrap/css/bootstrap.min.css"> 
    
</head>

<body>
''')

f.write('''
<div class = "container">
	<div class ="jumbotron">
	<h1>IMDb Sorter</h1></div>
	<h2>List of movies sorted by their IMDb ratings, in descending order: </h2>
		<ol class="list-group">
''')

for movie in listMovies:
	lCount+= 1
	l = str(lCount)
	text = '<li class="list-group-item">('+l+') Movie: '+movie['movie']+' | Rating: '+movie['rating']+'</li>'
	f.write(text.encode('utf-8'))

f.write('</ol>')

f.write('<h1>List of movies with N/A ratings or entries that do not exist, sorted by movie title: </h2>')
f.write('<ol class="list-group">')
# print "\nList of movies with N/A ratings or entries that do not exist, sorted by movie title: \n"
for movie in notFoundRatings:
	naCount+= 1
	na = str(naCount)
	text = '<li class="list-group-item">('+na+') Movie: '+movie['movie']+' | Rating: '+movie['rating']+'</li>'
	
	f.write(text.encode('utf-8'))

f.write('</ol>')
f.write('</div>')
f.write('</body>')

f.close()


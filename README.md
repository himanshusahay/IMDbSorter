# IMDb Sorter

IMDb Sorter reads in a list of movies from a file and sorts them in descending order of their IMDb ratings. The result is stored in a new <code>movies_sorted.html</code> file.

### Output Format
* Modes to view program output - CONDENSED MODE and DENSE MODE.
    * In CONDENSED MODE, only the sorted movie titles and ratings are shown.
    * In DENSE MODE, the file entries are shown as they are read in from the file, along with a counter of the entry number.
    * To turn on CONDENSED MODE, simply changed the value of the variable *condensedMode* to *True*.
    * DEFAULT: DENSE MODE

### Under the Hood
```
Python 2.7.9
```

Modules: <code>requests, csv, json, operator, os</code>


***

## Developer's Notes

>Here’s to the crazy ones. The misfits. The rebels. The troublemakers. The round pegs in the square holes. The ones who see things differently. They’re not fond of rules. And they have no respect for the status quo. You can quote them, disagree with them, glorify or vilify them. About the only thing you can’t do is ignore them. Because they change things. They push the human race forward. And while some may see them as the crazy ones, we see genius. Because the people who are crazy enough to think they can change the world, are the ones who do.

*Steve Jobs/Apple*

I decided to write IMDb Sorter in Python because I've never used Python before and figured this was a great opportunity to learn Python by building something cool using it. Python also has an advantage over JavaScript (my earlier choice) in handling requests between the client and server.

To familiarize myself with Python syntax, I completed the [NPR API tutorial](http://www.codecademy.com/en/tracks/npr) on [Codeacademy](http://codeacademy.com).

Then, aided by [StackOverflow](http://stackoverflow.com/) and the extensive [Python documentation](https://docs.python.org/2.7/), I wrote this program.


****

*Himanshu Sahay* 

*[wpi.edu/~hsahay](http:/www.wpi.edu/~hsahay)*
class MovieNode:
	def __init__(self, movieName, relDate):
		self.movieName = movieName
		self.relDate = relDate
		self.next = None
		return

class NetflixMovieList:
	def __init__(self):
		self.head = None

	def addMovie(self, movieName, relDate):
		new = MovieNode(movieName, relDate)
		if self.head == None:
			self.head = new
			return
			
		new.next = self.head
		self.head = new
		return

	def displayMovies(self):
		if self.head == None:
			print("No movies to show right now")
			return
		
		temp = self.head

		while(temp != None):
			print(temp.movieName, temp.relDate, '->', end = "")
			temp = temp.next
		print('None')
		return
		
	def deleteMovie(self):
		if self.head == None: # Case when the linked list is empty
			print("No movies to delete anymore")
			return
		
		temp = self.head
		prev = temp 
		
		while(temp != None): # Iterating through the linked list
				
			if temp.next != None: # If the current element is not the last element
				temp1 = temp.next # Assigning the next element of the current element
				if temp1.next == None: # Checking if the next element of current element is last
			    		prev = temp # prev will hold the element previous to the last element
			    	
			if(temp.next == None): # Checking if the element is the last element
				del temp
				prev.next = None # Assigning none to the next variable of the previous element
				break
			else:
			    	temp = temp.next
			    
		return
			
movie_list = NetflixMovieList()
movie_list.addMovie('Iron Man', '12th June 2010')
movie_list.addMovie('Thor', '15th July 2010')
movie_list.addMovie('Batman', '29th August 2010')
movie_list.displayMovies()
movie_list.deleteMovie()
movie_list.displayMovies()

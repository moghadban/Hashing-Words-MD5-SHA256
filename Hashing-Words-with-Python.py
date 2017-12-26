''' 
	Name: Mojahed Ghadban
	Hashing Words with Python
	Description:  This Python script will take in a list of words, compute their MD5 and SHA256 hash values, return two dictionaries, and will execute the word along its corresponding hashes.
	A module to calculate the MD5 and SHA256 values of a list of words will be named calcHashFunc, and the main function will prompt user for words to be hashed, once input is received,
	the word list is passed to calcHashFunc. The returned dictionaries are to be printed out in this function.
	Usage: python.exe Hashing-Words-with-Python.py
'''
#Importing library for hash and message digest algorithms
import hashlib


#Function calcHashFunc	
def calcHashFunc(wordList):
	'''Function that takes in a list of words and return two dictionaries: md5Dict and sha256Dict, containing the word and it’s corresponding hash value.'''
	md5Dict = {}					#Initializing an empty dictionary to store md5 hash values
	sha256Dict = {}					#Initializing an empty dictionary to store sha256 hash values
	#Loop through list, find md5 / sha256 hash values, store them in dictionaries md5Dict / sha256Dict, do necessary encoding, return dictionaries md5Dict / sha256Dict
	for x in wordList:
		md5Dict[x] = hashlib.md5(str(x).encode('utf-8')).hexdigest()            #processing each word 'x' and calculating its md5 hash value to dictionary 'md5Dict'
		#NOTICE: string is encoded to 'utf-8', its hexidecimal value is parsed, & stored value with its key.
		sha256Dict[x] = hashlib.sha256(str(x).encode('utf-8')).hexdigest()      #processing each word 'x' and calculating its sha256 hash value to dictionary 'sha256Dict'
		#NOTICE: string is encoded to 'utf-8', its hexidecimal value is parsed, & stored value with its key.
	
	return md5Dict,sha256Dict	#returning both dictionaries back to the main function.
    


#Main function
if __name__ == '__main__':
	'''main function will prompt user for words to be hashed, once input is received, the word list is passed to calcHashFunc.
        The returned dictionaries are to be printed out in this function.'''
	print("\n\n\t\t\t ======PROGRAME INFORMATION======\n")
	print("\t\t\t\t Name: Mojahed Ghadban")
	print("\t\t\t   Hashing Words with Python .")
	print("\t\tDescription: Finding md5/sha256 hash values of list of words")
	print("\t\t\t     Usage: python.exe Hashing-Words-with-Python.py\n\n")

	repeat = 'Y'								#Initializing 'repeat' as the letter 'Y' to sgore user repetition for another word.
	list1 = []								#Initializing list to store user's input(s) of list of words
	print("\n\n\n\t\t\t ========PROGRAME INPUT=========\n")
	while repeat == 'Y' or repeat == 'y':		#Loop as long as user response is "y" or "Y",
		userIn = input(" Please enter a word to be hashed: ")	                #User is prompted to enter a word to be hashed.
		list1.append(str(userIn))				                #Adding the user's input as a string and appending the list, list1
		repeat = input(" Would you like to process another word? (Y/N): ")	#Asking the user again to process another word by "y" or "Y" response
	
	md5ValDict, sha256ValDict = calcHashFunc(list1) 	#md5ValDict and sha256ValDict are set to call calcHashFunc function and to pass string list1
								#calcHashFunc function will return TWO different dictionaries.

print("\n\n\n\n\n\t\t\t ========PROGRAME OUTPUT========")
print("\n - Word:md5 %s \n - Word:sha256 %s" %(md5ValDict, sha256ValDict))  #Displaying the word along its corresponding hashes
print("\n\n\t\t\t ========END OF PROGRAME========")

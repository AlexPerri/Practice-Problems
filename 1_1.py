# Check if a string has all unique characters without using any other data structures

def unique(string) :
	temp = {}
	for x in string :
		if temp.__contains__(x) :
			print("Repeating characters")
			return False
		temp[x] = [x]
	print("No repeating characters")
	return True

def main() :

	print("This function checks for repeating characters")
	unique(input("Input a word or sentence"))
	input("Press Enter to close")

if __name__ == "__main__" :
	main()

# Take a sentence and replace all spaces with "%20"

def makeUrl(string) :
	print(string.replace(" ", "%20"))

def main() :

	makeUrl(input("Enter a sentence\n"))
	input("Press Enter to close")

if __name__ == "__main__" :
	main()


# Check if a string is a palandrome permutation
# Amount of reocurring chars must be all even or only 1 odd (space not included)

def palPerm(string) :
	count = {}
	for x in string :
		if x == ' ' :
			continue
		if x in count :
			count[x] += 1
		else :
			count[x] = 1
	odd = False
	for x in count :
		if count[x]%2 == 1 and odd == False :
			odd = True
		elif count[x]%2 == 1 and odd == True:
			print("Not a palandrome permutation")
			return False
	print("Is a palandrome  permutation")
	return True

def main() :

	palPerm(input("Enter a sentence\n"))
	input("Press Enter to close")

if __name__ == "__main__" :
	main()


import sys

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

file = sys.argv[1]

def get_book_text(book):
	x = ""
	with open(book) as story:
		x = story.read()
	return x

def main():
	x = "char"
	y = "num"
	text = get_book_text(file)
	from stats import get_word_count
	word_count = get_word_count(text)
	from stats import get_letter_counts
	letter_counts = get_letter_counts(text)
	from stats import sort_letter_list
	sorted_list = sort_letter_list(letter_counts)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {file}")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")
	for list in sorted_list:
		if list[x].isalpha():
			print(f"{list[x]}: {list[y]}")
	print("============= END ===============")

main()


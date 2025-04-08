import sys
from stats import (
  get_word_count,
  get_char_count,
  sort_char_count,
)

def get_book_text(path):
  with open(path) as f:
    return f.read()

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  book_path = sys.argv[1]

  book_text = get_book_text(book_path)
  word_count = get_word_count(book_text)
  char_count = ""
  for d in sort_char_count(get_char_count(book_text)):
      if d['char'].isalpha():
        char_count += f"{d['char']}: {d['count']}\n"

  report = f"""
============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
{char_count}
============= END ==============="""
  print(report)

main()

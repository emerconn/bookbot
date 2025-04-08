def get_word_count(text):
  return(len(text.split()))

def get_char_count(text):
  d = {}
  for char in text:
    if char.lower() in d:
      d[char.lower()] += 1
    else:
      d[char.lower()] = 1
  return d

def sort_char_count(chars):
  l = []
  for k, v in chars.items():
    l.append({"char": k, "count": v})
  return sorted(l, reverse=True, key=lambda d: d["count"])

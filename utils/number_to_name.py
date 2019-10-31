digits = [
  "zero",
  "one",
  "two",
  "three",
  "four",
  "five",
  "six",
  "seven",
  "eight",
  "nine"
]

emojis = [
  '0⃣',
  '1⃣',
  '2⃣',
  '3⃣',
  '4⃣',
  '5⃣',
  '6⃣',
  '7⃣',
  '8⃣'
]

def number_to_name(number):
  if number <= len(digits):
    return digits[number]

def number_to_emoji(number):
  if number <= len(emojis):
    return emojis[number]
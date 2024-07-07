# https://codeforces.com/problemset/problem/71/A
def abbreviate_word(word):
  if len(word) <= 10:
    return word 
  else:
    middle_length = len(word) - 2 
    return f"{word[0]}{middle_length}{word[-1]}"  

def main():
  num_words = int(input())

  for _ in range(num_words):
    word = input()
    abbreviated_word = abbreviate_word(word)
    print(abbreviated_word)

if __name__ == "__main__":
  main()


longest5words = []

with open('/usr/share/dict/words', 'r') as f:
    longest5words = f.read().splitlines()

longest5words.sort(key = len, reverse = True) #sorts based on the length, longest to shortest
for x in range(5):
    print(longest5words[x])
  #  print(longest5words[x])  #tests of the words were properly converted

   

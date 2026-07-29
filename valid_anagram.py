#words1=input("Enter the word1")
#words2=input("Enter the word2")
#if len(words1)!=len(words2):
 #   print("Not Anagram")
#else:
 #   for ch in words1:
  #      if words1.count(ch)!=words2.count(ch):
   #         print("Not Anagram")
    #        break
   # else:
    #    print("Anagram")
    
def isAnagram(word1,word2):
    return sorted(word1)==sorted(word2)

word1="anagram"
word2="nagaram"
print(isAnagram(word1,word2))
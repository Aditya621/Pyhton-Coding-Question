string = input("Enter a String :")
vowels = 0  
consonants = 0 
for i in string:  
  if i in ('a','e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'):  #if character in string is vowel
      vowels+=1 
  elif i.isalpha():  
      consonants+=1  #if consonant increment variable ‘consonants’ with one
print("Vowels :",vowels,"Consonants:",consonants)
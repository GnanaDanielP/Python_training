variable=input("enter the word:")
count=0
for vowels in variable:
   if vowels in 'aeiouAEIOU':
     count=count+1
print("number of vowels:",count) 
count_1=0
for consonats in variable:
       if consonats not in 'aeiouAEIOU':
         count_1=count_1+1
print("consonants:",count_1)

   
          

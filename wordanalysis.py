#
# File: wordanalysis.py
# Author: Yeabsira Bizualem
#
# Created: 10/10/22
# Modified: 10/10/22

infile = open("crosswords.txt","r")
word_list = []
for line in infile:
    word = line[:len(line)-1]
    word_list.append(word)
infile.close()

#Words with more than 20 letters.
for line in word_list:
    if len(line) > 20:
        print(line)

#Palindromes
def isPalindrome(word):
    i = 0
    while i < (len(word)-1)/2:
        if word[i]!= word[len(word)-1-i]:
            return False
        i+=1
    return True
count = 0
for word in word_list:
    if isPalindrome(word):
        count+=1
print("In the official list of 113,809 crosswords, there are",count,"palindromes.")

shortestPalindrome = ''
for word in word_list:
    if isPalindrome(word):
        if shortestPalindrome == '' or len(word) < len(shortestPalindrome):
            shortestPalindrome = word
print("The shortest palindrome is",shortestPalindrome)

longestPalindrome = ''
for word in word_list:
    if isPalindrome(word):
        if longestPalindrome == '' or len(word) > len(longestPalindrome):
            longestPalindrome = word
print("The longest palindrome is",longestPalindrome)

#Words without ‘e’
without_e = 0
shortest_without_e = ''
longest_without_e = ''
for word in word_list:
    if not 'e' in word:
        without_e +=1
        if longest_without_e == '' or len(word) > len(longest_without_e):
                longest_without_e = word
        if shortest_without_e == '' or len(word) < len(shortest_without_e):
                shortest_without_e = word
print("In the official list of 113,809 crosswords, there are",without_e,"words that do not have 'e'.")      
print("The shortest such word is",shortest_without_e," and the longest such word is",longest_without_e)

#The most frequently-used first letter

alpha_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

count_list = [0]*26

for word in word_list:
    first_letter = word[0]
    index = alpha_list.index( first_letter)
    count_list[index]= count_list[index]+1
n=0
max_count = 0
max_letter = ''
while n < 26:
    print(count_list[n],"words begin with "+"'"+alpha_list[n]+"'")
    if count_list[n]> max_count:
        max_count = count_list[n]
        max_letter = alpha_list[n]
    n+=1
        
print("and"+"'"+max_letter+"'"+"is the most frequently-used first letter.")

#The most frequently-used letter
frequency_list = [0]*26
for word in word_list:
    for char in alpha_list:
        if char in word:
            frequency_list[ord(char)-97]+= 1
t = 0
r = 0
freq_count = 0
freq_letter=''
while t < 26 :
    print(frequency_list[t],"words use"+"'"+alpha_list[t]+"'")
    if frequency_list[t]> freq_count:
        freq_count = frequency_list[t]
        freq_letter = alpha_list[t]
    t+=1
print("and","'"+freq_letter+"'"+" is the most frequently-used letter.")
    
            
    
    
    
    
    
    


   

#regular language detector 
# from langdetect import detect

# print(detect("this is language detection"))

# print(detect("hii ni nini"))

# checks confidence 
from langdetect import detect_langs

print(detect_langs("This is language detection "))
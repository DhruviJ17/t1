from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text1 = input("Enter first string: ").lower()
text2 = input("Enter second string: ").lower()

# tokenization
text1_list = word_tokenize(text1)
text2_list = word_tokenize(text2)

Stopwords = stopwords.words('english')
list1 = []
list2 = []

# remove stop words from text
text1_set = {i for i in text1_list if not i in Stopwords}
text2_set = {i for i in text2_list if not i in Stopwords}

# combine both and create vector
both = text1_set.union(text2_set)
for i in both:
    if i in text1_set:
        list1.append(1)
    else:
        list1.append(0)
    if i in text2_set:
        list2.append(1)
    else:
        list2.append(0)

a = 0
# by applying cosine formula
for i in range(len(both)):
    a += list1[i] * list2[i]
cos = (a / float((sum(list1) * sum(list2)) ** 0.5))*100
print("similarity between the texts is : ", cos)

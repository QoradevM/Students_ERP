# import random
#
# son = random.randint(1, 100)
# count = 0
#
# while count < 10:
#     txt = int(input("Kiriting: "))
#     count += 1
#
#     if txt != son:
#         if txt > son:
#             print(f"Kichikroq kiriting")
#         elif txt < son:
#             print("Kattaroq kiriting!")
#     else:
#         print("Topdingiz!")
#         print("Yana oynamoqchimisiz y/n")
#         sw = input("Tanloni kiriting: ")
#
#         if sw == 'n':
#             break
#
# print(f"Tugadi\nComputer tanladi: {son}")
# import random
#
# box = ['Naski','Telefon','12 varoqli daftar',"O'chir'gich",'Qalam','Calendar']
#
#
# while True:
#     txt1 = int(input("1,5 gacha son tanlang: "))
#     if txt1 <= 5:
#         txt = random.sample(box,txt1)
#         for user in txt:
#             print(txt)
#     else:
#         if txt1 >=5:
#             print()
#             break
#
#


#
# text = "This is a sample text. This text is a sample text."
#
# text = text.lower()
# punctuation = '!"#$%&\'()*+,–./:;<=>?@[\\]^_`{|}~'
#
# for char in punctuation:
#     text = text.replace(char, '')
#
# words = text.split()
# frequency = {}
#
# for word in words:
#     if word in frequency:
#         frequency[word] += 1
#     else:
#         frequency[word] = 1
#
# sorted_freq = {}
#
# while len(frequency) > 0:
#     max_value = -1
#     max_key = ''
#
#     for word, count in frequency.items():
#         if count > max_value:
#             max_value = count
#             max_key = word
#
#     sorted_freq[max_key] = max_value
#     del frequency[max_key]
#
# print(sorted_freq)






























# with open('students.txt', 'r') as f:
#     user = f.read().split()
# f.close()
# with open('grades.txt', 'r') as f:
#     baho = f.read().split()
# f.close()
# txt = zip(user, baho)
#
# format = list(map(lambda x: f"{x[0]}: {x[1]}", txt))
# result = '\n'.join(format)
#
# print(result)


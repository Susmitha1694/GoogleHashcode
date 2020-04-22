# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 20:52:22 2020

@author: susmi
"""

import numpy as np

filename = "D:\\UCD Masters\\hash code\\2020\\d_tough_choices.txt"
books = []
perday = []
signup_order = []
book_order = []
books_read = {}
with open(filename) as f:
    [books_num, library_num, days_num] = [int(x) for x in f.readline().strip().split(' ')]
    scores = [int(x) for x in f.readline().strip().split(' ')]
    signup = np.zeros(library_num)
    for lib_num in range(0,library_num):
        [num_books, signup_days, num_books_pd] = [int(x) for x in f.readline().strip().split(' ')]
        signup.put(lib_num, signup_days)
        perday.append(num_books_pd)
        books.append(f.readline().strip().split(' '))
    
book_order_insert = []
days_num_cp = days_num
k = 0
for i in range(books_num):
    books_read[i] = False

for i in range(len(signup)):
    books_weight = {}
    min_val = signup.min()
    min_idx = signup.argmin()
    signup[min_idx] = signup.max() + 1
    if (days_num_cp - min_val) >= 0:
        days_num_cp -= min_val
    else:
        continue
    for book in books[min_idx]:
        books_weight[book] = scores[int(book)]
    books_weight = {key:value for key,value in sorted(books_weight.items(), key=lambda item:item[1], reverse=True)}
    
    j = 0
    #if (days_num_cp - (float(len(books[min_idx])/perday[min_idx]))) >= 0:
        #book_order[k] = books
    book_order_insert = []
    for key,value in books_weight.items():
        if books_read[int(key)] == False:
            books_read[int(key)] = True
            book_order_insert.append(int(key)) #.append(j, book)
            j += 1
        else:
            continue
    signup_order.append(min_idx)
    book_order.append(book_order_insert)

f1 = open("C:\\Users\\susmi\\Desktop\\d_tough_choices_output_old.txt", "w+")
f1.write(str(len(book_order)) + "\n")

for i in range(len(signup_order)):
    #if len(book_order[i]) == 0:
        #continue
    f1.write(str(signup_order[i]) + " " + str(len(book_order[i])) + "\n")
    string = ""
    for j in range(len(book_order[i])):
        string += str(book_order[i][j]) + " "
    f1.write(string + "\n")
f1.close()
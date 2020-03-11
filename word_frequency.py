import csv
import ast
from collections import Counter
def read_file_and_find_word_frequency(filesname):
    line_count = 0
    all_words = []
    for filename in filesname :
        with open('./clean/'+filename+'.csv', mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            # scaning for all word
            for row in csv_reader:
                x = row["clean-default"]
                y = row["clean"]
                if "not" in x or "no" in x:
                    print(f"[{line_count}]{y}\n[{line_count}]____{x}")
                x = ast.literal_eval(x)
                x = [n.strip() for n in x]
                x = unique(x) # find unique words in any comments
                all_words.extend(x)
                line_count += 1
    print(f"Processed {line_count} lines.")
    print(f"Was found {len(all_words)} words. ")
    print("Finding words frequence.")
    bf = dict(Counter(all_words)) # counting words
    print(f"Was found {len(bf)} unique words. ")
    print("Ranking words frequence.")
    af = {k: bf[k] for k in sorted(bf, key=bf.get, reverse=True)} #sort asending
    i = 1
    for element in af:
        count = af.get(element,'')
        print(f"{i}.{element} : {count}")
        if(count==1):
            break
        i += 1

def unique(list1):

    # insert the list to the set
    list_set = set(list1)
    # convert the set to the list
    unique_list = (list(list_set))
    return unique_list


'''
def unique(list1): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    return unique_list'''

patong = ["patong_google_clean","patong_trip_clean"]
promthep = ["promthep_google_clean","promthep_trip_clean"]
wat = ["wat_google_clean","wat_trip_clean"]
read_file_and_find_word_frequency(patong)

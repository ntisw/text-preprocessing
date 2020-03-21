from bs4 import BeautifulSoup
import spacy
import unidecode
from word2number import w2n
from num2words import num2words
from pycontractions import Contractions
import gensim.downloader as api
import re
import csv

# nlp = spacy.load('en_core_web_md')
nlp = spacy.load("en_core_web_sm")
# Choose model accordingly for contractions function
model = api.load("glove-twitter-25")
# model = api.load("glove-twitter-100")
# model = api.load("word2vec-google-news-300")

cont = Contractions(kv_model=model)
cont.load_models()

# exclude words from spacy stopwords list
deselect_stop_words = ['no', 'not']
for w in deselect_stop_words:
    nlp.vocab[w].is_stop = False


def strip_html_tags(text):
    """remove html tags from text"""
    soup = BeautifulSoup(text, "html.parser")
    stripped_text = soup.get_text(separator=" ")
    return stripped_text


def remove_whitespace(text):
    """remove extra whitespaces from text"""
    text = text.strip()
    return " ".join(text.split())


def remove_accented_chars(text):
    """remove accented characters from text, e.g. café"""
    text = unidecode.unidecode(text)
    return text


def expand_contractions(text):
    """expand shortened words, e.g. don't to do not"""
    text = list(cont.expand_texts([text], precise=True))[0]
    return text


def text_preprocessing(text, accented_chars=True, contractions=True,
                       convert_num=True, extra_whitespace=True,
                       lemmatization=True, lowercase=True, punctuations=True,
                       remove_html=True, remove_num=True, special_chars=True,
                       stop_words=True):
    """preprocess text with default option set to true for all steps"""

    if punctuations == True:
        text = text.replace(')', '')
        text = re.sub(r'\,(?=,*\,)', '', text)

        

    
    if remove_html == True:  # remove html tags
        text = strip_html_tags(text)
    if extra_whitespace == True:  # remove extra whitespaces
        text = remove_whitespace(text)
    if accented_chars == True:  # remove accented characters
        text = remove_accented_chars(text)
    if contractions == True:  # expand contractions
        text = expand_contractions(text)
    if lowercase == True:  # convert all characters to lowercase
        text = text.lower()

    doc = nlp(text)  # tokenise text
    clean_text = []
    index = 0
    for token in doc:
        flag = True
        edit = token.text
        # remove stop words
        if stop_words == True and token.is_stop and token.pos_ != 'NUM':
            flag = False
        # remove punctuations
        if punctuations == True and token.pos_ == 'PUNCT' and flag == True:
            flag = False
            edit = re.sub(r'\.(?=.*\.)', '', edit)
            edit = re.sub(r'\-(?=-*\-)', '', edit)
            if edit == "-" :
                bf_pun = ""
                af_pun = ""
                if index != 0:
                    bf_pun = doc[index-1].text
                if index < len(doc):
                    af_pun = doc[index+1].text
                if re.match('[a-zA-Z]', bf_pun) and re.match('[a-zA-Z]', af_pun):
                    clean_text.append(edit)
            elif edit == "," or edit == ".":
                clean_text.append(edit)
        # remove special characters
        if special_chars == True and token.pos_ == 'SYM' and flag == True:
            flag = False
        # remove numbers
        if remove_num == True and (token.pos_ == 'NUM' or token.text.isnumeric()) \
                and flag == True:
            flag = False
        # convert number words to numeric numbers
        #if convert_num == True and token.pos_ == 'NUM' and flag == True:
        #    edit = w2n.word_to_num(token.text)
        # convert numeric numbers to number words
        if convert_num == True and  token.text.isnumeric() \
             and flag == True:
            #print(token.text)
            edit = num2words(token.text)
        # convert tokens to base form
        elif lemmatization == True and token.lemma_ != "-PRON-" and flag == True:
            edit = token.lemma_
        # append tokens edited and not removed to list
        if edit != "" and flag == True:
            edit = edit.replace('.', '. ')
            clean_text.append(edit)
        index += 1

    return clean_text


def read_write_csv(filename):
    text_t = []
    clean_t = []
    clean_lists = []
    clean_default = []
    with open('./data/'+filename+'.csv', mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            text = row["comment"]
            text_t.append(text)
            clean_temp_list = text_preprocessing(
                text, lemmatization=False, stop_words=False
                ,remove_num=False)
            clean_temp_default = text_preprocessing(text)
            clean_temp = ""
            clean_lists.append(clean_temp_list)
            i = 0
            for element in clean_temp_list:
                if i == 0 or element == "-" or element=="." or element == "," :
                    clean_temp += element
                else:
                    clean_temp += " " + element
                i += 1
            clean_t.append(clean_temp)
            clean_default.append(clean_temp_default)
            line_count += 1
        print(f'\tProcessed {line_count} lines.')
    with open('./clean/'+filename+'_clean.csv', mode='w', newline='', encoding='utf-8') as clean_comment_file:
        fieldnames = ['raw', 'clean_text', 'clean_token']
        writer = csv.DictWriter(clean_comment_file, fieldnames=fieldnames)
        writer.writeheader()
        i = 0
        for row in text_t:
            text_temp = text_t[i]
            clean_temp = clean_t[i]
            clean_temp_default = clean_default[i]
            clean_temp_list = clean_lists[i]
            writer.writerow(
                {'raw': text_temp, 'clean_text': clean_temp, 'clean_token': clean_temp_list})
            i += 1
        print(f'\tWrote {line_count} lines.')


files = ["patong_google", "patong_trip", "promthep_google",
         "promthep_trip", "wat_google", "wat_trip"]

for filename in files:
    print("Cleaning "+filename)
    read_write_csv(filename)
'''
text_1 = "This is a :-) \n(cat/dog)?....but papaya-pie about break fast,diner not a dog... cat.dog"
text_2 = "This is a :-) \n(cat/dog)?....but papaya-pie about break fast,diner not a dog... cat.dog"
clean_text_1 = text_preprocessing(
    text_1, punctuations=False, lemmatization=False, stop_words=False)
clean_text_2 = text_preprocessing(
    text_2, lemmatization=False, stop_words=False)
print(clean_text_1)
print(clean_text_2)
'''

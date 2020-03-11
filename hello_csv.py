import csv
def read_write_csv(filename):
    text = []

    with open('./data/'+filename+'.csv', mode='r',encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 1
        for row in csv_reader:
            #text.append(row["comment"])
            print(line_count)
            print(row["comment"])
            line_count += 1
        print(f'Processed {line_count} lines.')
'''
    with open('./test/'+filename+'_clean.csv', mode='w',newline='',encoding='utf-8') as clean_comment_file:
        fieldnames = ['raw']
        writer = csv.DictWriter(clean_comment_file, fieldnames=fieldnames)
        writer.writeheader()
        i = 1
        for row in text:
            writer.writerow({'raw': row})
            print(i)
            print(": "+row)
            i += 1
            '''

files = ["patong_google", "patong_trip", "promthep_google",
         "promthep_trip", "wat_google", "wat_trip"]


#for filename in files:
#    print("Scaning "+filename)
#    read_write_csv(filename)
read_write_csv("patong_trip")

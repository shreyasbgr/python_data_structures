import pandas as pd
df = pd.read_csv('nyc_weather.csv')
dates = list(df['date'])
temperatures = list(df['temperature(F)'])

def problem_1():
    sum = 0
    max =temperatures[0]
    for i in range(len(dates)):
        sum+=temperatures[i]
        if temperatures[i]>max:
            max = temperatures[i]

    avg = sum /len(temperatures)
    print(f"Average = {avg}")
    print(f"Max = {max}")

def problem_2():
    date_temp_map = {}
    for i in range(len(dates)):
        date_temp_map[dates[i]]=temperatures[i]
    
    print("Temperature on Jan 9= {}".format(date_temp_map['Jan 9']))
    print("Temperature on Jan 4= {}".format(date_temp_map['Jan 4']))

def problem_3():
    with open('poem.txt','r') as f:
        poem_string = f.read()
    poem_string=poem_string.replace("\n"," ")
    word_list = poem_string.split(" ")
    freq_words ={}
    for word in word_list:
        if word in freq_words:
            freq_words[word]+=1
        else:
            freq_words[word]=1
    
    print(freq_words)

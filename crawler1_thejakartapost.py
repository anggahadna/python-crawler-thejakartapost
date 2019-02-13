from bs4 import BeautifulSoup
import requests
import string

url = input('Insert Link (The Jakarta Post) : ')

r = requests.get(url, timeout=5)

soup = BeautifulSoup(r.content, "lxml")

all_text = []

title = soup.find('h1', {'class' : 'title-large'}).text
date = soup.find('span', {'class' : 'day'}).text
time = soup.find('span', {'class' : 'time'}).text
date_time = "\n[" + date + time + "]"
border = "\n" + "=" * 60

all_text.append(title)
all_text.append(date_time)
all_text.append(border)

# detect the right category from the article

cat1 = soup.find_all('div', {'class' : 'col-md-10 col-xs-12 detailNews'}) #news
cat2 = soup.find_all('div', {'class' : 'col-md-10 col-xs-12 detailNews wdsk wtbl'}) #multimedia
cat3 = soup.find_all('div', {'class' : 'show-define-text'}) #lifestyle, travel

if len(cat1) == 1:
    cat = cat1
elif len(cat2) == 1:
    cat = cat2
elif len(cat3) == 1:
    cat = cat3

# take all text with "p" tag under specific tag and class

for news in cat:
    for n in news.descendants:
        if n.name == 'p':
            paragraphs = '\n' + n.text
            all_text.append(paragraphs)

# generate file name

rem_punc = str.maketrans('', '', string.punctuation)
name_rem = title.translate(rem_punc)

# write text to .txt file

with open('%s.txt' % name_rem, 'w+', encoding='utf-8') as f:
    for item in all_text:
        f.write("%s\n" % item)

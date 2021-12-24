import string
import re
import nltk
import matplotlib.pyplot as plt
from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from wordcloud import WordCloud

f = open('pushkin-metel.txt', "r", encoding="utf-8")
text = f.read()
type(text)
len(text)
text[:300]
# перевод в единый регистр (например, нижний)
text = text.lower()
string.punctuation
type(string.punctuation)
spec_chars = string.punctuation + '\n\xa0«»\t—…'
text = "".join([ch for ch in text if ch not in spec_chars])
text = re.sub('\n', '', text)


def remove_chars_from_text(text, chars):
    return "".join([ch for ch in text if ch not in chars])


text = remove_chars_from_text(text, spec_chars)
text = remove_chars_from_text(text, string.digits)

text_tokens = word_tokenize(text)
print(type(text_tokens), len(text_tokens))
text_tokens[:10]
text = nltk.Text(text_tokens)
print(type(text))
text[:10]
fdist = FreqDist(text)
fdist
fdist.most_common(5)
fdist.plot(30, cumulative=False)

russian_stopwords = stopwords.words("russian")
russian_stopwords.extend(['это', 'нею'])
print(len(russian_stopwords))
text_tokens = [token.strip() for token in text_tokens if token not in russian_stopwords]
print(len(text_tokens))
text = nltk.Text(text_tokens)
fdist_sw = FreqDist(text)
fdist_sw.most_common(10)
text_raw = " ".join(text)
wordcloud = WordCloud().generate(text_raw)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

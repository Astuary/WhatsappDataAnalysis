import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    h = int(360.0 * float(random_state.randint(60, 120)) / 255.0)
    s = int(100.0 * float(random_state.randint(60, 120)) / 255.0)
    l = int(100.0 * float(random_state.randint(60, 120)) / 255.0)

    return "hsl({}, {}%, {}%)".format(h, s, l)

file_content=open ("WhatsApp Chat with Nisarg 07Jan2020.txt", encoding='utf-8').read()

wordcloud = WordCloud(font_path = r'C:\Windows\Fonts\BIG JOHN.otf',
                            stopwords = STOPWORDS.update(['PM', 'Nisarg', 'Kunjal', 'Media', 'Omitted']),
                            background_color = 'white',
                            width = 2200,
                            height = 2000,
                            color_func = random_color_func
                            ).generate(file_content)

plt.imshow(wordcloud)
plt.axis('off')
plt.show()

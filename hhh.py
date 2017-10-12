import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] =False
from wordcloud import WordCloud
from scipy.misc import imread
import jieba
f=open("./鬼吹灯全集（1-8）.txt",encoding='utf-8').read()
cut_text=" ".join(jieba.cut(f, cut_all=True))
# tags=jieba.analyse.extract_tags(f,topK=50)
color_mask=imread("./alice.png")
wordcloud=WordCloud(font_path="C:\\Windows\\Fonts\\STFANGSO.ttf",max_words=200,mask=color_mask,background_color="white",width=1000,height=860,margin=2).generate(cut_text)
# wordcloud2=WordCloud(font_path="C:\\Windows\\Fonts\\STFANGSO.ttf",max_words=200,background_color="white",width=1000,height=860,margin=2).generate(cut_text)
plt.imshow(wordcloud)
plt.axis("off")
plt.title("鬼吹灯关键词")
plt.show()
wordcloud.to_file('test1.png')
# plt.imshow(wordcloud2)
# plt.axis("off")
# plt.title("鬼吹灯关键词")
# plt.show()
# wordcloud2.to_file('test2.png')

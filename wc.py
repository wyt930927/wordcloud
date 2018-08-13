# coding: utf-8
import random
import re
from pprint import pprint

import jieba
import jieba.analyse
import math
import matplotlib.pyplot as plt
# from numpy import unicode
from scipy.misc import imread  # 这是一个处理图像的函数
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

back_color = imread('WordCloudColorsByImg.jpg')  # 解析该图片

wc = WordCloud(background_color='white',  # 背景颜色
               max_words=1000,  # 最大词数
               mask=back_color,  # 以该参数值作图绘制词云，这个参数不为空时，width和height会被忽略
               max_font_size=100,  # 显示字体的最大值
               stopwords=STOPWORDS.add('苟利国'),  # 使用内置的屏蔽词，再添加'苟利国'
               font_path="C:/Windows/Fonts/STXINWEI.TTF",  # 解决显示口字型乱码问题，可进入C:/Windows/Fonts/目录更换字体
               random_state=42,  # 为每个词返回一个PIL颜色
               # width=1000,  # 图片的宽
               # height=860  #图片的长
               )


def extract_hot_words(txt_path, topK=200):
    """
    extract hot words with TF-IDF weights
    :param txt_path:
    :return: dict
    """
    text = open(txt_path).read()
    jieba.analyse.set_stop_words('./stopwords.txt')
    hot_words = jieba.analyse.extract_tags(text, topK=topK, withWeight=True, allowPOS=())

    words = {}
    for word in hot_words:
        if len(word[0]) > 1 and word[0].strip() != "" and not re.match("[0-9]+", word[0]):
            words[word[0]] = int(word[1] * 1000)

    return words


def out_wordcloud(texts):
    """
    output word cloud image
    :param texts:
    :return:
    """
    wc.generate(" ".join([k for k in texts.keys()]))
    # 基于彩色图像生成相应彩色
    image_colors = ImageColorGenerator(back_color)
    # 显示图片
    plt.imshow(wc)
    # 关闭坐标轴
    plt.axis('off')
    # 绘制词云
    plt.figure()
    plt.imshow(wc.recolor(color_func=image_colors))
    plt.axis('off')
    # 保存图片
    wc.to_file('wc.png')


def out_to_echarts(texts):
    """

    :param texts:dict
    :return:
    """
    data = []
    for k, v in texts.items():
        data.append({"name": k, "value": v, "itemStyle": {
            "normal": {
                "color": "rgb(" + ",".join(
                    [str(math.floor(random.random() * 160)), str(math.floor(random.random() * 160)),
                     str(math.floor(random.random() * 160))]) + ")"
            }
        }})

    return data


if __name__ == '__main__':
    words = extract_hot_words('dest.txt', 150)
    # out_wordcloud(words)
    pprint(out_to_echarts(words))

# -*- coding: utf-8 -*-
from cemotion import Cemotion

str_text = ['配置顶级，不解释，手机需要的各个方面都很完美',
            '院线看电影这么多年以来，这是我第一次看电影睡着了。简直是史上最大烂片！没有之一！大家小心警惕！千万不要上当！再也不要看了！',
            '我可真是太厉害了',
            '你分析几把呢',
            '我真无语',
            '今年是2024年']

c = Cemotion()
for text in str_text:
    print(f'"{text}"\n预测值:{c.predict(text)}\n')

'''Warning: this is a generated file '''
import random

def top():
    r = random.random()
    if 0/1 < r <= 1/1:
        return poetry()

def poetry():
    r = random.random()
    if 0/3 < r <= 1/3:
        return stanza()
    if 1/3 < r <= 2/3:
        return stanza() + stanza()
    if 2/3 < r <= 3/3:
        return poetry() + "\n" + stanza()

def stanza():
    r = random.random()
    if 0/3 < r <= 1/3:
        return line() + "\n" + line() + "\n" + line() + "\n\n"
    if 1/3 < r <= 2/3:
        return line() + "\n" + line() + "\n" + line() + "\n" + line() + "\n\n"
    if 2/3 < r <= 3/3:
        return line() + "\n" + stanza()

def line():
    r = random.random()
    if 0/9 < r <= 1/9:
        return sentence()
    if 1/9 < r <= 2/9:
        return sentence() + punc()
    if 2/9 < r <= 3/9:
        return sentence()
    if 3/9 < r <= 4/9:
        return sentence() + punc()
    if 4/9 < r <= 5/9:
        return sentence() + punc()
    if 5/9 < r <= 6/9:
        return sentence() + punc()
    if 6/9 < r <= 7/9:
        return sentence() + punc()
    if 7/9 < r <= 8/9:
        return sentence()
    if 8/9 < r <= 9/9:
        return question()

def sentence():
    r = random.random()
    if 0/4 < r <= 1/4:
        return expr() + punc() + connector() + expr()
    if 1/4 < r <= 2/4:
        return connector() + expr()
    if 2/4 < r <= 3/4:
        return expr()
    if 3/4 < r <= 4/4:
        return expr()

def question():
    r = random.random()
    if 0/6 < r <= 1/6:
        return qn_aux() + sentence() + "？"
    if 1/6 < r <= 2/6:
        return sentence() + "？"
    if 2/6 < r <= 3/6:
        return qn_aux() + sentence() + "？"
    if 3/6 < r <= 4/6:
        return sentence() + "？"
    if 4/6 < r <= 5/6:
        return sentence() + "？"
    if 5/6 < r <= 6/6:
        return qn_aux() + "就好像" + expr() + "？"

def qn_aux():
    r = random.random()
    if 0/7 < r <= 1/7:
        return "是否"
    if 1/7 < r <= 2/7:
        return "为何"
    if 2/7 < r <= 3/7:
        return "难道"
    if 3/7 < r <= 4/7:
        return "竟然"
    if 4/7 < r <= 5/7:
        return "为什么"
    if 5/7 < r <= 6/7:
        return "是不是"
    if 6/7 < r <= 7/7:
        return "如何"

def punc():
    r = random.random()
    if 0/9 < r <= 1/9:
        return "，"
    if 1/9 < r <= 2/9:
        return "，"
    if 2/9 < r <= 3/9:
        return "，"
    if 3/9 < r <= 4/9:
        return "，"
    if 4/9 < r <= 5/9:
        return "。"
    if 5/9 < r <= 6/9:
        return "。"
    if 6/9 < r <= 7/9:
        return "。"
    if 7/9 < r <= 8/9:
        return "——"
    if 8/9 < r <= 9/9:
        return "！"

def pronoun():
    r = random.random()
    if 0/8 < r <= 1/8:
        return "我"
    if 1/8 < r <= 2/8:
        return "你"
    if 2/8 < r <= 3/8:
        return "他"
    if 3/8 < r <= 4/8:
        return "她"
    if 4/8 < r <= 5/8:
        return "它"
    if 5/8 < r <= 6/8:
        return "他们"
    if 6/8 < r <= 7/8:
        return "我们"
    if 7/8 < r <= 8/8:
        return "你们"

def adverb():
    r = random.random()
    if 0/3 < r <= 1/3:
        return "好好"
    if 1/3 < r <= 2/3:
        return "细细"
    if 2/3 < r <= 3/3:
        return "飞快"

def verb_prefix():
    r = random.random()
    if 0/28 < r <= 1/28:
        return "不可"
    if 1/28 < r <= 2/28:
        return "不愿"
    if 2/28 < r <= 3/28:
        return "为"
    if 3/28 < r <= 4/28:
        return "为了"
    if 4/28 < r <= 5/28:
        return "又"
    if 5/28 < r <= 6/28:
        return "希望"
    if 6/28 < r <= 7/28:
        return "不曾"
    if 7/28 < r <= 8/28:
        return "曾经"
    if 8/28 < r <= 9/28:
        return "如何"
    if 9/28 < r <= 10/28:
        return "便"
    if 10/28 < r <= 11/28:
        return "明明"
    if 11/28 < r <= 12/28:
        return "不必"
    if 12/28 < r <= 13/28:
        return "始终"
    if 13/28 < r <= 14/28:
        return "将"
    if 14/28 < r <= 15/28:
        return "也"
    if 15/28 < r <= 16/28:
        return "被"
    if 16/28 < r <= 17/28:
        return "不"
    if 17/28 < r <= 18/28:
        return "不再"
    if 18/28 < r <= 19/28:
        return "已经"
    if 19/28 < r <= 20/28:
        return "正好"
    if 20/28 < r <= 21/28:
        return "一步步"
    if 21/28 < r <= 22/28:
        return "都"
    if 22/28 < r <= 23/28:
        return "都是"
    if 23/28 < r <= 24/28:
        return "要"
    if 24/28 < r <= 25/28:
        return "往往"
    if 25/28 < r <= 26/28:
        return "宁愿"
    if 26/28 < r <= 27/28:
        return "才"
    if 27/28 < r <= 28/28:
        return "甚至"

def verb_suffix():
    r = random.random()
    if 0/3 < r <= 1/3:
        return "了"
    if 1/3 < r <= 2/3:
        return "着"
    if 2/3 < r <= 3/3:
        return "到"

def verb():
    r = random.random()
    if 0/5 < r <= 1/5:
        return noun()
    if 1/5 < r <= 2/5:
        return verb_prefix() + verb_hasdec()
    if 2/5 < r <= 3/5:
        return verb_hasdec() + verb_suffix() + verb_hasdec()
    if 3/5 < r <= 4/5:
        return verb_hasdec()
    if 4/5 < r <= 5/5:
        return verb_nodec()

def verb_nodec():
    r = random.random()
    if 0/3 < r <= 1/3:
        return "是"
    if 1/3 < r <= 2/3:
        return "不是"
    if 2/3 < r <= 3/3:
        return "没有"

def verb_hasdec():
    r = random.random()
    if 0/5 < r <= 1/5:
        return common_verb()
    if 1/5 < r <= 2/5:
        return common_verb()
    if 2/5 < r <= 3/5:
        return common_verb()
    if 3/5 < r <= 4/5:
        return rarer_verb()
    if 4/5 < r <= 5/5:
        return "不" + verb()

def expr_connector():
    r = random.random()
    if 0/4 < r <= 1/4:
        return "的"
    if 1/4 < r <= 2/4:
        return "或"
    if 2/4 < r <= 3/4:
        return "和"
    if 3/4 < r <= 4/4:
        return "与"

def expr():
    r = random.random()
    if 0/54 < r <= 1/54:
        return before_people_verb()
    if 1/54 < r <= 2/54:
        return after_people_verb()
    if 2/54 < r <= 3/54:
        return generic_no_object_verb()
    if 3/54 < r <= 4/54:
        return noun()
    if 4/54 < r <= 5/54:
        return before_people_verb() + people_noun()
    if 5/54 < r <= 6/54:
        return before_abstract_verb() + abstract_noun()
    if 6/54 < r <= 7/54:
        return before_abstract_verb() + things_noun()
    if 7/54 < r <= 8/54:
        return before_people_verb() + qty_noun()
    if 8/54 < r <= 9/54:
        return before_abstract_verb() + qty_noun()
    if 9/54 < r <= 10/54:
        return before_place_verb() + place_noun()
    if 10/54 < r <= 11/54:
        return people_noun() + after_people_verb()
    if 11/54 < r <= 12/54:
        return noun() + generic_no_object_verb()
    if 12/54 < r <= 13/54:
        return before_people_verb() + people_noun()
    if 13/54 < r <= 14/54:
        return before_abstract_verb() + abstract_noun()
    if 14/54 < r <= 15/54:
        return before_abstract_verb() + time_noun()
    if 15/54 < r <= 16/54:
        return before_people_verb() + qty_noun()
    if 16/54 < r <= 17/54:
        return before_abstract_verb() + qty_noun()
    if 17/54 < r <= 18/54:
        return before_place_verb() + place_noun()
    if 18/54 < r <= 19/54:
        return people_noun() + after_people_verb()
    if 19/54 < r <= 20/54:
        return noun() + generic_no_object_verb()
    if 20/54 < r <= 21/54:
        return before_people_verb() + people_noun()
    if 21/54 < r <= 22/54:
        return before_abstract_verb() + abstract_noun()
    if 22/54 < r <= 23/54:
        return before_abstract_verb() + things_noun()
    if 23/54 < r <= 24/54:
        return before_abstract_verb() + time_noun()
    if 24/54 < r <= 25/54:
        return before_people_verb() + qty_noun()
    if 25/54 < r <= 26/54:
        return before_abstract_verb() + qty_noun()
    if 26/54 < r <= 27/54:
        return before_place_verb() + place_noun()
    if 27/54 < r <= 28/54:
        return people_noun() + after_people_verb()
    if 28/54 < r <= 29/54:
        return noun() + generic_no_object_verb()
    if 29/54 < r <= 30/54:
        return "把" + abstract_noun() + before_abstract_verb()
    if 30/54 < r <= 31/54:
        return "把" + things_noun() + before_abstract_verb()
    if 31/54 < r <= 32/54:
        return "将" + abstract_noun() + before_abstract_verb()
    if 32/54 < r <= 33/54:
        return "像" + noun() + "一样"
    if 33/54 < r <= 34/54:
        return "像" + noun() + "一样" + noun_adj()
    if 34/54 < r <= 35/54:
        return "在" + feelings_adj() + "时"
    if 35/54 < r <= 36/54:
        return noun() + expr_connector() + noun()
    if 36/54 < r <= 37/54:
        return noun_adj() + "如" + noun()
    if 37/54 < r <= 38/54:
        return noun() + "是" + noun()
    if 38/54 < r <= 39/54:
        return noun() + "不是" + noun()
    if 39/54 < r <= 40/54:
        return people_noun() + "没有" + noun()
    if 40/54 < r <= 41/54:
        return pronoun() + "没有" + noun()
    if 41/54 < r <= 42/54:
        return "让" + pronoun() + after_people_verb()
    if 42/54 < r <= 43/54:
        return verb_prefix() + expr()
    if 43/54 < r <= 44/54:
        return "是" + noun()
    if 44/54 < r <= 45/54:
        return "不是" + noun()
    if 45/54 < r <= 46/54:
        return "在" + place_noun()
    if 46/54 < r <= 47/54:
        return "在" + time_noun() + generic_no_object_verb()
    if 47/54 < r <= 48/54:
        return time_noun() + "来临"
    if 48/54 < r <= 49/54:
        return generic_no_object_verb() + "吧"
    if 49/54 < r <= 50/54:
        return after_people_verb() + "吧"
    if 50/54 < r <= 51/54:
        return noun() + "啊"
    if 51/54 < r <= 52/54:
        return "被" + noun() + before_abstract_verb()
    if 52/54 < r <= 53/54:
        return things_noun() + "很" + noun_adj()
    if 53/54 < r <= 54/54:
        return abstract_noun() + "很" + noun_adj()

def before_people_verb():
    r = random.random()
    if 0/35 < r <= 1/35:
        return "失去"
    if 1/35 < r <= 2/35:
        return "等"
    if 2/35 < r <= 3/35:
        return "离开"
    if 3/35 < r <= 4/35:
        return "背叛"
    if 4/35 < r <= 5/35:
        return "守护"
    if 5/35 < r <= 6/35:
        return "惩罚"
    if 6/35 < r <= 7/35:
        return "问"
    if 7/35 < r <= 8/35:
        return "爱上"
    if 8/35 < r <= 9/35:
        return "爱"
    if 9/35 < r <= 10/35:
        return "拥抱"
    if 10/35 < r <= 11/35:
        return "相信"
    if 11/35 < r <= 12/35:
        return "忘记"
    if 12/35 < r <= 13/35:
        return "记得"
    if 13/35 < r <= 14/35:
        return "拥有"
    if 14/35 < r <= 15/35:
        return "选择" + before_people_verb()
    if 15/35 < r <= 16/35:
        return "做"
    if 16/35 < r <= 17/35:
        return "寻找"
    if 17/35 < r <= 18/35:
        return "握别"
    if 18/35 < r <= 19/35:
        return "迎来"
    if 19/35 < r <= 20/35:
        return "等待"
    if 20/35 < r <= 21/35:
        return "碰到"
    if 21/35 < r <= 22/35:
        return "惊动"
    if 22/35 < r <= 23/35:
        return "拯救"
    if 23/35 < r <= 24/35:
        return "成全"
    if 24/35 < r <= 25/35:
        return "化作"
    if 25/35 < r <= 26/35:
        return "出现了"
    if 26/35 < r <= 27/35:
        return "推开"
    if 27/35 < r <= 28/35:
        return "告诉"
    if 28/35 < r <= 29/35:
        return "遇见"
    if 29/35 < r <= 30/35:
        return "找不到"
    if 30/35 < r <= 31/35:
        return "沦为"
    if 31/35 < r <= 32/35:
        return "陪伴"
    if 32/35 < r <= 33/35:
        return "伤害"
    if 33/35 < r <= 34/35:
        return "劝"
    if 34/35 < r <= 35/35:
        return "辜负"

def before_abstract_verb():
    r = random.random()
    if 0/68 < r <= 1/68:
        return "借"
    if 1/68 < r <= 2/68:
        return "借" + pronoun()
    if 2/68 < r <= 3/68:
        return "看着"
    if 3/68 < r <= 4/68:
        return "看到"
    if 4/68 < r <= 5/68:
        return "报之以"
    if 5/68 < r <= 6/68:
        return "预知"
    if 6/68 < r <= 7/68:
        return "等待"
    if 7/68 < r <= 8/68:
        return "等"
    if 8/68 < r <= 9/68:
        return "品味着"
    if 9/68 < r <= 10/68:
        return "透支"
    if 10/68 < r <= 11/68:
        return "吹走"
    if 11/68 < r <= 12/68:
        return "化作"
    if 12/68 < r <= 13/68:
        return "品味"
    if 13/68 < r <= 14/68:
        return "藏着"
    if 14/68 < r <= 15/68:
        return "胜过"
    if 15/68 < r <= 16/68:
        return "感受到"
    if 16/68 < r <= 17/68:
        return "将"
    if 17/68 < r <= 18/68:
        return "跌落"
    if 18/68 < r <= 19/68:
        return "画着"
    if 19/68 < r <= 20/68:
        return "画上"
    if 20/68 < r <= 21/68:
        return "吹走"
    if 21/68 < r <= 22/68:
        return "看尽"
    if 22/68 < r <= 23/68:
        return "没有"
    if 23/68 < r <= 24/68:
        return "绕过"
    if 24/68 < r <= 25/68:
        return "推开"
    if 25/68 < r <= 26/68:
        return "织出"
    if 26/68 < r <= 27/68:
        return "映照"
    if 27/68 < r <= 28/68:
        return "空有"
    if 28/68 < r <= 29/68:
        return "虚度"
    if 29/68 < r <= 30/68:
        return "照亮"
    if 30/68 < r <= 31/68:
        return "铭记"
    if 31/68 < r <= 32/68:
        return "期待"
    if 32/68 < r <= 33/68:
        return "穿透"
    if 33/68 < r <= 34/68:
        return "砸碎"
    if 34/68 < r <= 35/68:
        return "烧热"
    if 35/68 < r <= 36/68:
        return "扑灭"
    if 36/68 < r <= 37/68:
        return "找不到"
    if 37/68 < r <= 38/68:
        return "空余"
    if 38/68 < r <= 39/68:
        return "错付"
    if 39/68 < r <= 40/68:
        return "多"
    if 40/68 < r <= 41/68:
        return "沦为"
    if 41/68 < r <= 42/68:
        return "当是"
    if 42/68 < r <= 43/68:
        return "打败"
    if 43/68 < r <= 44/68:
        return "宣告"
    if 44/68 < r <= 45/68:
        return "折断"
    if 45/68 < r <= 46/68:
        return "篆刻"
    if 46/68 < r <= 47/68:
        return "背负"
    if 47/68 < r <= 48/68:
        return "逃离"
    if 48/68 < r <= 49/68:
        return "假装"
    if 49/68 < r <= 50/68:
        return "对待"
    if 50/68 < r <= 51/68:
        return "载回"
    if 51/68 < r <= 52/68:
        return "习惯"
    if 52/68 < r <= 53/68:
        return before_abstract_verb() + "了"
    if 53/68 < r <= 54/68:
        return before_abstract_verb() + "了"
    if 54/68 < r <= 55/68:
        return "废弃"
    if 55/68 < r <= 56/68:
        return "装成"
    if 56/68 < r <= 57/68:
        return "辜负"
    if 57/68 < r <= 58/68:
        return "点燃"
    if 58/68 < r <= 59/68:
        return "捕捉"
    if 59/68 < r <= 60/68:
        return "窥视"
    if 60/68 < r <= 61/68:
        return "酣睡"
    if 61/68 < r <= 62/68:
        return "踏碎"
    if 62/68 < r <= 63/68:
        return "打湿"
    if 63/68 < r <= 64/68:
        return "胁迫"
    if 64/68 < r <= 65/68:
        return "点亮"
    if 65/68 < r <= 66/68:
        return "浪费"
    if 66/68 < r <= 67/68:
        return "描绘"
    if 67/68 < r <= 68/68:
        return "阐释"

def before_place_verb():
    r = random.random()
    if 0/35 < r <= 1/35:
        return "走到"
    if 1/35 < r <= 2/35:
        return "离开"
    if 2/35 < r <= 3/35:
        return "来到"
    if 3/35 < r <= 4/35:
        return "埋在"
    if 4/35 < r <= 5/35:
        return "藏在"
    if 5/35 < r <= 6/35:
        return "行走在"
    if 6/35 < r <= 7/35:
        return "跌落"
    if 7/35 < r <= 8/35:
        return "翻越"
    if 8/35 < r <= 9/35:
        return "路经"
    if 9/35 < r <= 10/35:
        return "经过"
    if 10/35 < r <= 11/35:
        return "栖身"
    if 11/35 < r <= 12/35:
        return "飞向"
    if 12/35 < r <= 13/35:
        return "绕过"
    if 13/35 < r <= 14/35:
        return "驻守"
    if 14/35 < r <= 15/35:
        return "伫立"
    if 15/35 < r <= 16/35:
        return "跋涉"
    if 16/35 < r <= 17/35:
        return "映照"
    if 17/35 < r <= 18/35:
        return "站在"
    if 18/35 < r <= 19/35:
        return "照亮"
    if 19/35 < r <= 20/35:
        return "沿着"
    if 20/35 < r <= 21/35:
        return "怀着"
    if 21/35 < r <= 22/35:
        return "坐在"
    if 22/35 < r <= 23/35:
        return "徘徊于"
    if 23/35 < r <= 24/35:
        return "穿越"
    if 24/35 < r <= 25/35:
        return "找不到"
    if 25/35 < r <= 26/35:
        return "住在"
    if 26/35 < r <= 27/35:
        return "望断"
    if 27/35 < r <= 28/35:
        return "奔驰在"
    if 28/35 < r <= 29/35:
        return "向往"
    if 29/35 < r <= 30/35:
        return "载回"
    if 30/35 < r <= 31/35:
        return "迷失在"
    if 31/35 < r <= 32/35:
        return "遗落在"
    if 32/35 < r <= 33/35:
        return "遗落"
    if 33/35 < r <= 34/35:
        return "坠落"
    if 34/35 < r <= 35/35:
        return "蜷缩在"

def after_people_verb():
    r = random.random()
    if 0/48 < r <= 1/48:
        return "明白"
    if 1/48 < r <= 2/48:
        return "说"
    if 2/48 < r <= 3/48:
        return "走"
    if 3/48 < r <= 4/48:
        return "离开"
    if 4/48 < r <= 5/48:
        return "来"
    if 5/48 < r <= 6/48:
        return "记得"
    if 6/48 < r <= 7/48:
        return "听得"
    if 7/48 < r <= 8/48:
        return "感叹"
    if 8/48 < r <= 9/48:
        return "喜欢"
    if 9/48 < r <= 10/48:
        return "觉得"
    if 10/48 < r <= 11/48:
        return "出现"
    if 11/48 < r <= 12/48:
        return "怕"
    if 12/48 < r <= 13/48:
        return "害怕"
    if 13/48 < r <= 14/48:
        return "知道"
    if 14/48 < r <= 15/48:
        return "承认"
    if 15/48 < r <= 16/48:
        return "选择"
    if 16/48 < r <= 17/48:
        return "走过"
    if 17/48 < r <= 18/48:
        return "后退"
    if 18/48 < r <= 19/48:
        return "靠近"
    if 19/48 < r <= 20/48:
        return "重逢"
    if 20/48 < r <= 21/48:
        return "沉醉"
    if 21/48 < r <= 22/48:
        return "流浪"
    if 22/48 < r <= 23/48:
        return "愿意"
    if 23/48 < r <= 24/48:
        return "下山"
    if 24/48 < r <= 25/48:
        return "期待"
    if 25/48 < r <= 26/48:
        return "徘徊"
    if 26/48 < r <= 27/48:
        return "舍不得"
    if 27/48 < r <= 28/48:
        return "舍得"
    if 28/48 < r <= 29/48:
        return "仰望"
    if 29/48 < r <= 30/48:
        return "写诗"
    if 30/48 < r <= 31/48:
        return "生活"
    if 31/48 < r <= 32/48:
        return "坚持"
    if 32/48 < r <= 33/48:
        return "不辞而别"
    if 33/48 < r <= 34/48:
        return "开口"
    if 34/48 < r <= 35/48:
        return "不用" + after_people_verb()
    if 35/48 < r <= 36/48:
        return "不要" + after_people_verb()
    if 36/48 < r <= 37/48:
        return "终老"
    if 37/48 < r <= 38/48:
        return "衰老"
    if 38/48 < r <= 39/48:
        return "醒了"
    if 39/48 < r <= 40/48:
        return "习惯"
    if 40/48 < r <= 41/48:
        return "归来"
    if 41/48 < r <= 42/48:
        return "迷失"
    if 42/48 < r <= 43/48:
        return "醒来"
    if 43/48 < r <= 44/48:
        return "酣睡"
    if 44/48 < r <= 45/48:
        return "说爱"
    if 45/48 < r <= 46/48:
        return "翻身"
    if 46/48 < r <= 47/48:
        return "倾诉"
    if 47/48 < r <= 48/48:
        return "答应"

def generic_no_object_verb():
    r = random.random()
    if 0/85 < r <= 1/85:
        return "离开"
    if 1/85 < r <= 2/85:
        return "来"
    if 2/85 < r <= 3/85:
        return "记得"
    if 3/85 < r <= 4/85:
        return "承受"
    if 4/85 < r <= 5/85:
        return "过去"
    if 5/85 < r <= 6/85:
        return "已经" + generic_no_object_verb()
    if 6/85 < r <= 7/85:
        return "已经" + generic_no_object_verb()
    if 7/85 < r <= 8/85:
        return generic_no_object_verb() + "了"
    if 8/85 < r <= 9/85:
        return "下沉"
    if 9/85 < r <= 10/85:
        return "跌落"
    if 10/85 < r <= 11/85:
        return "盛开"
    if 11/85 < r <= 12/85:
        return "走过"
    if 12/85 < r <= 13/85:
        return "存在"
    if 13/85 < r <= 14/85:
        return "下雪"
    if 14/85 < r <= 15/85:
        return "放手"
    if 15/85 < r <= 16/85:
        return "松手"
    if 16/85 < r <= 17/85:
        return "浮动"
    if 17/85 < r <= 18/85:
        return "没有"
    if 18/85 < r <= 19/85:
        return "失重"
    if 19/85 < r <= 20/85:
        return "冻结"
    if 20/85 < r <= 21/85:
        return "受伤"
    if 21/85 < r <= 22/85:
        return "痊愈"
    if 22/85 < r <= 23/85:
        return "摇晃"
    if 23/85 < r <= 24/85:
        return "明灭"
    if 24/85 < r <= 25/85:
        return "流浪"
    if 25/85 < r <= 26/85:
        return "消融"
    if 26/85 < r <= 27/85:
        return "融化"
    if 27/85 < r <= 28/85:
        return "沉醉"
    if 28/85 < r <= 29/85:
        return "重逢"
    if 29/85 < r <= 30/85:
        return "未完"
    if 30/85 < r <= 31/85:
        return "苏醒"
    if 31/85 < r <= 32/85:
        return "愿意"
    if 32/85 < r <= 33/85:
        return "沿途"
    if 33/85 < r <= 34/85:
        return "飞扬"
    if 34/85 < r <= 35/85:
        return "飘零"
    if 35/85 < r <= 36/85:
        return "错过"
    if 36/85 < r <= 37/85:
        return "让" + noun() + generic_no_object_verb()
    if 37/85 < r <= 38/85:
        return "沸腾"
    if 38/85 < r <= 39/85:
        return "碎"
    if 39/85 < r <= 40/85:
        return "念念不忘"
    if 40/85 < r <= 41/85:
        return "砸碎"
    if 41/85 < r <= 42/85:
        return "可以"
    if 42/85 < r <= 43/85:
        return "不可以"
    if 43/85 < r <= 44/85:
        return "仰望"
    if 44/85 < r <= 45/85:
        return "写诗"
    if 45/85 < r <= 46/85:
        return "生活"
    if 46/85 < r <= 47/85:
        return "下雨"
    if 47/85 < r <= 48/85:
        return "悬空"
    if 48/85 < r <= 49/85:
        return "伤人"
    if 49/85 < r <= 50/85:
        return "高悬空中"
    if 50/85 < r <= 51/85:
        return "散落"
    if 51/85 < r <= 52/85:
        return "散落一地"
    if 52/85 < r <= 53/85:
        return "冒险"
    if 53/85 < r <= 54/85:
        return "干涸"
    if 54/85 < r <= 55/85:
        return "已经" + generic_no_object_verb()
    if 55/85 < r <= 56/85:
        return "虽然" + generic_no_object_verb()
    if 56/85 < r <= 57/85:
        return "不用" + generic_no_object_verb()
    if 57/85 < r <= 58/85:
        return "不要" + generic_no_object_verb()
    if 58/85 < r <= 59/85:
        return "浮想联翩"
    if 59/85 < r <= 60/85:
        return "归零"
    if 60/85 < r <= 61/85:
        return "挑灯"
    if 61/85 < r <= 62/85:
        return "停息"
    if 62/85 < r <= 63/85:
        return "起风"
    if 63/85 < r <= 64/85:
        return "挣扎"
    if 64/85 < r <= 65/85:
        return "回想"
    if 65/85 < r <= 66/85:
        return "停顿"
    if 66/85 < r <= 67/85:
        return "翻涌"
    if 67/85 < r <= 68/85:
        return "奔驰"
    if 68/85 < r <= 69/85:
        return "熄灭"
    if 69/85 < r <= 70/85:
        return "旋转"
    if 70/85 < r <= 71/85:
        return "颤抖"
    if 71/85 < r <= 72/85:
        return "颤抖着"
    if 72/85 < r <= 73/85:
        return "摇曳"
    if 73/85 < r <= 74/85:
        return "垂落"
    if 74/85 < r <= 75/85:
        return "漂泊"
    if 75/85 < r <= 76/85:
        return "习惯"
    if 76/85 < r <= 77/85:
        return "成长"
    if 77/85 < r <= 78/85:
        return "转暗"
    if 78/85 < r <= 79/85:
        return "生长"
    if 79/85 < r <= 80/85:
        return "跳动"
    if 80/85 < r <= 81/85:
        return "说爱"
    if 81/85 < r <= 82/85:
        return "坠落"
    if 82/85 < r <= 83/85:
        return "沉睡"
    if 83/85 < r <= 84/85:
        return "拒绝"
    if 84/85 < r <= 85/85:
        return "歌唱"

def people_qty():
    r = random.random()
    if 0/9 < r <= 1/9:
        return "一个"
    if 1/9 < r <= 2/9:
        return "千千万万个"
    if 2/9 < r <= 3/9:
        return "寥寥几个"
    if 3/9 < r <= 4/9:
        return "两三个"
    if 4/9 < r <= 5/9:
        return "好多"
    if 5/9 < r <= 6/9:
        return "太多"
    if 6/9 < r <= 7/9:
        return "无数"
    if 7/9 < r <= 8/9:
        return "许多"
    if 8/9 < r <= 9/9:
        return "太少"

def qty():
    r = random.random()
    if 0/16 < r <= 1/16:
        return "一个"
    if 1/16 < r <= 2/16:
        return "千千万万"
    if 2/16 < r <= 3/16:
        return "三两个"
    if 3/16 < r <= 4/16:
        return "一千"
    if 4/16 < r <= 5/16:
        return "无数"
    if 5/16 < r <= 6/16:
        return "数不清"
    if 6/16 < r <= 7/16:
        return "半个"
    if 7/16 < r <= 8/16:
        return "千重"
    if 8/16 < r <= 9/16:
        return "一点"
    if 9/16 < r <= 10/16:
        return "一些"
    if 10/16 < r <= 11/16:
        return "些许"
    if 11/16 < r <= 12/16:
        return "许多"
    if 12/16 < r <= 13/16:
        return "千里"
    if 13/16 < r <= 14/16:
        return "有些"
    if 14/16 < r <= 15/16:
        return "一碗"
    if 15/16 < r <= 16/16:
        return "一场"

def adj_prefix():
    r = random.random()
    if 0/5 < r <= 1/5:
        return "多"
    if 1/5 < r <= 2/5:
        return "太"
    if 2/5 < r <= 3/5:
        return "最"
    if 3/5 < r <= 4/5:
        return "好"
    if 4/5 < r <= 5/5:
        return "极为"

def adj():
    r = random.random()
    if 0/3 < r <= 1/3:
        return noun_adj()
    if 1/3 < r <= 2/3:
        return adj_only()
    if 2/3 < r <= 3/3:
        return adj_prefix() + noun_adj()

def adj_only():
    r = random.random()
    if 0/17 < r <= 1/17:
        return "小小"
    if 1/17 < r <= 2/17:
        return "大"
    if 2/17 < r <= 3/17:
        return "傻"
    if 3/17 < r <= 4/17:
        return "不够"
    if 4/17 < r <= 5/17:
        return "辽远"
    if 5/17 < r <= 6/17:
        return "急"
    if 6/17 < r <= 7/17:
        return "匆匆"
    if 7/17 < r <= 8/17:
        return "同行"
    if 8/17 < r <= 9/17:
        return "短"
    if 9/17 < r <= 10/17:
        return "阵阵"
    if 10/17 < r <= 11/17:
        return "一直"
    if 11/17 < r <= 12/17:
        return "绵绵"
    if 12/17 < r <= 13/17:
        return "孤零零"
    if 13/17 < r <= 14/17:
        return "弯曲"
    if 14/17 < r <= 15/17:
        return "废弃"
    if 15/17 < r <= 16/17:
        return "漫漫"
    if 16/17 < r <= 17/17:
        return "满满"

def feelings_adj():
    r = random.random()
    if 0/13 < r <= 1/13:
        return "悲怆"
    if 1/13 < r <= 2/13:
        return "寒冷"
    if 2/13 < r <= 3/13:
        return "向往"
    if 3/13 < r <= 4/13:
        return "年轻"
    if 4/13 < r <= 5/13:
        return "寂寞"
    if 5/13 < r <= 6/13:
        return "孤单"
    if 6/13 < r <= 7/13:
        return "孤独"
    if 7/13 < r <= 8/13:
        return "寂静"
    if 8/13 < r <= 9/13:
        return "彷徨"
    if 9/13 < r <= 10/13:
        return "激动"
    if 10/13 < r <= 11/13:
        return "勇敢"
    if 11/13 < r <= 12/13:
        return "奇怪"
    if 12/13 < r <= 13/13:
        return "恓惶"

def noun_adj():
    r = random.random()
    if 0/146 < r <= 1/146:
        return feelings_adj()
    if 1/146 < r <= 2/146:
        return feelings_adj()
    if 2/146 < r <= 3/146:
        return feelings_adj()
    if 3/146 < r <= 4/146:
        return "繁荣"
    if 4/146 < r <= 5/146:
        return "不言而喻"
    if 5/146 < r <= 6/146:
        return "最终"
    if 6/146 < r <= 7/146:
        return "藏起来"
    if 7/146 < r <= 8/146:
        return "鲁莽"
    if 8/146 < r <= 9/146:
        return "磊落"
    if 9/146 < r <= 10/146:
        return "庄严"
    if 10/146 < r <= 11/146:
        return "温暖"
    if 11/146 < r <= 12/146:
        return "温柔"
    if 12/146 < r <= 13/146:
        return "柔软"
    if 13/146 < r <= 14/146:
        return "磊落"
    if 14/146 < r <= 15/146:
        return "最初"
    if 15/146 < r <= 16/146:
        return "平庸"
    if 16/146 < r <= 17/146:
        return "无动于衷"
    if 17/146 < r <= 18/146:
        return "黑暗"
    if 18/146 < r <= 19/146:
        return "如旧"
    if 19/146 < r <= 20/146:
        return "曾经"
    if 20/146 < r <= 21/146:
        return "从前"
    if 21/146 < r <= 22/146:
        return "不顾一切"
    if 22/146 < r <= 23/146:
        return "遥远"
    if 23/146 < r <= 24/146:
        return "大火"
    if 24/146 < r <= 25/146:
        return "殷红"
    if 25/146 < r <= 26/146:
        return "漫长"
    if 26/146 < r <= 27/146:
        return "漫夜"
    if 27/146 < r <= 28/146:
        return "明朗"
    if 28/146 < r <= 29/146:
        return "恐惧"
    if 29/146 < r <= 30/146:
        return "彻头彻尾"
    if 30/146 < r <= 31/146:
        return "彻底"
    if 31/146 < r <= 32/146:
        return "清澈"
    if 32/146 < r <= 33/146:
        return "失魂落魄"
    if 33/146 < r <= 34/146:
        return "薄情"
    if 34/146 < r <= 35/146:
        return "粉身碎骨"
    if 35/146 < r <= 36/146:
        return "绚烂"
    if 36/146 < r <= 37/146:
        return "自负"
    if 37/146 < r <= 38/146:
        return "软弱"
    if 38/146 < r <= 39/146:
        return "坦白"
    if 39/146 < r <= 40/146:
        return "如花"
    if 40/146 < r <= 41/146:
        return "随意"
    if 41/146 < r <= 42/146:
        return "忧郁"
    if 42/146 < r <= 43/146:
        return "悲伤"
    if 43/146 < r <= 44/146:
        return "欢喜"
    if 44/146 < r <= 45/146:
        return "所有"
    if 45/146 < r <= 46/146:
        return "沉重"
    if 46/146 < r <= 47/146:
        return "污浊"
    if 47/146 < r <= 48/146:
        return "比如"
    if 48/146 < r <= 49/146:
        return "脆弱"
    if 49/146 < r <= 50/146:
        return "不堪"
    if 50/146 < r <= 51/146:
        return "黑白"
    if 51/146 < r <= 52/146:
        return "装模作样"
    if 52/146 < r <= 53/146:
        return "复杂"
    if 53/146 < r <= 54/146:
        return "一个人"
    if 54/146 < r <= 55/146:
        return "澄澈"
    if 55/146 < r <= 56/146:
        return "苟且"
    if 56/146 < r <= 57/146:
        return "诗意"
    if 57/146 < r <= 58/146:
        return "简单"
    if 58/146 < r <= 59/146:
        return "多余"
    if 59/146 < r <= 60/146:
        return "一无所有"
    if 60/146 < r <= 61/146:
        return "流浪"
    if 61/146 < r <= 62/146:
        return "从容"
    if 62/146 < r <= 63/146:
        return "迟钝"
    if 63/146 < r <= 64/146:
        return "苍白"
    if 64/146 < r <= 65/146:
        return "明亮"
    if 65/146 < r <= 66/146:
        return "冰凉"
    if 66/146 < r <= 67/146:
        return "舒适"
    if 67/146 < r <= 68/146:
        return "悸动"
    if 68/146 < r <= 69/146:
        return "懦弱"
    if 69/146 < r <= 70/146:
        return "傻傻"
    if 70/146 < r <= 71/146:
        return "漫漫"
    if 71/146 < r <= 72/146:
        return "烈烈"
    if 72/146 < r <= 73/146:
        return "恰到好处"
    if 73/146 < r <= 74/146:
        return "鲜明"
    if 74/146 < r <= 75/146:
        return "每一个"
    if 75/146 < r <= 76/146:
        return "好"
    if 76/146 < r <= 77/146:
        return "安宁"
    if 77/146 < r <= 78/146:
        return "宁静"
    if 78/146 < r <= 79/146:
        return "黯然"
    if 79/146 < r <= 80/146:
        return "坚定"
    if 80/146 < r <= 81/146:
        return "苦涩"
    if 81/146 < r <= 82/146:
        return "不为人知"
    if 82/146 < r <= 83/146:
        return "不易察觉"
    if 83/146 < r <= 84/146:
        return "骄傲"
    if 84/146 < r <= 85/146:
        return "圆缺"
    if 85/146 < r <= 86/146:
        return "浮光掠影"
    if 86/146 < r <= 87/146:
        return "陈年"
    if 87/146 < r <= 88/146:
        return "云涌"
    if 88/146 < r <= 89/146:
        return "风起云涌"
    if 89/146 < r <= 90/146:
        return "泛黄"
    if 90/146 < r <= 91/146:
        return "落幕"
    if 91/146 < r <= 92/146:
        return "古老"
    if 92/146 < r <= 93/146:
        return "年少"
    if 93/146 < r <= 94/146:
        return "辉煌"
    if 94/146 < r <= 95/146:
        return "模糊"
    if 95/146 < r <= 96/146:
        return "空洞"
    if 96/146 < r <= 97/146:
        return "难"
    if 97/146 < r <= 98/146:
        return "容易"
    if 98/146 < r <= 99/146:
        return "长久"
    if 99/146 < r <= 100/146:
        return "永远"
    if 100/146 < r <= 101/146:
        return "破碎"
    if 101/146 < r <= 102/146:
        return "苦痛"
    if 102/146 < r <= 103/146:
        return "疲乏"
    if 103/146 < r <= 104/146:
        return "疲倦"
    if 104/146 < r <= 105/146:
        return "轰烈"
    if 105/146 < r <= 106/146:
        return "轰轰烈烈"
    if 106/146 < r <= 107/146:
        return "这样"
    if 107/146 < r <= 108/146:
        return "那样"
    if 108/146 < r <= 109/146:
        return "这样"
    if 109/146 < r <= 110/146:
        return "那样"
    if 110/146 < r <= 111/146:
        return "神圣"
    if 111/146 < r <= 112/146:
        return "麻木"
    if 112/146 < r <= 113/146:
        return "安静"
    if 113/146 < r <= 114/146:
        return "失望"
    if 114/146 < r <= 115/146:
        return "空灵"
    if 115/146 < r <= 116/146:
        return "坦率"
    if 116/146 < r <= 117/146:
        return "清冷"
    if 117/146 < r <= 118/146:
        return "孤傲"
    if 118/146 < r <= 119/146:
        return "憔悴"
    if 119/146 < r <= 120/146:
        return "心酸"
    if 120/146 < r <= 121/146:
        return "狼狈"
    if 121/146 < r <= 122/146:
        return "昏黄"
    if 122/146 < r <= 123/146:
        return "颤抖"
    if 123/146 < r <= 124/146:
        return "摇曳"
    if 124/146 < r <= 125/146:
        return "陌生"
    if 125/146 < r <= 126/146:
        return "熟悉"
    if 126/146 < r <= 127/146:
        return "坚决"
    if 127/146 < r <= 128/146:
        return "辽阔"
    if 128/146 < r <= 129/146:
        return "疯狂"
    if 129/146 < r <= 130/146:
        return "混浊"
    if 130/146 < r <= 131/146:
        return "空白"
    if 131/146 < r <= 132/146:
        return "昏暗"
    if 132/146 < r <= 133/146:
        return "抽象"
    if 133/146 < r <= 134/146:
        return "苍老"
    if 134/146 < r <= 135/146:
        return "困倦"
    if 135/146 < r <= 136/146:
        return "枯卷"
    if 136/146 < r <= 137/146:
        return "兵荒马乱"
    if 137/146 < r <= 138/146:
        return "湿漉漉"
    if 138/146 < r <= 139/146:
        return "贫瘠"
    if 139/146 < r <= 140/146:
        return "炙热"
    if 140/146 < r <= 141/146:
        return "单调"
    if 141/146 < r <= 142/146:
        return "繁华"
    if 142/146 < r <= 143/146:
        return "普通"
    if 143/146 < r <= 144/146:
        return "肤浅"
    if 144/146 < r <= 145/146:
        return "干净"
    if 145/146 < r <= 146/146:
        return "籍籍无名"

def colors():
    r = random.random()
    if 0/10 < r <= 1/10:
        return "红色"
    if 1/10 < r <= 2/10:
        return "湛蓝"
    if 2/10 < r <= 3/10:
        return "血红"
    if 3/10 < r <= 4/10:
        return "殷红"
    if 4/10 < r <= 5/10:
        return "白色"
    if 5/10 < r <= 6/10:
        return "纯白"
    if 6/10 < r <= 7/10:
        return "灰色"
    if 7/10 < r <= 8/10:
        return "死灰色"
    if 8/10 < r <= 9/10:
        return "暗黑"
    if 9/10 < r <= 10/10:
        return "鲜红"

def noun():
    r = random.random()
    if 0/38 < r <= 1/38:
        return people_noun()
    if 1/38 < r <= 2/38:
        return things_noun()
    if 2/38 < r <= 3/38:
        return things_noun()
    if 3/38 < r <= 4/38:
        return time_noun()
    if 4/38 < r <= 5/38:
        return qty_noun()
    if 5/38 < r <= 6/38:
        return abstract_noun()
    if 6/38 < r <= 7/38:
        return abstract_noun()
    if 7/38 < r <= 8/38:
        return abstract_noun()
    if 8/38 < r <= 9/38:
        return abstract_noun()
    if 9/38 < r <= 10/38:
        return place_noun()
    if 10/38 < r <= 11/38:
        return "那" + people_noun()
    if 11/38 < r <= 12/38:
        return "这" + people_noun()
    if 12/38 < r <= 13/38:
        return "那" + qty_noun()
    if 13/38 < r <= 14/38:
        return "这" + qty_noun()
    if 14/38 < r <= 15/38:
        return pronoun()
    if 15/38 < r <= 16/38:
        return "这个" + time_noun()
    if 16/38 < r <= 17/38:
        return "这" + things_noun()
    if 17/38 < r <= 18/38:
        return "那" + things_noun()
    if 18/38 < r <= 19/38:
        return pronoun() + "的" + things_noun()
    if 19/38 < r <= 20/38:
        return pronoun() + "的" + abstract_noun()
    if 20/38 < r <= 21/38:
        return "这" + abstract_noun()
    if 21/38 < r <= 22/38:
        return "在" + place_noun()
    if 22/38 < r <= 23/38:
        return people_qty() + people_noun()
    if 23/38 < r <= 24/38:
        return qty() + time_noun()
    if 24/38 < r <= 25/38:
        return qty() + abstract_noun()
    if 25/38 < r <= 26/38:
        return noun_adj()
    if 26/38 < r <= 27/38:
        return noun_adj()
    if 27/38 < r <= 28/38:
        return time_noun() + "里"
    if 28/38 < r <= 29/38:
        return time_noun() + "外"
    if 29/38 < r <= 30/38:
        return qty_noun() + "之外"
    if 30/38 < r <= 31/38:
        return noun() + "一样"
    if 31/38 < r <= 32/38:
        return place_noun() + "尽头"
    if 32/38 < r <= 33/38:
        return place_noun() + "尽处"
    if 33/38 < r <= 34/38:
        return colors() + "的" + things_noun()
    if 34/38 < r <= 35/38:
        return "那" + adj() + "的" + people_noun()
    if 35/38 < r <= 36/38:
        return "那" + adj() + "的" + time_noun()
    if 36/38 < r <= 37/38:
        return "那" + adj() + "的" + abstract_noun()
    if 37/38 < r <= 38/38:
        return "这" + adj() + "的" + abstract_noun()

def people_noun():
    r = random.random()
    if 0/30 < r <= 1/30:
        return "诗人"
    if 1/30 < r <= 2/30:
        return "摆渡人"
    if 2/30 < r <= 3/30:
        return "爱人"
    if 3/30 < r <= 4/30:
        return "朋友"
    if 4/30 < r <= 5/30:
        return "孩童"
    if 5/30 < r <= 6/30:
        return "孩子"
    if 6/30 < r <= 7/30:
        return "少年"
    if 7/30 < r <= 8/30:
        return "过客"
    if 8/30 < r <= 9/30:
        return "归人"
    if 9/30 < r <= 10/30:
        return "路人"
    if 10/30 < r <= 11/30:
        return "别人"
    if 11/30 < r <= 12/30:
        return "佳人"
    if 12/30 < r <= 13/30:
        return "小孩"
    if 13/30 < r <= 14/30:
        return "病人"
    if 14/30 < r <= 15/30:
        return "情人"
    if 15/30 < r <= 16/30:
        return "猎人"
    if 16/30 < r <= 17/30:
        return "亲人"
    if 17/30 < r <= 18/30:
        return "陌生人"
    if 18/30 < r <= 19/30:
        return "敌人"
    if 19/30 < r <= 20/30:
        return "孤儿"
    if 20/30 < r <= 21/30:
        return "使者"
    if 21/30 < r <= 22/30:
        return "精灵"
    if 22/30 < r <= 23/30:
        return "凶徒"
    if 23/30 < r <= 24/30:
        return "绑匪"
    if 24/30 < r <= 25/30:
        return "翩翩少年"
    if 25/30 < r <= 26/30:
        return "男孩"
    if 26/30 < r <= 27/30:
        return "故人"
    if 27/30 < r <= 28/30:
        return "友人"
    if 28/30 < r <= 29/30:
        return "同伴"
    if 29/30 < r <= 30/30:
        return "恋人"

def time_noun():
    r = random.random()
    if 0/20 < r <= 1/20:
        return "春天"
    if 1/20 < r <= 2/20:
        return "冬天"
    if 2/20 < r <= 3/20:
        return "秋天"
    if 3/20 < r <= 4/20:
        return "夏天"
    if 4/20 < r <= 5/20:
        return "童年"
    if 5/20 < r <= 6/20:
        return "夜晚"
    if 6/20 < r <= 7/20:
        return "黄昏"
    if 7/20 < r <= 8/20:
        return "三月"
    if 8/20 < r <= 9/20:
        return "七月"
    if 9/20 < r <= 10/20:
        return "季节"
    if 10/20 < r <= 11/20:
        return "冷冬"
    if 11/20 < r <= 12/20:
        return "黑夜"
    if 12/20 < r <= 13/20:
        return "时刻"
    if 13/20 < r <= 14/20:
        return "醒时"
    if 14/20 < r <= 15/20:
        return "黎明"
    if 15/20 < r <= 16/20:
        return "早晨"
    if 16/20 < r <= 17/20:
        return "夏日"
    if 17/20 < r <= 18/20:
        return "午后"
    if 18/20 < r <= 19/20:
        return "半夜"
    if 19/20 < r <= 20/20:
        return "未来"

def qty_noun():
    r = random.random()
    if 0/39 < r <= 1/39:
        return "一杯烈酒"
    if 1/39 < r <= 2/39:
        return "一盏灯"
    if 2/39 < r <= 3/39:
        return "一秒"
    if 3/39 < r <= 4/39:
        return "一年"
    if 4/39 < r <= 5/39:
        return "一条街"
    if 5/39 < r <= 6/39:
        return "一寸"
    if 6/39 < r <= 7/39:
        return "三寸"
    if 7/39 < r <= 8/39:
        return "一个字"
    if 8/39 < r <= 9/39:
        return "一首歌"
    if 9/39 < r <= 10/39:
        return "一切"
    if 10/39 < r <= 11/39:
        return "一个人"
    if 11/39 < r <= 12/39:
        return "一本书"
    if 12/39 < r <= 13/39:
        return "一颗心"
    if 13/39 < r <= 14/39:
        return "一支笔"
    if 14/39 < r <= 15/39:
        return "有些人"
    if 15/39 < r <= 16/39:
        return "一道谜题"
    if 16/39 < r <= 17/39:
        return "一场梦"
    if 17/39 < r <= 18/39:
        return "一场雨"
    if 18/39 < r <= 19/39:
        return "一生"
    if 19/39 < r <= 20/39:
        return "一双手"
    if 20/39 < r <= 21/39:
        return "一地"
    if 21/39 < r <= 22/39:
        return "一棵树"
    if 22/39 < r <= 23/39:
        return "一身疲倦"
    if 23/39 < r <= 24/39:
        return "亲爱的"
    if 24/39 < r <= 25/39:
        return "脉脉春风"
    if 25/39 < r <= 26/39:
        return "一场空"
    if 26/39 < r <= 27/39:
        return "一场冒险"
    if 27/39 < r <= 28/39:
        return "一壶酒"
    if 28/39 < r <= 29/39:
        return "一句话"
    if 29/39 < r <= 30/39:
        return "一条路"
    if 30/39 < r <= 31/39:
        return "一座城"
    if 31/39 < r <= 32/39:
        return "一线阳光"
    if 32/39 < r <= 33/39:
        return "某个角落"
    if 33/39 < r <= 34/39:
        return "一个人"
    if 34/39 < r <= 35/39:
        return "一盏美酒"
    if 35/39 < r <= 36/39:
        return "一支曲调"
    if 36/39 < r <= 37/39:
        return "装睡的人"
    if 37/39 < r <= 38/39:
        return "一樽火炉"
    if 38/39 < r <= 39/39:
        return "一页诗"

def things_noun():
    r = random.random()
    if 0/68 < r <= 1/68:
        return "身躯"
    if 1/68 < r <= 2/68:
        return "瞳孔"
    if 2/68 < r <= 3/68:
        return "手"
    if 3/68 < r <= 4/68:
        return "皑皑白雪"
    if 4/68 < r <= 5/68:
        return "飞蛾"
    if 5/68 < r <= 6/68:
        return "身体"
    if 6/68 < r <= 7/68:
        return "白纸"
    if 7/68 < r <= 8/68:
        return "细雨"
    if 8/68 < r <= 9/68:
        return "酒"
    if 9/68 < r <= 10/68:
        return "窗口"
    if 10/68 < r <= 11/68:
        return "眼睛"
    if 11/68 < r <= 12/68:
        return "莲花"
    if 12/68 < r <= 13/68:
        return "灯火"
    if 13/68 < r <= 14/68:
        return "灯盏"
    if 14/68 < r <= 15/68:
        return "鸟"
    if 15/68 < r <= 16/68:
        return "飞鸟"
    if 16/68 < r <= 17/68:
        return "花瓣"
    if 17/68 < r <= 18/68:
        return "树"
    if 18/68 < r <= 19/68:
        return "书"
    if 19/68 < r <= 20/68:
        return "心"
    if 20/68 < r <= 21/68:
        return "白发"
    if 21/68 < r <= 22/68:
        return "笔"
    if 22/68 < r <= 23/68:
        return "容貌"
    if 23/68 < r <= 24/68:
        return "花香"
    if 24/68 < r <= 25/68:
        return "画像"
    if 25/68 < r <= 26/68:
        return "屋檐"
    if 26/68 < r <= 27/68:
        return "面具"
    if 27/68 < r <= 28/68:
        return "明眸"
    if 28/68 < r <= 29/68:
        return "繁花"
    if 29/68 < r <= 30/68:
        return "丛林"
    if 30/68 < r <= 31/68:
        return "曲调"
    if 31/68 < r <= 32/68:
        return "曲子"
    if 32/68 < r <= 33/68:
        return "川流"
    if 33/68 < r <= 34/68:
        return "青石"
    if 34/68 < r <= 35/68:
        return "河流"
    if 35/68 < r <= 36/68:
        return "蜡烛"
    if 36/68 < r <= 37/68:
        return "乌云"
    if 37/68 < r <= 38/68:
        return "指纹"
    if 38/68 < r <= 39/68:
        return "篱笆"
    if 39/68 < r <= 40/68:
        return "候鸟"
    if 40/68 < r <= 41/68:
        return "玫瑰"
    if 41/68 < r <= 42/68:
        return "路灯"
    if 42/68 < r <= 43/68:
        return "小鹿"
    if 43/68 < r <= 44/68:
        return "羽毛"
    if 44/68 < r <= 45/68:
        return "猎物"
    if 45/68 < r <= 46/68:
        return "长明灯"
    if 46/68 < r <= 47/68:
        return "鱼"
    if 47/68 < r <= 48/68:
        return "猫头鹰"
    if 48/68 < r <= 49/68:
        return "鸽子"
    if 49/68 < r <= 50/68:
        return "木头"
    if 50/68 < r <= 51/68:
        return "鸟笼"
    if 51/68 < r <= 52/68:
        return "风筝"
    if 52/68 < r <= 53/68:
        return "琴弦"
    if 53/68 < r <= 54/68:
        return "枯井"
    if 54/68 < r <= 55/68:
        return "船帆"
    if 55/68 < r <= 56/68:
        return "光影"
    if 56/68 < r <= 57/68:
        return "骨头"
    if 57/68 < r <= 58/68:
        return "麋鹿"
    if 58/68 < r <= 59/68:
        return "赎金"
    if 59/68 < r <= 60/68:
        return "新芽"
    if 60/68 < r <= 61/68:
        return "火柴"
    if 61/68 < r <= 62/68:
        return "皮肤"
    if 62/68 < r <= 63/68:
        return "背包"
    if 63/68 < r <= 64/68:
        return "猛兽"
    if 64/68 < r <= 65/68:
        return "陈年猛兽"
    if 65/68 < r <= 66/68:
        return "野花"
    if 66/68 < r <= 67/68:
        return "风铃"
    if 67/68 < r <= 68/68:
        return "洋葱"

def place_noun():
    r = random.random()
    if 0/51 < r <= 1/51:
        return "这里"
    if 1/51 < r <= 2/51:
        return "那里"
    if 2/51 < r <= 3/51:
        return "草原"
    if 3/51 < r <= 4/51:
        return "草原上"
    if 4/51 < r <= 5/51:
        return "沙漠"
    if 5/51 < r <= 6/51:
        return "沙漠里"
    if 6/51 < r <= 7/51:
        return "湖面"
    if 7/51 < r <= 8/51:
        return "河"
    if 8/51 < r <= 9/51:
        return "街道"
    if 9/51 < r <= 10/51:
        return "江南"
    if 10/51 < r <= 11/51:
        return "沼泽"
    if 11/51 < r <= 12/51:
        return "村庄"
    if 12/51 < r <= 13/51:
        return "海岸"
    if 13/51 < r <= 14/51:
        return "海岸边"
    if 14/51 < r <= 15/51:
        return "山"
    if 15/51 < r <= 16/51:
        return "大山"
    if 16/51 < r <= 17/51:
        return "海"
    if 17/51 < r <= 18/51:
        return "大海"
    if 18/51 < r <= 19/51:
        return "海边"
    if 19/51 < r <= 20/51:
        return "沧海"
    if 20/51 < r <= 21/51:
        return "石桥"
    if 21/51 < r <= 22/51:
        return "深山"
    if 22/51 < r <= 23/51:
        return "海角"
    if 23/51 < r <= 24/51:
        return "天涯"
    if 24/51 < r <= 25/51:
        return "远处"
    if 25/51 < r <= 26/51:
        return "孤岛"
    if 26/51 < r <= 27/51:
        return "山涧"
    if 27/51 < r <= 28/51:
        return "故乡"
    if 28/51 < r <= 29/51:
        return "路口"
    if 29/51 < r <= 30/51:
        return "瀑布"
    if 30/51 < r <= 31/51:
        return "远山"
    if 31/51 < r <= 32/51:
        return "麦田"
    if 32/51 < r <= 33/51:
        return "岛屿"
    if 33/51 < r <= 34/51:
        return "峡谷"
    if 34/51 < r <= 35/51:
        return "灯塔"
    if 35/51 < r <= 36/51:
        return "湖泊"
    if 36/51 < r <= 37/51:
        return "山峰"
    if 37/51 < r <= 38/51:
        return "高山"
    if 38/51 < r <= 39/51:
        return "尘世"
    if 39/51 < r <= 40/51:
        return "深渊"
    if 40/51 < r <= 41/51:
        return "路上"
    if 41/51 < r <= 42/51:
        return "北极"
    if 42/51 < r <= 43/51:
        return "火柴"
    if 43/51 < r <= 44/51:
        return "北极"
    if 44/51 < r <= 45/51:
        return "南海"
    if 45/51 < r <= 46/51:
        return "北海"
    if 46/51 < r <= 47/51:
        return "小镇"
    if 47/51 < r <= 48/51:
        return "稻田"
    if 48/51 < r <= 49/51:
        return "人间"
    if 49/51 < r <= 50/51:
        return "路牌"
    if 50/51 < r <= 51/51:
        return "站台"

def abstract_noun():
    r = random.random()
    if 0/233 < r <= 1/233:
        return "以前"
    if 1/233 < r <= 2/233:
        return "以后"
    if 2/233 < r <= 3/233:
        return "将来"
    if 3/233 < r <= 4/233:
        return "过去"
    if 4/233 < r <= 5/233:
        return "生活"
    if 5/233 < r <= 6/233:
        return "坚持"
    if 6/233 < r <= 7/233:
        return "风景"
    if 7/233 < r <= 8/233:
        return "回忆"
    if 8/233 < r <= 9/233:
        return "燃点"
    if 9/233 < r <= 10/233:
        return "愿望"
    if 10/233 < r <= 11/233:
        return "结局"
    if 11/233 < r <= 12/233:
        return "梦"
    if 12/233 < r <= 13/233:
        return "瞬间"
    if 13/233 < r <= 14/233:
        return "空间"
    if 14/233 < r <= 15/233:
        return "瞬间"
    if 15/233 < r <= 16/233:
        return "流水"
    if 16/233 < r <= 17/233:
        return "改变"
    if 17/233 < r <= 18/233:
        return "故事"
    if 18/233 < r <= 19/233:
        return "一寸"
    if 19/233 < r <= 20/233:
        return "三寸"
    if 20/233 < r <= 21/233:
        return "天"
    if 21/233 < r <= 22/233:
        return "天气"
    if 22/233 < r <= 23/233:
        return "明镜"
    if 23/233 < r <= 24/233:
        return "暖阳"
    if 24/233 < r <= 25/233:
        return "喧嚣"
    if 25/233 < r <= 26/233:
        return "无声"
    if 26/233 < r <= 27/233:
        return "沉默"
    if 27/233 < r <= 28/233:
        return "火焰"
    if 28/233 < r <= 29/233:
        return "神色"
    if 29/233 < r <= 30/233:
        return "眼神"
    if 30/233 < r <= 31/233:
        return "微风"
    if 31/233 < r <= 32/233:
        return "落日"
    if 32/233 < r <= 33/233:
        return "痛"
    if 33/233 < r <= 34/233:
        return "昔年"
    if 34/233 < r <= 35/233:
        return "世间"
    if 35/233 < r <= 36/233:
        return "生命"
    if 36/233 < r <= 37/233:
        return "面前"
    if 37/233 < r <= 38/233:
        return "伤痕"
    if 38/233 < r <= 39/233:
        return "长日"
    if 39/233 < r <= 40/233:
        return "远方"
    if 40/233 < r <= 41/233:
        return "泥沙"
    if 41/233 < r <= 42/233:
        return "大风"
    if 42/233 < r <= 43/233:
        return "过错"
    if 43/233 < r <= 44/233:
        return "病痛"
    if 44/233 < r <= 45/233:
        return "心头"
    if 45/233 < r <= 46/233:
        return "无人"
    if 46/233 < r <= 47/233:
        return "冰雪"
    if 47/233 < r <= 48/233:
        return "岁月"
    if 48/233 < r <= 49/233:
        return "灵魂"
    if 49/233 < r <= 50/233:
        return "自己"
    if 50/233 < r <= 51/233:
        return "绝望"
    if 51/233 < r <= 52/233:
        return "希望"
    if 52/233 < r <= 53/233:
        return "裂缝"
    if 53/233 < r <= 54/233:
        return "伤口"
    if 54/233 < r <= 55/233:
        return "错"
    if 55/233 < r <= 56/233:
        return "佳境"
    if 56/233 < r <= 57/233:
        return "时间"
    if 57/233 < r <= 58/233:
        return "里面"
    if 58/233 < r <= 59/233:
        return "外面"
    if 59/233 < r <= 60/233:
        return "月光"
    if 60/233 < r <= 61/233:
        return "盛夏"
    if 61/233 < r <= 62/233:
        return "笑语"
    if 62/233 < r <= 63/233:
        return "全世界"
    if 63/233 < r <= 64/233:
        return "天地"
    if 64/233 < r <= 65/233:
        return "笑容"
    if 65/233 < r <= 66/233:
        return "风"
    if 66/233 < r <= 67/233:
        return "晨风"
    if 67/233 < r <= 68/233:
        return "旧梦"
    if 68/233 < r <= 69/233:
        return "歌声"
    if 69/233 < r <= 70/233:
        return "利刃"
    if 70/233 < r <= 71/233:
        return "光晕"
    if 71/233 < r <= 72/233:
        return "相遇"
    if 72/233 < r <= 73/233:
        return "初遇"
    if 73/233 < r <= 74/233:
        return "心事"
    if 74/233 < r <= 75/233:
        return "拥抱"
    if 75/233 < r <= 76/233:
        return "星空"
    if 76/233 < r <= 77/233:
        return "回答"
    if 77/233 < r <= 78/233:
        return "死亡"
    if 78/233 < r <= 79/233:
        return "光明"
    if 79/233 < r <= 80/233:
        return "一个字"
    if 80/233 < r <= 81/233:
        return "一首歌"
    if 81/233 < r <= 82/233:
        return "天空"
    if 82/233 < r <= 83/233:
        return "一切"
    if 83/233 < r <= 84/233:
        return "诗歌"
    if 84/233 < r <= 85/233:
        return "诗"
    if 85/233 < r <= 86/233:
        return "年华"
    if 86/233 < r <= 87/233:
        return "世故"
    if 87/233 < r <= 88/233:
        return "玩笑"
    if 88/233 < r <= 89/233:
        return "他人"
    if 89/233 < r <= 90/233:
        return "深处"
    if 90/233 < r <= 91/233:
        return "遗憾"
    if 91/233 < r <= 92/233:
        return "满月"
    if 92/233 < r <= 93/233:
        return "星河"
    if 93/233 < r <= 94/233:
        return "轨道"
    if 94/233 < r <= 95/233:
        return "青春"
    if 95/233 < r <= 96/233:
        return "长途"
    if 96/233 < r <= 97/233:
        return "假面"
    if 97/233 < r <= 98/233:
        return "人世间"
    if 98/233 < r <= 99/233:
        return "再见"
    if 99/233 < r <= 100/233:
        return "秘密"
    if 100/233 < r <= 101/233:
        return "理由"
    if 101/233 < r <= 102/233:
        return "原因"
    if 102/233 < r <= 103/233:
        return "暗香"
    if 103/233 < r <= 104/233:
        return "方向"
    if 104/233 < r <= 105/233:
        return "错误"
    if 105/233 < r <= 106/233:
        return "欢乐"
    if 106/233 < r <= 107/233:
        return "快乐"
    if 107/233 < r <= 108/233:
        return "悲欢"
    if 108/233 < r <= 109/233:
        return "陌路"
    if 109/233 < r <= 110/233:
        return "歌"
    if 110/233 < r <= 111/233:
        return "谜题"
    if 111/233 < r <= 112/233:
        return "深意"
    if 112/233 < r <= 113/233:
        return "安排"
    if 113/233 < r <= 114/233:
        return "思绪"
    if 114/233 < r <= 115/233:
        return "泪水"
    if 115/233 < r <= 116/233:
        return "云影"
    if 116/233 < r <= 117/233:
        return "事情"
    if 117/233 < r <= 118/233:
        return "北方"
    if 118/233 < r <= 119/233:
        return "南方"
    if 119/233 < r <= 120/233:
        return "长久"
    if 120/233 < r <= 121/233:
        return "颜色"
    if 121/233 < r <= 122/233:
        return "模样"
    if 122/233 < r <= 123/233:
        return "断句"
    if 123/233 < r <= 124/233:
        return "心情"
    if 124/233 < r <= 125/233:
        return "斜阳"
    if 125/233 < r <= 126/233:
        return "残阳"
    if 126/233 < r <= 127/233:
        return "时刻"
    if 127/233 < r <= 128/233:
        return "尘土"
    if 128/233 < r <= 129/233:
        return "微命"
    if 129/233 < r <= 130/233:
        return "信念"
    if 130/233 < r <= 131/233:
        return "路途"
    if 131/233 < r <= 132/233:
        return "时光"
    if 132/233 < r <= 133/233:
        return "洪荒"
    if 133/233 < r <= 134/233:
        return "灰尘"
    if 134/233 < r <= 135/233:
        return "流火"
    if 135/233 < r <= 136/233:
        return "春风"
    if 136/233 < r <= 137/233:
        return "声音"
    if 137/233 < r <= 138/233:
        return "山水"
    if 138/233 < r <= 139/233:
        return "喜悦"
    if 139/233 < r <= 140/233:
        return "埋怨"
    if 140/233 < r <= 141/233:
        return "哀愁"
    if 141/233 < r <= 142/233:
        return "冒险"
    if 142/233 < r <= 143/233:
        return "呼喊"
    if 143/233 < r <= 144/233:
        return "呐喊"
    if 144/233 < r <= 145/233:
        return "影子"
    if 145/233 < r <= 146/233:
        return "人影"
    if 146/233 < r <= 147/233:
        return "背影"
    if 147/233 < r <= 148/233:
        return "灰烬"
    if 148/233 < r <= 149/233:
        return "尘埃"
    if 149/233 < r <= 150/233:
        return "花开"
    if 150/233 < r <= 151/233:
        return "明天"
    if 151/233 < r <= 152/233:
        return "昨天"
    if 152/233 < r <= 153/233:
        return "朝夕"
    if 153/233 < r <= 154/233:
        return "潮汐"
    if 154/233 < r <= 155/233:
        return "名字"
    if 155/233 < r <= 156/233:
        return "烟火"
    if 156/233 < r <= 157/233:
        return "何处"
    if 157/233 < r <= 158/233:
        return "明朝"
    if 158/233 < r <= 159/233:
        return "茶香"
    if 159/233 < r <= 160/233:
        return "酒香"
    if 160/233 < r <= 161/233:
        return "海啸"
    if 161/233 < r <= 162/233:
        return "梦呓"
    if 162/233 < r <= 163/233:
        return "地平线"
    if 163/233 < r <= 164/233:
        return "青烟"
    if 164/233 < r <= 165/233:
        return "馈赠"
    if 165/233 < r <= 166/233:
        return "牢笼"
    if 166/233 < r <= 167/233:
        return "拂晓"
    if 167/233 < r <= 168/233:
        return "自由"
    if 168/233 < r <= 169/233:
        return "碎纸"
    if 169/233 < r <= 170/233:
        return "纸屑"
    if 170/233 < r <= 171/233:
        return "倒影"
    if 171/233 < r <= 172/233:
        return "回声"
    if 172/233 < r <= 173/233:
        return "路口"
    if 173/233 < r <= 174/233:
        return "风帆"
    if 174/233 < r <= 175/233:
        return "羽毛"
    if 175/233 < r <= 176/233:
        return "气息"
    if 176/233 < r <= 177/233:
        return "目光"
    if 177/233 < r <= 178/233:
        return "十字路口"
    if 178/233 < r <= 179/233:
        return "梦境"
    if 179/233 < r <= 180/233:
        return "记忆"
    if 180/233 < r <= 181/233:
        return "夕阳"
    if 181/233 < r <= 182/233:
        return "谎言"
    if 182/233 < r <= 183/233:
        return "泡沫"
    if 183/233 < r <= 184/233:
        return "空白"
    if 184/233 < r <= 185/233:
        return "轻蔑"
    if 185/233 < r <= 186/233:
        return "仇敌"
    if 186/233 < r <= 187/233:
        return "饥渴"
    if 187/233 < r <= 188/233:
        return "青苔"
    if 188/233 < r <= 189/233:
        return "烙印"
    if 189/233 < r <= 190/233:
        return "角落"
    if 190/233 < r <= 191/233:
        return "意义"
    if 191/233 < r <= 192/233:
        return "四壁"
    if 192/233 < r <= 193/233:
        return "沙丘"
    if 193/233 < r <= 194/233:
        return "山丘"
    if 194/233 < r <= 195/233:
        return "样貌"
    if 195/233 < r <= 196/233:
        return "暮年"
    if 196/233 < r <= 197/233:
        return "群星"
    if 197/233 < r <= 198/233:
        return "光影"
    if 198/233 < r <= 199/233:
        return "天光"
    if 199/233 < r <= 200/233:
        return "萤火"
    if 200/233 < r <= 201/233:
        return "花香"
    if 201/233 < r <= 202/233:
        return "骨头"
    if 202/233 < r <= 203/233:
        return "诗篇"
    if 203/233 < r <= 204/233:
        return "韵脚"
    if 204/233 < r <= 205/233:
        return "糖"
    if 205/233 < r <= 206/233:
        return "真心"
    if 206/233 < r <= 207/233:
        return "鸦噪"
    if 207/233 < r <= 208/233:
        return "一生"
    if 208/233 < r <= 209/233:
        return "人生"
    if 209/233 < r <= 210/233:
        return "寿命"
    if 210/233 < r <= 211/233:
        return "暮色"
    if 211/233 < r <= 212/233:
        return "雾气"
    if 212/233 < r <= 213/233:
        return "万有引力"
    if 213/233 < r <= 214/233:
        return "酒香"
    if 214/233 < r <= 215/233:
        return "人质"
    if 215/233 < r <= 216/233:
        return "遗物"
    if 216/233 < r <= 217/233:
        return "归宿"
    if 217/233 < r <= 218/233:
        return "推嚷"
    if 218/233 < r <= 219/233:
        return "美酒"
    if 219/233 < r <= 220/233:
        return "钟点"
    if 220/233 < r <= 221/233:
        return "钟点"
    if 221/233 < r <= 222/233:
        return "人间"
    if 222/233 < r <= 223/233:
        return "忧愁"
    if 223/233 < r <= 224/233:
        return "呼吸"
    if 224/233 < r <= 225/233:
        return "同类"
    if 225/233 < r <= 226/233:
        return "使命"
    if 226/233 < r <= 227/233:
        return "尾音"
    if 227/233 < r <= 228/233:
        return "本质"
    if 228/233 < r <= 229/233:
        return "残灯"
    if 229/233 < r <= 230/233:
        return "洪流"
    if 230/233 < r <= 231/233:
        return "晚风"
    if 231/233 < r <= 232/233:
        return "年代"
    if 232/233 < r <= 233/233:
        return "告白"

def connector():
    r = random.random()
    if 0/20 < r <= 1/20:
        return "可是"
    if 1/20 < r <= 2/20:
        return "然而"
    if 2/20 < r <= 3/20:
        return "但是"
    if 3/20 < r <= 4/20:
        return "于是"
    if 4/20 < r <= 5/20:
        return "所以"
    if 5/20 < r <= 6/20:
        return "原来"
    if 6/20 < r <= 7/20:
        return "如果"
    if 7/20 < r <= 8/20:
        return "如同"
    if 8/20 < r <= 9/20:
        return "后来"
    if 9/20 < r <= 10/20:
        return "虽然"
    if 10/20 < r <= 11/20:
        return "还是"
    if 11/20 < r <= 12/20:
        return "若"
    if 12/20 < r <= 13/20:
        return "其实"
    if 13/20 < r <= 14/20:
        return "总是"
    if 14/20 < r <= 15/20:
        return "终于"
    if 15/20 < r <= 16/20:
        return "而"
    if 16/20 < r <= 17/20:
        return "本来"
    if 17/20 < r <= 18/20:
        return "总有"
    if 18/20 < r <= 19/20:
        return "毕竟"
    if 19/20 < r <= 20/20:
        return "从来"

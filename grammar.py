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
    if 0/34 < r <= 1/34:
        return "失去"
    if 1/34 < r <= 2/34:
        return "等"
    if 2/34 < r <= 3/34:
        return "离开"
    if 3/34 < r <= 4/34:
        return "背叛"
    if 4/34 < r <= 5/34:
        return "守护"
    if 5/34 < r <= 6/34:
        return "惩罚"
    if 6/34 < r <= 7/34:
        return "问"
    if 7/34 < r <= 8/34:
        return "爱上"
    if 8/34 < r <= 9/34:
        return "爱"
    if 9/34 < r <= 10/34:
        return "拥抱"
    if 10/34 < r <= 11/34:
        return "相信"
    if 11/34 < r <= 12/34:
        return "忘记"
    if 12/34 < r <= 13/34:
        return "记得"
    if 13/34 < r <= 14/34:
        return "拥有"
    if 14/34 < r <= 15/34:
        return "选择" + before_people_verb()
    if 15/34 < r <= 16/34:
        return "做"
    if 16/34 < r <= 17/34:
        return "寻找"
    if 17/34 < r <= 18/34:
        return "握别"
    if 18/34 < r <= 19/34:
        return "迎来"
    if 19/34 < r <= 20/34:
        return "等待"
    if 20/34 < r <= 21/34:
        return "碰到"
    if 21/34 < r <= 22/34:
        return "惊动"
    if 22/34 < r <= 23/34:
        return "拯救"
    if 23/34 < r <= 24/34:
        return "成全"
    if 24/34 < r <= 25/34:
        return "化作"
    if 25/34 < r <= 26/34:
        return "出现了"
    if 26/34 < r <= 27/34:
        return "推开"
    if 27/34 < r <= 28/34:
        return "告诉"
    if 28/34 < r <= 29/34:
        return "遇见"
    if 29/34 < r <= 30/34:
        return "找不到"
    if 30/34 < r <= 31/34:
        return "沦为"
    if 31/34 < r <= 32/34:
        return "陪伴"
    if 32/34 < r <= 33/34:
        return "伤害"
    if 33/34 < r <= 34/34:
        return "劝"

def before_abstract_verb():
    r = random.random()
    if 0/56 < r <= 1/56:
        return "借"
    if 1/56 < r <= 2/56:
        return "借" + pronoun()
    if 2/56 < r <= 3/56:
        return "看着"
    if 3/56 < r <= 4/56:
        return "看到"
    if 4/56 < r <= 5/56:
        return "报之以"
    if 5/56 < r <= 6/56:
        return "预知"
    if 6/56 < r <= 7/56:
        return "等待"
    if 7/56 < r <= 8/56:
        return "等"
    if 8/56 < r <= 9/56:
        return "品味着"
    if 9/56 < r <= 10/56:
        return "透支"
    if 10/56 < r <= 11/56:
        return "吹走"
    if 11/56 < r <= 12/56:
        return "化作"
    if 12/56 < r <= 13/56:
        return "品味"
    if 13/56 < r <= 14/56:
        return "藏着"
    if 14/56 < r <= 15/56:
        return "胜过"
    if 15/56 < r <= 16/56:
        return "感受到"
    if 16/56 < r <= 17/56:
        return "将"
    if 17/56 < r <= 18/56:
        return "跌落"
    if 18/56 < r <= 19/56:
        return "画着"
    if 19/56 < r <= 20/56:
        return "画上"
    if 20/56 < r <= 21/56:
        return "吹走"
    if 21/56 < r <= 22/56:
        return "看尽"
    if 22/56 < r <= 23/56:
        return "没有"
    if 23/56 < r <= 24/56:
        return "绕过"
    if 24/56 < r <= 25/56:
        return "推开"
    if 25/56 < r <= 26/56:
        return "织出"
    if 26/56 < r <= 27/56:
        return "映照"
    if 27/56 < r <= 28/56:
        return "空有"
    if 28/56 < r <= 29/56:
        return "虚度"
    if 29/56 < r <= 30/56:
        return "照亮"
    if 30/56 < r <= 31/56:
        return "铭记"
    if 31/56 < r <= 32/56:
        return "期待"
    if 32/56 < r <= 33/56:
        return "穿透"
    if 33/56 < r <= 34/56:
        return "砸碎"
    if 34/56 < r <= 35/56:
        return "烧热"
    if 35/56 < r <= 36/56:
        return "扑灭"
    if 36/56 < r <= 37/56:
        return "找不到"
    if 37/56 < r <= 38/56:
        return "空余"
    if 38/56 < r <= 39/56:
        return "错付"
    if 39/56 < r <= 40/56:
        return "多"
    if 40/56 < r <= 41/56:
        return "沦为"
    if 41/56 < r <= 42/56:
        return "当是"
    if 42/56 < r <= 43/56:
        return "打败"
    if 43/56 < r <= 44/56:
        return "宣告"
    if 44/56 < r <= 45/56:
        return "折断"
    if 45/56 < r <= 46/56:
        return "篆刻"
    if 46/56 < r <= 47/56:
        return "背负"
    if 47/56 < r <= 48/56:
        return "逃离"
    if 48/56 < r <= 49/56:
        return "假装"
    if 49/56 < r <= 50/56:
        return "对待"
    if 50/56 < r <= 51/56:
        return "载回"
    if 51/56 < r <= 52/56:
        return "习惯"
    if 52/56 < r <= 53/56:
        return before_abstract_verb() + "了"
    if 53/56 < r <= 54/56:
        return before_abstract_verb() + "了"
    if 54/56 < r <= 55/56:
        return "废弃"
    if 55/56 < r <= 56/56:
        return "装成"

def before_place_verb():
    r = random.random()
    if 0/31 < r <= 1/31:
        return "走到"
    if 1/31 < r <= 2/31:
        return "离开"
    if 2/31 < r <= 3/31:
        return "来到"
    if 3/31 < r <= 4/31:
        return "埋在"
    if 4/31 < r <= 5/31:
        return "藏在"
    if 5/31 < r <= 6/31:
        return "行走在"
    if 6/31 < r <= 7/31:
        return "跌落"
    if 7/31 < r <= 8/31:
        return "翻越"
    if 8/31 < r <= 9/31:
        return "路经"
    if 9/31 < r <= 10/31:
        return "经过"
    if 10/31 < r <= 11/31:
        return "栖身"
    if 11/31 < r <= 12/31:
        return "飞向"
    if 12/31 < r <= 13/31:
        return "绕过"
    if 13/31 < r <= 14/31:
        return "驻守"
    if 14/31 < r <= 15/31:
        return "伫立"
    if 15/31 < r <= 16/31:
        return "跋涉"
    if 16/31 < r <= 17/31:
        return "映照"
    if 17/31 < r <= 18/31:
        return "站在"
    if 18/31 < r <= 19/31:
        return "照亮"
    if 19/31 < r <= 20/31:
        return "沿着"
    if 20/31 < r <= 21/31:
        return "怀着"
    if 21/31 < r <= 22/31:
        return "坐在"
    if 22/31 < r <= 23/31:
        return "徘徊于"
    if 23/31 < r <= 24/31:
        return "穿越"
    if 24/31 < r <= 25/31:
        return "找不到"
    if 25/31 < r <= 26/31:
        return "住在"
    if 26/31 < r <= 27/31:
        return "望断"
    if 27/31 < r <= 28/31:
        return "奔驰在"
    if 28/31 < r <= 29/31:
        return "向往"
    if 29/31 < r <= 30/31:
        return "载回"
    if 30/31 < r <= 31/31:
        return "迷失在"

def after_people_verb():
    r = random.random()
    if 0/42 < r <= 1/42:
        return "明白"
    if 1/42 < r <= 2/42:
        return "说"
    if 2/42 < r <= 3/42:
        return "走"
    if 3/42 < r <= 4/42:
        return "离开"
    if 4/42 < r <= 5/42:
        return "来"
    if 5/42 < r <= 6/42:
        return "记得"
    if 6/42 < r <= 7/42:
        return "听得"
    if 7/42 < r <= 8/42:
        return "感叹"
    if 8/42 < r <= 9/42:
        return "喜欢"
    if 9/42 < r <= 10/42:
        return "觉得"
    if 10/42 < r <= 11/42:
        return "出现"
    if 11/42 < r <= 12/42:
        return "怕"
    if 12/42 < r <= 13/42:
        return "害怕"
    if 13/42 < r <= 14/42:
        return "知道"
    if 14/42 < r <= 15/42:
        return "承认"
    if 15/42 < r <= 16/42:
        return "选择"
    if 16/42 < r <= 17/42:
        return "走过"
    if 17/42 < r <= 18/42:
        return "后退"
    if 18/42 < r <= 19/42:
        return "靠近"
    if 19/42 < r <= 20/42:
        return "重逢"
    if 20/42 < r <= 21/42:
        return "沉醉"
    if 21/42 < r <= 22/42:
        return "流浪"
    if 22/42 < r <= 23/42:
        return "愿意"
    if 23/42 < r <= 24/42:
        return "下山"
    if 24/42 < r <= 25/42:
        return "期待"
    if 25/42 < r <= 26/42:
        return "徘徊"
    if 26/42 < r <= 27/42:
        return "舍不得"
    if 27/42 < r <= 28/42:
        return "舍得"
    if 28/42 < r <= 29/42:
        return "仰望"
    if 29/42 < r <= 30/42:
        return "写诗"
    if 30/42 < r <= 31/42:
        return "生活"
    if 31/42 < r <= 32/42:
        return "坚持"
    if 32/42 < r <= 33/42:
        return "不辞而别"
    if 33/42 < r <= 34/42:
        return "开口"
    if 34/42 < r <= 35/42:
        return "不用" + after_people_verb()
    if 35/42 < r <= 36/42:
        return "不要" + after_people_verb()
    if 36/42 < r <= 37/42:
        return "终老"
    if 37/42 < r <= 38/42:
        return "衰老"
    if 38/42 < r <= 39/42:
        return "醒了"
    if 39/42 < r <= 40/42:
        return "习惯"
    if 40/42 < r <= 41/42:
        return "归来"
    if 41/42 < r <= 42/42:
        return "迷失"

def generic_no_object_verb():
    r = random.random()
    if 0/78 < r <= 1/78:
        return "离开"
    if 1/78 < r <= 2/78:
        return "来"
    if 2/78 < r <= 3/78:
        return "记得"
    if 3/78 < r <= 4/78:
        return "承受"
    if 4/78 < r <= 5/78:
        return "过去"
    if 5/78 < r <= 6/78:
        return "已经" + generic_no_object_verb()
    if 6/78 < r <= 7/78:
        return "已经" + generic_no_object_verb()
    if 7/78 < r <= 8/78:
        return generic_no_object_verb() + "了"
    if 8/78 < r <= 9/78:
        return "下沉"
    if 9/78 < r <= 10/78:
        return "跌落"
    if 10/78 < r <= 11/78:
        return "盛开"
    if 11/78 < r <= 12/78:
        return "走过"
    if 12/78 < r <= 13/78:
        return "存在"
    if 13/78 < r <= 14/78:
        return "下雪"
    if 14/78 < r <= 15/78:
        return "放手"
    if 15/78 < r <= 16/78:
        return "松手"
    if 16/78 < r <= 17/78:
        return "浮动"
    if 17/78 < r <= 18/78:
        return "没有"
    if 18/78 < r <= 19/78:
        return "失重"
    if 19/78 < r <= 20/78:
        return "冻结"
    if 20/78 < r <= 21/78:
        return "受伤"
    if 21/78 < r <= 22/78:
        return "痊愈"
    if 22/78 < r <= 23/78:
        return "摇晃"
    if 23/78 < r <= 24/78:
        return "明灭"
    if 24/78 < r <= 25/78:
        return "流浪"
    if 25/78 < r <= 26/78:
        return "消融"
    if 26/78 < r <= 27/78:
        return "融化"
    if 27/78 < r <= 28/78:
        return "沉醉"
    if 28/78 < r <= 29/78:
        return "重逢"
    if 29/78 < r <= 30/78:
        return "未完"
    if 30/78 < r <= 31/78:
        return "苏醒"
    if 31/78 < r <= 32/78:
        return "愿意"
    if 32/78 < r <= 33/78:
        return "沿途"
    if 33/78 < r <= 34/78:
        return "飞扬"
    if 34/78 < r <= 35/78:
        return "飘零"
    if 35/78 < r <= 36/78:
        return "错过"
    if 36/78 < r <= 37/78:
        return "让" + noun() + generic_no_object_verb()
    if 37/78 < r <= 38/78:
        return "沸腾"
    if 38/78 < r <= 39/78:
        return "碎"
    if 39/78 < r <= 40/78:
        return "念念不忘"
    if 40/78 < r <= 41/78:
        return "砸碎"
    if 41/78 < r <= 42/78:
        return "可以"
    if 42/78 < r <= 43/78:
        return "不可以"
    if 43/78 < r <= 44/78:
        return "仰望"
    if 44/78 < r <= 45/78:
        return "写诗"
    if 45/78 < r <= 46/78:
        return "生活"
    if 46/78 < r <= 47/78:
        return "下雨"
    if 47/78 < r <= 48/78:
        return "悬空"
    if 48/78 < r <= 49/78:
        return "伤人"
    if 49/78 < r <= 50/78:
        return "高悬空中"
    if 50/78 < r <= 51/78:
        return "散落"
    if 51/78 < r <= 52/78:
        return "散落一地"
    if 52/78 < r <= 53/78:
        return "冒险"
    if 53/78 < r <= 54/78:
        return "干涸"
    if 54/78 < r <= 55/78:
        return "已经" + generic_no_object_verb()
    if 55/78 < r <= 56/78:
        return "虽然" + generic_no_object_verb()
    if 56/78 < r <= 57/78:
        return "不用" + generic_no_object_verb()
    if 57/78 < r <= 58/78:
        return "不要" + generic_no_object_verb()
    if 58/78 < r <= 59/78:
        return "浮想联翩"
    if 59/78 < r <= 60/78:
        return "归零"
    if 60/78 < r <= 61/78:
        return "挑灯"
    if 61/78 < r <= 62/78:
        return "停息"
    if 62/78 < r <= 63/78:
        return "起风"
    if 63/78 < r <= 64/78:
        return "挣扎"
    if 64/78 < r <= 65/78:
        return "回想"
    if 65/78 < r <= 66/78:
        return "停顿"
    if 66/78 < r <= 67/78:
        return "翻涌"
    if 67/78 < r <= 68/78:
        return "奔驰"
    if 68/78 < r <= 69/78:
        return "熄灭"
    if 69/78 < r <= 70/78:
        return "旋转"
    if 70/78 < r <= 71/78:
        return "颤抖"
    if 71/78 < r <= 72/78:
        return "颤抖着"
    if 72/78 < r <= 73/78:
        return "摇曳"
    if 73/78 < r <= 74/78:
        return "垂落"
    if 74/78 < r <= 75/78:
        return "漂泊"
    if 75/78 < r <= 76/78:
        return "习惯"
    if 76/78 < r <= 77/78:
        return "成长"
    if 77/78 < r <= 78/78:
        return "转暗"

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
    if 0/12 < r <= 1/12:
        return "悲怆"
    if 1/12 < r <= 2/12:
        return "寒冷"
    if 2/12 < r <= 3/12:
        return "向往"
    if 3/12 < r <= 4/12:
        return "年轻"
    if 4/12 < r <= 5/12:
        return "寂寞"
    if 5/12 < r <= 6/12:
        return "孤单"
    if 6/12 < r <= 7/12:
        return "孤独"
    if 7/12 < r <= 8/12:
        return "寂静"
    if 8/12 < r <= 9/12:
        return "彷徨"
    if 9/12 < r <= 10/12:
        return "激动"
    if 10/12 < r <= 11/12:
        return "勇敢"
    if 11/12 < r <= 12/12:
        return "奇怪"

def noun_adj():
    r = random.random()
    if 0/132 < r <= 1/132:
        return feelings_adj()
    if 1/132 < r <= 2/132:
        return feelings_adj()
    if 2/132 < r <= 3/132:
        return feelings_adj()
    if 3/132 < r <= 4/132:
        return "繁荣"
    if 4/132 < r <= 5/132:
        return "不言而喻"
    if 5/132 < r <= 6/132:
        return "最终"
    if 6/132 < r <= 7/132:
        return "藏起来"
    if 7/132 < r <= 8/132:
        return "鲁莽"
    if 8/132 < r <= 9/132:
        return "磊落"
    if 9/132 < r <= 10/132:
        return "庄严"
    if 10/132 < r <= 11/132:
        return "温暖"
    if 11/132 < r <= 12/132:
        return "温柔"
    if 12/132 < r <= 13/132:
        return "柔软"
    if 13/132 < r <= 14/132:
        return "磊落"
    if 14/132 < r <= 15/132:
        return "最初"
    if 15/132 < r <= 16/132:
        return "平庸"
    if 16/132 < r <= 17/132:
        return "无动于衷"
    if 17/132 < r <= 18/132:
        return "黑暗"
    if 18/132 < r <= 19/132:
        return "如旧"
    if 19/132 < r <= 20/132:
        return "曾经"
    if 20/132 < r <= 21/132:
        return "从前"
    if 21/132 < r <= 22/132:
        return "不顾一切"
    if 22/132 < r <= 23/132:
        return "遥远"
    if 23/132 < r <= 24/132:
        return "大火"
    if 24/132 < r <= 25/132:
        return "殷红"
    if 25/132 < r <= 26/132:
        return "漫长"
    if 26/132 < r <= 27/132:
        return "漫夜"
    if 27/132 < r <= 28/132:
        return "明朗"
    if 28/132 < r <= 29/132:
        return "恐惧"
    if 29/132 < r <= 30/132:
        return "彻头彻尾"
    if 30/132 < r <= 31/132:
        return "彻底"
    if 31/132 < r <= 32/132:
        return "清澈"
    if 32/132 < r <= 33/132:
        return "失魂落魄"
    if 33/132 < r <= 34/132:
        return "薄情"
    if 34/132 < r <= 35/132:
        return "粉身碎骨"
    if 35/132 < r <= 36/132:
        return "绚烂"
    if 36/132 < r <= 37/132:
        return "自负"
    if 37/132 < r <= 38/132:
        return "软弱"
    if 38/132 < r <= 39/132:
        return "坦白"
    if 39/132 < r <= 40/132:
        return "如花"
    if 40/132 < r <= 41/132:
        return "随意"
    if 41/132 < r <= 42/132:
        return "忧郁"
    if 42/132 < r <= 43/132:
        return "悲伤"
    if 43/132 < r <= 44/132:
        return "欢喜"
    if 44/132 < r <= 45/132:
        return "所有"
    if 45/132 < r <= 46/132:
        return "沉重"
    if 46/132 < r <= 47/132:
        return "污浊"
    if 47/132 < r <= 48/132:
        return "比如"
    if 48/132 < r <= 49/132:
        return "脆弱"
    if 49/132 < r <= 50/132:
        return "不堪"
    if 50/132 < r <= 51/132:
        return "黑白"
    if 51/132 < r <= 52/132:
        return "装模作样"
    if 52/132 < r <= 53/132:
        return "复杂"
    if 53/132 < r <= 54/132:
        return "一个人"
    if 54/132 < r <= 55/132:
        return "澄澈"
    if 55/132 < r <= 56/132:
        return "苟且"
    if 56/132 < r <= 57/132:
        return "诗意"
    if 57/132 < r <= 58/132:
        return "简单"
    if 58/132 < r <= 59/132:
        return "多余"
    if 59/132 < r <= 60/132:
        return "一无所有"
    if 60/132 < r <= 61/132:
        return "流浪"
    if 61/132 < r <= 62/132:
        return "从容"
    if 62/132 < r <= 63/132:
        return "迟钝"
    if 63/132 < r <= 64/132:
        return "苍白"
    if 64/132 < r <= 65/132:
        return "明亮"
    if 65/132 < r <= 66/132:
        return "冰凉"
    if 66/132 < r <= 67/132:
        return "舒适"
    if 67/132 < r <= 68/132:
        return "悸动"
    if 68/132 < r <= 69/132:
        return "懦弱"
    if 69/132 < r <= 70/132:
        return "傻傻"
    if 70/132 < r <= 71/132:
        return "漫漫"
    if 71/132 < r <= 72/132:
        return "烈烈"
    if 72/132 < r <= 73/132:
        return "恰到好处"
    if 73/132 < r <= 74/132:
        return "鲜明"
    if 74/132 < r <= 75/132:
        return "每一个"
    if 75/132 < r <= 76/132:
        return "好"
    if 76/132 < r <= 77/132:
        return "安宁"
    if 77/132 < r <= 78/132:
        return "宁静"
    if 78/132 < r <= 79/132:
        return "黯然"
    if 79/132 < r <= 80/132:
        return "坚定"
    if 80/132 < r <= 81/132:
        return "苦涩"
    if 81/132 < r <= 82/132:
        return "不为人知"
    if 82/132 < r <= 83/132:
        return "不易察觉"
    if 83/132 < r <= 84/132:
        return "骄傲"
    if 84/132 < r <= 85/132:
        return "圆缺"
    if 85/132 < r <= 86/132:
        return "浮光掠影"
    if 86/132 < r <= 87/132:
        return "陈年"
    if 87/132 < r <= 88/132:
        return "云涌"
    if 88/132 < r <= 89/132:
        return "风起云涌"
    if 89/132 < r <= 90/132:
        return "泛黄"
    if 90/132 < r <= 91/132:
        return "落幕"
    if 91/132 < r <= 92/132:
        return "古老"
    if 92/132 < r <= 93/132:
        return "年少"
    if 93/132 < r <= 94/132:
        return "辉煌"
    if 94/132 < r <= 95/132:
        return "模糊"
    if 95/132 < r <= 96/132:
        return "空洞"
    if 96/132 < r <= 97/132:
        return "难"
    if 97/132 < r <= 98/132:
        return "容易"
    if 98/132 < r <= 99/132:
        return "长久"
    if 99/132 < r <= 100/132:
        return "永远"
    if 100/132 < r <= 101/132:
        return "破碎"
    if 101/132 < r <= 102/132:
        return "苦痛"
    if 102/132 < r <= 103/132:
        return "疲乏"
    if 103/132 < r <= 104/132:
        return "疲倦"
    if 104/132 < r <= 105/132:
        return "轰烈"
    if 105/132 < r <= 106/132:
        return "轰轰烈烈"
    if 106/132 < r <= 107/132:
        return "这样"
    if 107/132 < r <= 108/132:
        return "那样"
    if 108/132 < r <= 109/132:
        return "这样"
    if 109/132 < r <= 110/132:
        return "那样"
    if 110/132 < r <= 111/132:
        return "神圣"
    if 111/132 < r <= 112/132:
        return "麻木"
    if 112/132 < r <= 113/132:
        return "安静"
    if 113/132 < r <= 114/132:
        return "失望"
    if 114/132 < r <= 115/132:
        return "空灵"
    if 115/132 < r <= 116/132:
        return "坦率"
    if 116/132 < r <= 117/132:
        return "清冷"
    if 117/132 < r <= 118/132:
        return "孤傲"
    if 118/132 < r <= 119/132:
        return "憔悴"
    if 119/132 < r <= 120/132:
        return "心酸"
    if 120/132 < r <= 121/132:
        return "狼狈"
    if 121/132 < r <= 122/132:
        return "昏黄"
    if 122/132 < r <= 123/132:
        return "颤抖"
    if 123/132 < r <= 124/132:
        return "摇曳"
    if 124/132 < r <= 125/132:
        return "陌生"
    if 125/132 < r <= 126/132:
        return "熟悉"
    if 126/132 < r <= 127/132:
        return "坚决"
    if 127/132 < r <= 128/132:
        return "辽阔"
    if 128/132 < r <= 129/132:
        return "疯狂"
    if 129/132 < r <= 130/132:
        return "混浊"
    if 130/132 < r <= 131/132:
        return "空白"
    if 131/132 < r <= 132/132:
        return "昏暗"

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
    if 0/21 < r <= 1/21:
        return "诗人"
    if 1/21 < r <= 2/21:
        return "摆渡人"
    if 2/21 < r <= 3/21:
        return "爱人"
    if 3/21 < r <= 4/21:
        return "朋友"
    if 4/21 < r <= 5/21:
        return "孩童"
    if 5/21 < r <= 6/21:
        return "孩子"
    if 6/21 < r <= 7/21:
        return "少年"
    if 7/21 < r <= 8/21:
        return "过客"
    if 8/21 < r <= 9/21:
        return "归人"
    if 9/21 < r <= 10/21:
        return "路人"
    if 10/21 < r <= 11/21:
        return "别人"
    if 11/21 < r <= 12/21:
        return "佳人"
    if 12/21 < r <= 13/21:
        return "小孩"
    if 13/21 < r <= 14/21:
        return "病人"
    if 14/21 < r <= 15/21:
        return "情人"
    if 15/21 < r <= 16/21:
        return "猎人"
    if 16/21 < r <= 17/21:
        return "亲人"
    if 17/21 < r <= 18/21:
        return "陌生人"
    if 18/21 < r <= 19/21:
        return "敌人"
    if 19/21 < r <= 20/21:
        return "孤儿"
    if 20/21 < r <= 21/21:
        return "使者"

def time_noun():
    r = random.random()
    if 0/16 < r <= 1/16:
        return "春天"
    if 1/16 < r <= 2/16:
        return "冬天"
    if 2/16 < r <= 3/16:
        return "秋天"
    if 3/16 < r <= 4/16:
        return "夏天"
    if 4/16 < r <= 5/16:
        return "童年"
    if 5/16 < r <= 6/16:
        return "夜晚"
    if 6/16 < r <= 7/16:
        return "黄昏"
    if 7/16 < r <= 8/16:
        return "三月"
    if 8/16 < r <= 9/16:
        return "七月"
    if 9/16 < r <= 10/16:
        return "季节"
    if 10/16 < r <= 11/16:
        return "冷冬"
    if 11/16 < r <= 12/16:
        return "黑夜"
    if 12/16 < r <= 13/16:
        return "时刻"
    if 13/16 < r <= 14/16:
        return "醒时"
    if 14/16 < r <= 15/16:
        return "黎明"
    if 15/16 < r <= 16/16:
        return "早晨"

def qty_noun():
    r = random.random()
    if 0/34 < r <= 1/34:
        return "一杯烈酒"
    if 1/34 < r <= 2/34:
        return "一盏灯"
    if 2/34 < r <= 3/34:
        return "一秒"
    if 3/34 < r <= 4/34:
        return "一年"
    if 4/34 < r <= 5/34:
        return "一条街"
    if 5/34 < r <= 6/34:
        return "一寸"
    if 6/34 < r <= 7/34:
        return "三寸"
    if 7/34 < r <= 8/34:
        return "一个字"
    if 8/34 < r <= 9/34:
        return "一首歌"
    if 9/34 < r <= 10/34:
        return "一切"
    if 10/34 < r <= 11/34:
        return "一个人"
    if 11/34 < r <= 12/34:
        return "一本书"
    if 12/34 < r <= 13/34:
        return "一颗心"
    if 13/34 < r <= 14/34:
        return "一支笔"
    if 14/34 < r <= 15/34:
        return "有些人"
    if 15/34 < r <= 16/34:
        return "一道谜题"
    if 16/34 < r <= 17/34:
        return "一场梦"
    if 17/34 < r <= 18/34:
        return "一场雨"
    if 18/34 < r <= 19/34:
        return "一生"
    if 19/34 < r <= 20/34:
        return "一双手"
    if 20/34 < r <= 21/34:
        return "一地"
    if 21/34 < r <= 22/34:
        return "一棵树"
    if 22/34 < r <= 23/34:
        return "一身疲倦"
    if 23/34 < r <= 24/34:
        return "亲爱的"
    if 24/34 < r <= 25/34:
        return "脉脉春风"
    if 25/34 < r <= 26/34:
        return "一场空"
    if 26/34 < r <= 27/34:
        return "一场冒险"
    if 27/34 < r <= 28/34:
        return "一壶酒"
    if 28/34 < r <= 29/34:
        return "一句话"
    if 29/34 < r <= 30/34:
        return "一条路"
    if 30/34 < r <= 31/34:
        return "一座城"
    if 31/34 < r <= 32/34:
        return "一线阳光"
    if 32/34 < r <= 33/34:
        return "某个角落"
    if 33/34 < r <= 34/34:
        return "一个人"

def things_noun():
    r = random.random()
    if 0/54 < r <= 1/54:
        return "身躯"
    if 1/54 < r <= 2/54:
        return "瞳孔"
    if 2/54 < r <= 3/54:
        return "手"
    if 3/54 < r <= 4/54:
        return "皑皑白雪"
    if 4/54 < r <= 5/54:
        return "飞蛾"
    if 5/54 < r <= 6/54:
        return "身体"
    if 6/54 < r <= 7/54:
        return "白纸"
    if 7/54 < r <= 8/54:
        return "细雨"
    if 8/54 < r <= 9/54:
        return "酒"
    if 9/54 < r <= 10/54:
        return "窗口"
    if 10/54 < r <= 11/54:
        return "眼睛"
    if 11/54 < r <= 12/54:
        return "莲花"
    if 12/54 < r <= 13/54:
        return "灯火"
    if 13/54 < r <= 14/54:
        return "灯盏"
    if 14/54 < r <= 15/54:
        return "鸟"
    if 15/54 < r <= 16/54:
        return "飞鸟"
    if 16/54 < r <= 17/54:
        return "花瓣"
    if 17/54 < r <= 18/54:
        return "树"
    if 18/54 < r <= 19/54:
        return "书"
    if 19/54 < r <= 20/54:
        return "心"
    if 20/54 < r <= 21/54:
        return "白发"
    if 21/54 < r <= 22/54:
        return "笔"
    if 22/54 < r <= 23/54:
        return "容貌"
    if 23/54 < r <= 24/54:
        return "花香"
    if 24/54 < r <= 25/54:
        return "画像"
    if 25/54 < r <= 26/54:
        return "屋檐"
    if 26/54 < r <= 27/54:
        return "面具"
    if 27/54 < r <= 28/54:
        return "明眸"
    if 28/54 < r <= 29/54:
        return "繁花"
    if 29/54 < r <= 30/54:
        return "丛林"
    if 30/54 < r <= 31/54:
        return "曲调"
    if 31/54 < r <= 32/54:
        return "曲子"
    if 32/54 < r <= 33/54:
        return "川流"
    if 33/54 < r <= 34/54:
        return "青石"
    if 34/54 < r <= 35/54:
        return "河流"
    if 35/54 < r <= 36/54:
        return "蜡烛"
    if 36/54 < r <= 37/54:
        return "乌云"
    if 37/54 < r <= 38/54:
        return "指纹"
    if 38/54 < r <= 39/54:
        return "篱笆"
    if 39/54 < r <= 40/54:
        return "候鸟"
    if 40/54 < r <= 41/54:
        return "玫瑰"
    if 41/54 < r <= 42/54:
        return "路灯"
    if 42/54 < r <= 43/54:
        return "小鹿"
    if 43/54 < r <= 44/54:
        return "羽毛"
    if 44/54 < r <= 45/54:
        return "猎物"
    if 45/54 < r <= 46/54:
        return "长明灯"
    if 46/54 < r <= 47/54:
        return "鱼"
    if 47/54 < r <= 48/54:
        return "猫头鹰"
    if 48/54 < r <= 49/54:
        return "鸽子"
    if 49/54 < r <= 50/54:
        return "木头"
    if 50/54 < r <= 51/54:
        return "鸟笼"
    if 51/54 < r <= 52/54:
        return "风筝"
    if 52/54 < r <= 53/54:
        return "琴弦"
    if 53/54 < r <= 54/54:
        return "枯井"

def place_noun():
    r = random.random()
    if 0/41 < r <= 1/41:
        return "这里"
    if 1/41 < r <= 2/41:
        return "那里"
    if 2/41 < r <= 3/41:
        return "草原"
    if 3/41 < r <= 4/41:
        return "草原上"
    if 4/41 < r <= 5/41:
        return "沙漠"
    if 5/41 < r <= 6/41:
        return "沙漠里"
    if 6/41 < r <= 7/41:
        return "湖面"
    if 7/41 < r <= 8/41:
        return "河"
    if 8/41 < r <= 9/41:
        return "街道"
    if 9/41 < r <= 10/41:
        return "江南"
    if 10/41 < r <= 11/41:
        return "沼泽"
    if 11/41 < r <= 12/41:
        return "村庄"
    if 12/41 < r <= 13/41:
        return "海岸"
    if 13/41 < r <= 14/41:
        return "海岸边"
    if 14/41 < r <= 15/41:
        return "山"
    if 15/41 < r <= 16/41:
        return "大山"
    if 16/41 < r <= 17/41:
        return "海"
    if 17/41 < r <= 18/41:
        return "大海"
    if 18/41 < r <= 19/41:
        return "海边"
    if 19/41 < r <= 20/41:
        return "沧海"
    if 20/41 < r <= 21/41:
        return "石桥"
    if 21/41 < r <= 22/41:
        return "深山"
    if 22/41 < r <= 23/41:
        return "海角"
    if 23/41 < r <= 24/41:
        return "天涯"
    if 24/41 < r <= 25/41:
        return "远处"
    if 25/41 < r <= 26/41:
        return "孤岛"
    if 26/41 < r <= 27/41:
        return "山涧"
    if 27/41 < r <= 28/41:
        return "故乡"
    if 28/41 < r <= 29/41:
        return "路口"
    if 29/41 < r <= 30/41:
        return "瀑布"
    if 30/41 < r <= 31/41:
        return "远山"
    if 31/41 < r <= 32/41:
        return "麦田"
    if 32/41 < r <= 33/41:
        return "岛屿"
    if 33/41 < r <= 34/41:
        return "峡谷"
    if 34/41 < r <= 35/41:
        return "灯塔"
    if 35/41 < r <= 36/41:
        return "湖泊"
    if 36/41 < r <= 37/41:
        return "山峰"
    if 37/41 < r <= 38/41:
        return "高山"
    if 38/41 < r <= 39/41:
        return "尘世"
    if 39/41 < r <= 40/41:
        return "深渊"
    if 40/41 < r <= 41/41:
        return "路上"

def abstract_noun():
    r = random.random()
    if 0/197 < r <= 1/197:
        return "以前"
    if 1/197 < r <= 2/197:
        return "以后"
    if 2/197 < r <= 3/197:
        return "将来"
    if 3/197 < r <= 4/197:
        return "过去"
    if 4/197 < r <= 5/197:
        return "生活"
    if 5/197 < r <= 6/197:
        return "坚持"
    if 6/197 < r <= 7/197:
        return "风景"
    if 7/197 < r <= 8/197:
        return "回忆"
    if 8/197 < r <= 9/197:
        return "燃点"
    if 9/197 < r <= 10/197:
        return "愿望"
    if 10/197 < r <= 11/197:
        return "结局"
    if 11/197 < r <= 12/197:
        return "梦"
    if 12/197 < r <= 13/197:
        return "瞬间"
    if 13/197 < r <= 14/197:
        return "空间"
    if 14/197 < r <= 15/197:
        return "瞬间"
    if 15/197 < r <= 16/197:
        return "流水"
    if 16/197 < r <= 17/197:
        return "改变"
    if 17/197 < r <= 18/197:
        return "故事"
    if 18/197 < r <= 19/197:
        return "一寸"
    if 19/197 < r <= 20/197:
        return "三寸"
    if 20/197 < r <= 21/197:
        return "天"
    if 21/197 < r <= 22/197:
        return "天气"
    if 22/197 < r <= 23/197:
        return "明镜"
    if 23/197 < r <= 24/197:
        return "暖阳"
    if 24/197 < r <= 25/197:
        return "喧嚣"
    if 25/197 < r <= 26/197:
        return "无声"
    if 26/197 < r <= 27/197:
        return "沉默"
    if 27/197 < r <= 28/197:
        return "火焰"
    if 28/197 < r <= 29/197:
        return "神色"
    if 29/197 < r <= 30/197:
        return "眼神"
    if 30/197 < r <= 31/197:
        return "微风"
    if 31/197 < r <= 32/197:
        return "落日"
    if 32/197 < r <= 33/197:
        return "痛"
    if 33/197 < r <= 34/197:
        return "昔年"
    if 34/197 < r <= 35/197:
        return "世间"
    if 35/197 < r <= 36/197:
        return "生命"
    if 36/197 < r <= 37/197:
        return "面前"
    if 37/197 < r <= 38/197:
        return "伤痕"
    if 38/197 < r <= 39/197:
        return "长日"
    if 39/197 < r <= 40/197:
        return "远方"
    if 40/197 < r <= 41/197:
        return "泥沙"
    if 41/197 < r <= 42/197:
        return "大风"
    if 42/197 < r <= 43/197:
        return "过错"
    if 43/197 < r <= 44/197:
        return "病痛"
    if 44/197 < r <= 45/197:
        return "心头"
    if 45/197 < r <= 46/197:
        return "无人"
    if 46/197 < r <= 47/197:
        return "冰雪"
    if 47/197 < r <= 48/197:
        return "岁月"
    if 48/197 < r <= 49/197:
        return "灵魂"
    if 49/197 < r <= 50/197:
        return "自己"
    if 50/197 < r <= 51/197:
        return "绝望"
    if 51/197 < r <= 52/197:
        return "希望"
    if 52/197 < r <= 53/197:
        return "裂缝"
    if 53/197 < r <= 54/197:
        return "伤口"
    if 54/197 < r <= 55/197:
        return "错"
    if 55/197 < r <= 56/197:
        return "佳境"
    if 56/197 < r <= 57/197:
        return "时间"
    if 57/197 < r <= 58/197:
        return "里面"
    if 58/197 < r <= 59/197:
        return "外面"
    if 59/197 < r <= 60/197:
        return "月光"
    if 60/197 < r <= 61/197:
        return "盛夏"
    if 61/197 < r <= 62/197:
        return "笑语"
    if 62/197 < r <= 63/197:
        return "全世界"
    if 63/197 < r <= 64/197:
        return "天地"
    if 64/197 < r <= 65/197:
        return "笑容"
    if 65/197 < r <= 66/197:
        return "风"
    if 66/197 < r <= 67/197:
        return "晨风"
    if 67/197 < r <= 68/197:
        return "旧梦"
    if 68/197 < r <= 69/197:
        return "歌声"
    if 69/197 < r <= 70/197:
        return "利刃"
    if 70/197 < r <= 71/197:
        return "光晕"
    if 71/197 < r <= 72/197:
        return "相遇"
    if 72/197 < r <= 73/197:
        return "初遇"
    if 73/197 < r <= 74/197:
        return "心事"
    if 74/197 < r <= 75/197:
        return "拥抱"
    if 75/197 < r <= 76/197:
        return "星空"
    if 76/197 < r <= 77/197:
        return "回答"
    if 77/197 < r <= 78/197:
        return "死亡"
    if 78/197 < r <= 79/197:
        return "光明"
    if 79/197 < r <= 80/197:
        return "一个字"
    if 80/197 < r <= 81/197:
        return "一首歌"
    if 81/197 < r <= 82/197:
        return "天空"
    if 82/197 < r <= 83/197:
        return "一切"
    if 83/197 < r <= 84/197:
        return "诗歌"
    if 84/197 < r <= 85/197:
        return "诗"
    if 85/197 < r <= 86/197:
        return "年华"
    if 86/197 < r <= 87/197:
        return "世故"
    if 87/197 < r <= 88/197:
        return "玩笑"
    if 88/197 < r <= 89/197:
        return "他人"
    if 89/197 < r <= 90/197:
        return "深处"
    if 90/197 < r <= 91/197:
        return "遗憾"
    if 91/197 < r <= 92/197:
        return "满月"
    if 92/197 < r <= 93/197:
        return "星河"
    if 93/197 < r <= 94/197:
        return "轨道"
    if 94/197 < r <= 95/197:
        return "青春"
    if 95/197 < r <= 96/197:
        return "长途"
    if 96/197 < r <= 97/197:
        return "假面"
    if 97/197 < r <= 98/197:
        return "人世间"
    if 98/197 < r <= 99/197:
        return "再见"
    if 99/197 < r <= 100/197:
        return "秘密"
    if 100/197 < r <= 101/197:
        return "理由"
    if 101/197 < r <= 102/197:
        return "原因"
    if 102/197 < r <= 103/197:
        return "暗香"
    if 103/197 < r <= 104/197:
        return "方向"
    if 104/197 < r <= 105/197:
        return "错误"
    if 105/197 < r <= 106/197:
        return "欢乐"
    if 106/197 < r <= 107/197:
        return "快乐"
    if 107/197 < r <= 108/197:
        return "悲欢"
    if 108/197 < r <= 109/197:
        return "陌路"
    if 109/197 < r <= 110/197:
        return "歌"
    if 110/197 < r <= 111/197:
        return "谜题"
    if 111/197 < r <= 112/197:
        return "深意"
    if 112/197 < r <= 113/197:
        return "安排"
    if 113/197 < r <= 114/197:
        return "思绪"
    if 114/197 < r <= 115/197:
        return "泪水"
    if 115/197 < r <= 116/197:
        return "云影"
    if 116/197 < r <= 117/197:
        return "事情"
    if 117/197 < r <= 118/197:
        return "北方"
    if 118/197 < r <= 119/197:
        return "南方"
    if 119/197 < r <= 120/197:
        return "长久"
    if 120/197 < r <= 121/197:
        return "颜色"
    if 121/197 < r <= 122/197:
        return "模样"
    if 122/197 < r <= 123/197:
        return "断句"
    if 123/197 < r <= 124/197:
        return "心情"
    if 124/197 < r <= 125/197:
        return "斜阳"
    if 125/197 < r <= 126/197:
        return "残阳"
    if 126/197 < r <= 127/197:
        return "时刻"
    if 127/197 < r <= 128/197:
        return "尘土"
    if 128/197 < r <= 129/197:
        return "微命"
    if 129/197 < r <= 130/197:
        return "信念"
    if 130/197 < r <= 131/197:
        return "路途"
    if 131/197 < r <= 132/197:
        return "时光"
    if 132/197 < r <= 133/197:
        return "洪荒"
    if 133/197 < r <= 134/197:
        return "灰尘"
    if 134/197 < r <= 135/197:
        return "流火"
    if 135/197 < r <= 136/197:
        return "春风"
    if 136/197 < r <= 137/197:
        return "声音"
    if 137/197 < r <= 138/197:
        return "山水"
    if 138/197 < r <= 139/197:
        return "喜悦"
    if 139/197 < r <= 140/197:
        return "埋怨"
    if 140/197 < r <= 141/197:
        return "哀愁"
    if 141/197 < r <= 142/197:
        return "冒险"
    if 142/197 < r <= 143/197:
        return "呼喊"
    if 143/197 < r <= 144/197:
        return "呐喊"
    if 144/197 < r <= 145/197:
        return "影子"
    if 145/197 < r <= 146/197:
        return "人影"
    if 146/197 < r <= 147/197:
        return "背影"
    if 147/197 < r <= 148/197:
        return "灰烬"
    if 148/197 < r <= 149/197:
        return "尘埃"
    if 149/197 < r <= 150/197:
        return "花开"
    if 150/197 < r <= 151/197:
        return "明天"
    if 151/197 < r <= 152/197:
        return "昨天"
    if 152/197 < r <= 153/197:
        return "朝夕"
    if 153/197 < r <= 154/197:
        return "潮汐"
    if 154/197 < r <= 155/197:
        return "名字"
    if 155/197 < r <= 156/197:
        return "烟火"
    if 156/197 < r <= 157/197:
        return "何处"
    if 157/197 < r <= 158/197:
        return "明朝"
    if 158/197 < r <= 159/197:
        return "茶香"
    if 159/197 < r <= 160/197:
        return "酒香"
    if 160/197 < r <= 161/197:
        return "海啸"
    if 161/197 < r <= 162/197:
        return "梦呓"
    if 162/197 < r <= 163/197:
        return "地平线"
    if 163/197 < r <= 164/197:
        return "青烟"
    if 164/197 < r <= 165/197:
        return "馈赠"
    if 165/197 < r <= 166/197:
        return "牢笼"
    if 166/197 < r <= 167/197:
        return "拂晓"
    if 167/197 < r <= 168/197:
        return "自由"
    if 168/197 < r <= 169/197:
        return "碎纸"
    if 169/197 < r <= 170/197:
        return "纸屑"
    if 170/197 < r <= 171/197:
        return "倒影"
    if 171/197 < r <= 172/197:
        return "回声"
    if 172/197 < r <= 173/197:
        return "路口"
    if 173/197 < r <= 174/197:
        return "风帆"
    if 174/197 < r <= 175/197:
        return "羽毛"
    if 175/197 < r <= 176/197:
        return "气息"
    if 176/197 < r <= 177/197:
        return "目光"
    if 177/197 < r <= 178/197:
        return "十字路口"
    if 178/197 < r <= 179/197:
        return "梦境"
    if 179/197 < r <= 180/197:
        return "记忆"
    if 180/197 < r <= 181/197:
        return "夕阳"
    if 181/197 < r <= 182/197:
        return "谎言"
    if 182/197 < r <= 183/197:
        return "泡沫"
    if 183/197 < r <= 184/197:
        return "空白"
    if 184/197 < r <= 185/197:
        return "轻蔑"
    if 185/197 < r <= 186/197:
        return "仇敌"
    if 186/197 < r <= 187/197:
        return "饥渴"
    if 187/197 < r <= 188/197:
        return "青苔"
    if 188/197 < r <= 189/197:
        return "烙印"
    if 189/197 < r <= 190/197:
        return "角落"
    if 190/197 < r <= 191/197:
        return "意义"
    if 191/197 < r <= 192/197:
        return "四壁"
    if 192/197 < r <= 193/197:
        return "沙丘"
    if 193/197 < r <= 194/197:
        return "山丘"
    if 194/197 < r <= 195/197:
        return "样貌"
    if 195/197 < r <= 196/197:
        return "暮年"
    if 196/197 < r <= 197/197:
        return "群星"

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

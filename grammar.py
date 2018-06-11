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
    if 0/7 < r <= 1/7:
        return sentence()
    if 1/7 < r <= 2/7:
        return sentence() + punc()
    if 2/7 < r <= 3/7:
        return expr() + punc()
    if 3/7 < r <= 4/7:
        return sentence()
    if 4/7 < r <= 5/7:
        return sentence() + punc()
    if 5/7 < r <= 6/7:
        return expr() + punc()
    if 6/7 < r <= 7/7:
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
    if 0/4 < r <= 1/4:
        return qn_aux() + sentence() + "？"
    if 1/4 < r <= 2/4:
        return qn_aux() + expr() + "？"
    if 2/4 < r <= 3/4:
        return sentence() + "？"
    if 3/4 < r <= 4/4:
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
    if 0/2 < r <= 1/2:
        return "好好"
    if 1/2 < r <= 2/2:
        return "细细"

def verb_prefix():
    r = random.random()
    if 0/29 < r <= 1/29:
        return "可"
    if 1/29 < r <= 2/29:
        return "不可"
    if 2/29 < r <= 3/29:
        return "不愿"
    if 3/29 < r <= 4/29:
        return "为"
    if 4/29 < r <= 5/29:
        return "为了"
    if 5/29 < r <= 6/29:
        return "又"
    if 6/29 < r <= 7/29:
        return "希望"
    if 7/29 < r <= 8/29:
        return "不曾"
    if 8/29 < r <= 9/29:
        return "曾经"
    if 9/29 < r <= 10/29:
        return "如何"
    if 10/29 < r <= 11/29:
        return "便"
    if 11/29 < r <= 12/29:
        return "明明"
    if 12/29 < r <= 13/29:
        return "不必"
    if 13/29 < r <= 14/29:
        return "始终"
    if 14/29 < r <= 15/29:
        return "将"
    if 15/29 < r <= 16/29:
        return "也"
    if 16/29 < r <= 17/29:
        return "被"
    if 17/29 < r <= 18/29:
        return "不"
    if 18/29 < r <= 19/29:
        return "不再"
    if 19/29 < r <= 20/29:
        return "已经"
    if 20/29 < r <= 21/29:
        return "正好"
    if 21/29 < r <= 22/29:
        return "一步步"
    if 22/29 < r <= 23/29:
        return "都"
    if 23/29 < r <= 24/29:
        return "都是"
    if 24/29 < r <= 25/29:
        return "要"
    if 25/29 < r <= 26/29:
        return "往往"
    if 26/29 < r <= 27/29:
        return "宁愿"
    if 27/29 < r <= 28/29:
        return "才"
    if 28/29 < r <= 29/29:
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
    if 0/29 < r <= 1/29:
        return before_people_verb()
    if 1/29 < r <= 2/29:
        return after_people_verb()
    if 2/29 < r <= 3/29:
        return generic_no_object_verb()
    if 3/29 < r <= 4/29:
        return noun()
    if 4/29 < r <= 5/29:
        return before_people_verb() + people_noun()
    if 5/29 < r <= 6/29:
        return before_abstract_verb() + abstract_noun()
    if 6/29 < r <= 7/29:
        return before_abstract_verb() + things_noun()
    if 7/29 < r <= 8/29:
        return before_abstract_verb() + time_noun()
    if 8/29 < r <= 9/29:
        return before_people_verb() + qty_noun()
    if 9/29 < r <= 10/29:
        return before_abstract_verb() + qty_noun()
    if 10/29 < r <= 11/29:
        return before_place_verb() + place_noun()
    if 11/29 < r <= 12/29:
        return people_noun() + after_people_verb()
    if 12/29 < r <= 13/29:
        return noun() + generic_no_object_verb()
    if 13/29 < r <= 14/29:
        return "把" + abstract_noun() + before_abstract_verb()
    if 14/29 < r <= 15/29:
        return "把" + things_noun() + before_abstract_verb()
    if 15/29 < r <= 16/29:
        return "将" + abstract_noun() + before_abstract_verb()
    if 16/29 < r <= 17/29:
        return "像" + noun() + "一样"
    if 17/29 < r <= 18/29:
        return "像" + noun() + "一样" + adj()
    if 18/29 < r <= 19/29:
        return "在" + feelings_adj() + "时"
    if 19/29 < r <= 20/29:
        return noun() + expr_connector() + noun()
    if 20/29 < r <= 21/29:
        return adj() + "如" + noun()
    if 21/29 < r <= 22/29:
        return noun() + "是" + noun()
    if 22/29 < r <= 23/29:
        return noun() + "不是" + noun()
    if 23/29 < r <= 24/29:
        return people_noun() + "没有" + noun()
    if 24/29 < r <= 25/29:
        return pronoun() + "没有" + noun()
    if 25/29 < r <= 26/29:
        return "让" + pronoun() + after_people_verb()
    if 26/29 < r <= 27/29:
        return verb_prefix() + expr()
    if 27/29 < r <= 28/29:
        return "是" + noun()
    if 28/29 < r <= 29/29:
        return "不是" + noun()

def before_people_verb():
    r = random.random()
    if 0/33 < r <= 1/33:
        return "失去"
    if 1/33 < r <= 2/33:
        return "等"
    if 2/33 < r <= 3/33:
        return "离开"
    if 3/33 < r <= 4/33:
        return "背叛"
    if 4/33 < r <= 5/33:
        return "守护"
    if 5/33 < r <= 6/33:
        return "惩罚"
    if 6/33 < r <= 7/33:
        return "问"
    if 7/33 < r <= 8/33:
        return "爱上"
    if 8/33 < r <= 9/33:
        return "爱"
    if 9/33 < r <= 10/33:
        return "拥抱"
    if 10/33 < r <= 11/33:
        return "相信"
    if 11/33 < r <= 12/33:
        return "忘记"
    if 12/33 < r <= 13/33:
        return "记得"
    if 13/33 < r <= 14/33:
        return "拥有"
    if 14/33 < r <= 15/33:
        return "选择" + before_people_verb()
    if 15/33 < r <= 16/33:
        return "做"
    if 16/33 < r <= 17/33:
        return "寻找"
    if 17/33 < r <= 18/33:
        return "握别"
    if 18/33 < r <= 19/33:
        return "迎来"
    if 19/33 < r <= 20/33:
        return "等待"
    if 20/33 < r <= 21/33:
        return "碰到"
    if 21/33 < r <= 22/33:
        return "惊动"
    if 22/33 < r <= 23/33:
        return "拯救"
    if 23/33 < r <= 24/33:
        return "成全"
    if 24/33 < r <= 25/33:
        return "化作"
    if 25/33 < r <= 26/33:
        return "藏着"
    if 26/33 < r <= 27/33:
        return "出现了"
    if 27/33 < r <= 28/33:
        return "推开"
    if 28/33 < r <= 29/33:
        return "告诉"
    if 29/33 < r <= 30/33:
        return "遇见"
    if 30/33 < r <= 31/33:
        return "找不到"
    if 31/33 < r <= 32/33:
        return "沦为"
    if 32/33 < r <= 33/33:
        return "陪伴"

def before_abstract_verb():
    r = random.random()
    if 0/54 < r <= 1/54:
        return "预支"
    if 1/54 < r <= 2/54:
        return "借"
    if 2/54 < r <= 3/54:
        return "借" + pronoun()
    if 3/54 < r <= 4/54:
        return "看着"
    if 4/54 < r <= 5/54:
        return "看到"
    if 5/54 < r <= 6/54:
        return "报之以"
    if 6/54 < r <= 7/54:
        return "预知"
    if 7/54 < r <= 8/54:
        return "等待"
    if 8/54 < r <= 9/54:
        return "等"
    if 9/54 < r <= 10/54:
        return "品味着"
    if 10/54 < r <= 11/54:
        return "过去"
    if 11/54 < r <= 12/54:
        return "透支"
    if 12/54 < r <= 13/54:
        return "吹走"
    if 13/54 < r <= 14/54:
        return "化作"
    if 14/54 < r <= 15/54:
        return "品味"
    if 15/54 < r <= 16/54:
        return "藏着"
    if 16/54 < r <= 17/54:
        return "胜过"
    if 17/54 < r <= 18/54:
        return "感受到"
    if 18/54 < r <= 19/54:
        return "用"
    if 19/54 < r <= 20/54:
        return "将"
    if 20/54 < r <= 21/54:
        return "跌落"
    if 21/54 < r <= 22/54:
        return "画着"
    if 22/54 < r <= 23/54:
        return "画上"
    if 23/54 < r <= 24/54:
        return "吹走"
    if 24/54 < r <= 25/54:
        return "看尽"
    if 25/54 < r <= 26/54:
        return "没有"
    if 26/54 < r <= 27/54:
        return "绕过"
    if 27/54 < r <= 28/54:
        return "推开"
    if 28/54 < r <= 29/54:
        return "织出"
    if 29/54 < r <= 30/54:
        return "映照"
    if 30/54 < r <= 31/54:
        return "空有"
    if 31/54 < r <= 32/54:
        return "虚度"
    if 32/54 < r <= 33/54:
        return "照亮"
    if 33/54 < r <= 34/54:
        return "铭记"
    if 34/54 < r <= 35/54:
        return "期待"
    if 35/54 < r <= 36/54:
        return "穿透"
    if 36/54 < r <= 37/54:
        return "砸碎"
    if 37/54 < r <= 38/54:
        return "烧热"
    if 38/54 < r <= 39/54:
        return "扑灭"
    if 39/54 < r <= 40/54:
        return "找不到"
    if 40/54 < r <= 41/54:
        return "空余"
    if 41/54 < r <= 42/54:
        return "错付"
    if 42/54 < r <= 43/54:
        return "多"
    if 43/54 < r <= 44/54:
        return "沦为"
    if 44/54 < r <= 45/54:
        return "当是"
    if 45/54 < r <= 46/54:
        return "打败"
    if 46/54 < r <= 47/54:
        return "宣告"
    if 47/54 < r <= 48/54:
        return "折断"
    if 48/54 < r <= 49/54:
        return "篆刻"
    if 49/54 < r <= 50/54:
        return "背负"
    if 50/54 < r <= 51/54:
        return "逃离"
    if 51/54 < r <= 52/54:
        return "孕育"
    if 52/54 < r <= 53/54:
        return "假装"
    if 53/54 < r <= 54/54:
        return "对待"

def before_place_verb():
    r = random.random()
    if 0/28 < r <= 1/28:
        return "走到"
    if 1/28 < r <= 2/28:
        return "离开"
    if 2/28 < r <= 3/28:
        return "来到"
    if 3/28 < r <= 4/28:
        return "埋在"
    if 4/28 < r <= 5/28:
        return "藏在"
    if 5/28 < r <= 6/28:
        return "行走在"
    if 6/28 < r <= 7/28:
        return "跌落"
    if 7/28 < r <= 8/28:
        return "翻越"
    if 8/28 < r <= 9/28:
        return "路经"
    if 9/28 < r <= 10/28:
        return "经过"
    if 10/28 < r <= 11/28:
        return "栖身"
    if 11/28 < r <= 12/28:
        return "飞入"
    if 12/28 < r <= 13/28:
        return "绕过"
    if 13/28 < r <= 14/28:
        return "驻守"
    if 14/28 < r <= 15/28:
        return "伫立"
    if 15/28 < r <= 16/28:
        return "跋涉"
    if 16/28 < r <= 17/28:
        return "映照"
    if 17/28 < r <= 18/28:
        return "站在"
    if 18/28 < r <= 19/28:
        return "照亮"
    if 19/28 < r <= 20/28:
        return "沿着"
    if 20/28 < r <= 21/28:
        return "怀着"
    if 21/28 < r <= 22/28:
        return "坐在"
    if 22/28 < r <= 23/28:
        return "徘徊于"
    if 23/28 < r <= 24/28:
        return "穿越"
    if 24/28 < r <= 25/28:
        return "找不到"
    if 25/28 < r <= 26/28:
        return "住在"
    if 26/28 < r <= 27/28:
        return "望断"
    if 27/28 < r <= 28/28:
        return "奔驰在"

def after_people_verb():
    r = random.random()
    if 0/38 < r <= 1/38:
        return "明白"
    if 1/38 < r <= 2/38:
        return "说"
    if 2/38 < r <= 3/38:
        return "走"
    if 3/38 < r <= 4/38:
        return "离开"
    if 4/38 < r <= 5/38:
        return "来"
    if 5/38 < r <= 6/38:
        return "记得"
    if 6/38 < r <= 7/38:
        return "听得"
    if 7/38 < r <= 8/38:
        return "感叹"
    if 8/38 < r <= 9/38:
        return "喜欢"
    if 9/38 < r <= 10/38:
        return "觉得"
    if 10/38 < r <= 11/38:
        return "出现"
    if 11/38 < r <= 12/38:
        return "怕"
    if 12/38 < r <= 13/38:
        return "害怕"
    if 13/38 < r <= 14/38:
        return "知道"
    if 14/38 < r <= 15/38:
        return "承认"
    if 15/38 < r <= 16/38:
        return "选择"
    if 16/38 < r <= 17/38:
        return "走过"
    if 17/38 < r <= 18/38:
        return "后退"
    if 18/38 < r <= 19/38:
        return "靠近"
    if 19/38 < r <= 20/38:
        return "重逢"
    if 20/38 < r <= 21/38:
        return "沉醉"
    if 21/38 < r <= 22/38:
        return "流浪"
    if 22/38 < r <= 23/38:
        return "愿意"
    if 23/38 < r <= 24/38:
        return "下山"
    if 24/38 < r <= 25/38:
        return "期待"
    if 25/38 < r <= 26/38:
        return "徘徊"
    if 26/38 < r <= 27/38:
        return "舍不得"
    if 27/38 < r <= 28/38:
        return "舍得"
    if 28/38 < r <= 29/38:
        return "仰望"
    if 29/38 < r <= 30/38:
        return "写字"
    if 30/38 < r <= 31/38:
        return "生活"
    if 31/38 < r <= 32/38:
        return "坚持"
    if 32/38 < r <= 33/38:
        return "不辞而别"
    if 33/38 < r <= 34/38:
        return "开口"
    if 34/38 < r <= 35/38:
        return "不用" + after_people_verb()
    if 35/38 < r <= 36/38:
        return "不要" + after_people_verb()
    if 36/38 < r <= 37/38:
        return "终老"
    if 37/38 < r <= 38/38:
        return "衰老"

def generic_no_object_verb():
    r = random.random()
    if 0/67 < r <= 1/67:
        return "离开"
    if 1/67 < r <= 2/67:
        return "来"
    if 2/67 < r <= 3/67:
        return "记得"
    if 3/67 < r <= 4/67:
        return "承受"
    if 4/67 < r <= 5/67:
        return "过去"
    if 5/67 < r <= 6/67:
        return "已经" + generic_no_object_verb()
    if 6/67 < r <= 7/67:
        return generic_no_object_verb() + "了"
    if 7/67 < r <= 8/67:
        return "下沉"
    if 8/67 < r <= 9/67:
        return "跌落"
    if 9/67 < r <= 10/67:
        return "盛开"
    if 10/67 < r <= 11/67:
        return "走过"
    if 11/67 < r <= 12/67:
        return "存在"
    if 12/67 < r <= 13/67:
        return "下雪"
    if 13/67 < r <= 14/67:
        return "放手"
    if 14/67 < r <= 15/67:
        return "松手"
    if 15/67 < r <= 16/67:
        return "浮动"
    if 16/67 < r <= 17/67:
        return "没有"
    if 17/67 < r <= 18/67:
        return "失重"
    if 18/67 < r <= 19/67:
        return "冻结"
    if 19/67 < r <= 20/67:
        return "受伤"
    if 20/67 < r <= 21/67:
        return "痊愈"
    if 21/67 < r <= 22/67:
        return "摇晃"
    if 22/67 < r <= 23/67:
        return "明灭"
    if 23/67 < r <= 24/67:
        return "流浪"
    if 24/67 < r <= 25/67:
        return "消融"
    if 25/67 < r <= 26/67:
        return "融化"
    if 26/67 < r <= 27/67:
        return "沉醉"
    if 27/67 < r <= 28/67:
        return "重逢"
    if 28/67 < r <= 29/67:
        return "未完"
    if 29/67 < r <= 30/67:
        return "苏醒"
    if 30/67 < r <= 31/67:
        return "愿意"
    if 31/67 < r <= 32/67:
        return "沿途"
    if 32/67 < r <= 33/67:
        return "飞扬"
    if 33/67 < r <= 34/67:
        return "飘零"
    if 34/67 < r <= 35/67:
        return "错过"
    if 35/67 < r <= 36/67:
        return "让" + noun() + generic_no_object_verb()
    if 36/67 < r <= 37/67:
        return "沸腾"
    if 37/67 < r <= 38/67:
        return "碎"
    if 38/67 < r <= 39/67:
        return "念念不忘"
    if 39/67 < r <= 40/67:
        return "砸碎"
    if 40/67 < r <= 41/67:
        return "可以"
    if 41/67 < r <= 42/67:
        return "不可以"
    if 42/67 < r <= 43/67:
        return "仰望"
    if 43/67 < r <= 44/67:
        return "写字"
    if 44/67 < r <= 45/67:
        return "生活"
    if 45/67 < r <= 46/67:
        return "下雨"
    if 46/67 < r <= 47/67:
        return "悬空"
    if 47/67 < r <= 48/67:
        return "伤人"
    if 48/67 < r <= 49/67:
        return "高悬空中"
    if 49/67 < r <= 50/67:
        return "散落"
    if 50/67 < r <= 51/67:
        return "散落一地"
    if 51/67 < r <= 52/67:
        return "冒险"
    if 52/67 < r <= 53/67:
        return "干涸"
    if 53/67 < r <= 54/67:
        return "已经" + generic_no_object_verb()
    if 54/67 < r <= 55/67:
        return "虽然" + generic_no_object_verb()
    if 55/67 < r <= 56/67:
        return "不用" + generic_no_object_verb()
    if 56/67 < r <= 57/67:
        return "不要" + generic_no_object_verb()
    if 57/67 < r <= 58/67:
        return "浮想联翩"
    if 58/67 < r <= 59/67:
        return "归零"
    if 59/67 < r <= 60/67:
        return "挑灯"
    if 60/67 < r <= 61/67:
        return "停息"
    if 61/67 < r <= 62/67:
        return "起风"
    if 62/67 < r <= 63/67:
        return "挣扎"
    if 63/67 < r <= 64/67:
        return "回想"
    if 64/67 < r <= 65/67:
        return "停顿"
    if 65/67 < r <= 66/67:
        return "翻涌"
    if 66/67 < r <= 67/67:
        return "奔驰"

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
    if 0/12 < r <= 1/12:
        return "小小"
    if 1/12 < r <= 2/12:
        return "大"
    if 2/12 < r <= 3/12:
        return "傻"
    if 3/12 < r <= 4/12:
        return "不够"
    if 4/12 < r <= 5/12:
        return "辽远"
    if 5/12 < r <= 6/12:
        return "急"
    if 6/12 < r <= 7/12:
        return "匆匆"
    if 7/12 < r <= 8/12:
        return "同行"
    if 8/12 < r <= 9/12:
        return "短"
    if 9/12 < r <= 10/12:
        return "阵阵"
    if 10/12 < r <= 11/12:
        return "一直"
    if 11/12 < r <= 12/12:
        return "绵绵"

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
    if 0/123 < r <= 1/123:
        return feelings_adj()
    if 1/123 < r <= 2/123:
        return feelings_adj()
    if 2/123 < r <= 3/123:
        return feelings_adj()
    if 3/123 < r <= 4/123:
        return "繁荣"
    if 4/123 < r <= 5/123:
        return "不言而喻"
    if 5/123 < r <= 6/123:
        return "最终"
    if 6/123 < r <= 7/123:
        return "藏起来"
    if 7/123 < r <= 8/123:
        return "鲁莽"
    if 8/123 < r <= 9/123:
        return "磊落"
    if 9/123 < r <= 10/123:
        return "庄严"
    if 10/123 < r <= 11/123:
        return "温暖"
    if 11/123 < r <= 12/123:
        return "温柔"
    if 12/123 < r <= 13/123:
        return "柔软"
    if 13/123 < r <= 14/123:
        return "磊落"
    if 14/123 < r <= 15/123:
        return "最初"
    if 15/123 < r <= 16/123:
        return "平庸"
    if 16/123 < r <= 17/123:
        return "无动于衷"
    if 17/123 < r <= 18/123:
        return "黑暗"
    if 18/123 < r <= 19/123:
        return "如旧"
    if 19/123 < r <= 20/123:
        return "曾经"
    if 20/123 < r <= 21/123:
        return "从前"
    if 21/123 < r <= 22/123:
        return "不顾一切"
    if 22/123 < r <= 23/123:
        return "遥远"
    if 23/123 < r <= 24/123:
        return "大火"
    if 24/123 < r <= 25/123:
        return "殷红"
    if 25/123 < r <= 26/123:
        return "漫长"
    if 26/123 < r <= 27/123:
        return "漫漫"
    if 27/123 < r <= 28/123:
        return "满满"
    if 28/123 < r <= 29/123:
        return "漫夜"
    if 29/123 < r <= 30/123:
        return "群星"
    if 30/123 < r <= 31/123:
        return "明朝"
    if 31/123 < r <= 32/123:
        return "恐惧"
    if 32/123 < r <= 33/123:
        return "彻头彻尾"
    if 33/123 < r <= 34/123:
        return "彻底"
    if 34/123 < r <= 35/123:
        return "清澈"
    if 35/123 < r <= 36/123:
        return "失魂落魄"
    if 36/123 < r <= 37/123:
        return "薄情"
    if 37/123 < r <= 38/123:
        return "粉身碎骨"
    if 38/123 < r <= 39/123:
        return "绚烂"
    if 39/123 < r <= 40/123:
        return "自负"
    if 40/123 < r <= 41/123:
        return "软弱"
    if 41/123 < r <= 42/123:
        return "坦白"
    if 42/123 < r <= 43/123:
        return "如花"
    if 43/123 < r <= 44/123:
        return "随意"
    if 44/123 < r <= 45/123:
        return "忧郁"
    if 45/123 < r <= 46/123:
        return "悲伤"
    if 46/123 < r <= 47/123:
        return "欢喜"
    if 47/123 < r <= 48/123:
        return "所有"
    if 48/123 < r <= 49/123:
        return "沉重"
    if 49/123 < r <= 50/123:
        return "污浊"
    if 50/123 < r <= 51/123:
        return "比如"
    if 51/123 < r <= 52/123:
        return "脆弱"
    if 52/123 < r <= 53/123:
        return "不堪"
    if 53/123 < r <= 54/123:
        return "黑白"
    if 54/123 < r <= 55/123:
        return "装模作样"
    if 55/123 < r <= 56/123:
        return "复杂"
    if 56/123 < r <= 57/123:
        return "一个人"
    if 57/123 < r <= 58/123:
        return "澄澈"
    if 58/123 < r <= 59/123:
        return "苟且"
    if 59/123 < r <= 60/123:
        return "诗意"
    if 60/123 < r <= 61/123:
        return "简单"
    if 61/123 < r <= 62/123:
        return "多余"
    if 62/123 < r <= 63/123:
        return "一无所有"
    if 63/123 < r <= 64/123:
        return "流浪"
    if 64/123 < r <= 65/123:
        return "从容"
    if 65/123 < r <= 66/123:
        return "迟钝"
    if 66/123 < r <= 67/123:
        return "苍白"
    if 67/123 < r <= 68/123:
        return "明亮"
    if 68/123 < r <= 69/123:
        return "冰凉"
    if 69/123 < r <= 70/123:
        return "舒适"
    if 70/123 < r <= 71/123:
        return "悸动"
    if 71/123 < r <= 72/123:
        return "懦弱"
    if 72/123 < r <= 73/123:
        return "傻傻"
    if 73/123 < r <= 74/123:
        return "漫漫"
    if 74/123 < r <= 75/123:
        return "烈烈"
    if 75/123 < r <= 76/123:
        return "恰到好处"
    if 76/123 < r <= 77/123:
        return "鲜明"
    if 77/123 < r <= 78/123:
        return "每一个"
    if 78/123 < r <= 79/123:
        return "好"
    if 79/123 < r <= 80/123:
        return "安宁"
    if 80/123 < r <= 81/123:
        return "宁静"
    if 81/123 < r <= 82/123:
        return "黯然"
    if 82/123 < r <= 83/123:
        return "坚定"
    if 83/123 < r <= 84/123:
        return "苦涩"
    if 84/123 < r <= 85/123:
        return "不为人知"
    if 85/123 < r <= 86/123:
        return "不易察觉"
    if 86/123 < r <= 87/123:
        return "骄傲"
    if 87/123 < r <= 88/123:
        return "圆缺"
    if 88/123 < r <= 89/123:
        return "浮光掠影"
    if 89/123 < r <= 90/123:
        return "陈年"
    if 90/123 < r <= 91/123:
        return "云涌"
    if 91/123 < r <= 92/123:
        return "风起云涌"
    if 92/123 < r <= 93/123:
        return "泛黄"
    if 93/123 < r <= 94/123:
        return "落幕"
    if 94/123 < r <= 95/123:
        return "古老"
    if 95/123 < r <= 96/123:
        return "年少"
    if 96/123 < r <= 97/123:
        return "辉煌"
    if 97/123 < r <= 98/123:
        return "模糊"
    if 98/123 < r <= 99/123:
        return "空洞"
    if 99/123 < r <= 100/123:
        return "难"
    if 100/123 < r <= 101/123:
        return "容易"
    if 101/123 < r <= 102/123:
        return "长久"
    if 102/123 < r <= 103/123:
        return "永远"
    if 103/123 < r <= 104/123:
        return "破碎"
    if 104/123 < r <= 105/123:
        return "苦痛"
    if 105/123 < r <= 106/123:
        return "疲乏"
    if 106/123 < r <= 107/123:
        return "疲倦"
    if 107/123 < r <= 108/123:
        return "轰烈"
    if 108/123 < r <= 109/123:
        return "轰轰烈烈"
    if 109/123 < r <= 110/123:
        return "这样"
    if 110/123 < r <= 111/123:
        return "那样"
    if 111/123 < r <= 112/123:
        return "这样"
    if 112/123 < r <= 113/123:
        return "那样"
    if 113/123 < r <= 114/123:
        return "神圣"
    if 114/123 < r <= 115/123:
        return "麻木"
    if 115/123 < r <= 116/123:
        return "安静"
    if 116/123 < r <= 117/123:
        return "失望"
    if 117/123 < r <= 118/123:
        return "空灵"
    if 118/123 < r <= 119/123:
        return "坦率"
    if 119/123 < r <= 120/123:
        return "清冷"
    if 120/123 < r <= 121/123:
        return "孤傲"
    if 121/123 < r <= 122/123:
        return "憔悴"
    if 122/123 < r <= 123/123:
        return "心酸"

def noun():
    r = random.random()
    if 0/39 < r <= 1/39:
        return people_noun()
    if 1/39 < r <= 2/39:
        return things_noun()
    if 2/39 < r <= 3/39:
        return time_noun()
    if 3/39 < r <= 4/39:
        return qty_noun()
    if 4/39 < r <= 5/39:
        return abstract_noun()
    if 5/39 < r <= 6/39:
        return abstract_noun()
    if 6/39 < r <= 7/39:
        return abstract_noun()
    if 7/39 < r <= 8/39:
        return abstract_noun()
    if 8/39 < r <= 9/39:
        return place_noun()
    if 9/39 < r <= 10/39:
        return "那" + people_noun()
    if 10/39 < r <= 11/39:
        return "这" + people_noun()
    if 11/39 < r <= 12/39:
        return "那" + qty_noun()
    if 12/39 < r <= 13/39:
        return "这" + qty_noun()
    if 13/39 < r <= 14/39:
        return pronoun()
    if 14/39 < r <= 15/39:
        return "那个" + pronoun()
    if 15/39 < r <= 16/39:
        return "这个" + time_noun()
    if 16/39 < r <= 17/39:
        return "这个" + things_noun()
    if 17/39 < r <= 18/39:
        return "这" + things_noun()
    if 18/39 < r <= 19/39:
        return "那" + things_noun()
    if 19/39 < r <= 20/39:
        return "那个" + things_noun()
    if 20/39 < r <= 21/39:
        return pronoun() + "的" + things_noun()
    if 21/39 < r <= 22/39:
        return pronoun() + "的" + abstract_noun()
    if 22/39 < r <= 23/39:
        return "这" + abstract_noun()
    if 23/39 < r <= 24/39:
        return "在" + place_noun()
    if 24/39 < r <= 25/39:
        return place_noun()
    if 25/39 < r <= 26/39:
        return people_qty() + people_noun()
    if 26/39 < r <= 27/39:
        return qty() + time_noun()
    if 27/39 < r <= 28/39:
        return qty() + abstract_noun()
    if 28/39 < r <= 29/39:
        return noun_adj()
    if 29/39 < r <= 30/39:
        return noun_adj()
    if 30/39 < r <= 31/39:
        return time_noun() + "里"
    if 31/39 < r <= 32/39:
        return time_noun() + "外"
    if 32/39 < r <= 33/39:
        return qty_noun() + "之外"
    if 33/39 < r <= 34/39:
        return people_noun() + "一样"
    if 34/39 < r <= 35/39:
        return qty_noun() + "一样"
    if 35/39 < r <= 36/39:
        return place_noun() + "一样"
    if 36/39 < r <= 37/39:
        return abstract_noun() + "一样"
    if 37/39 < r <= 38/39:
        return place_noun() + "尽头"
    if 38/39 < r <= 39/39:
        return place_noun() + "尽处"

def people_noun():
    r = random.random()
    if 0/14 < r <= 1/14:
        return "诗人"
    if 1/14 < r <= 2/14:
        return "摆渡人"
    if 2/14 < r <= 3/14:
        return "爱人"
    if 3/14 < r <= 4/14:
        return "朋友"
    if 4/14 < r <= 5/14:
        return "孩童"
    if 5/14 < r <= 6/14:
        return "孩子"
    if 6/14 < r <= 7/14:
        return "少年"
    if 7/14 < r <= 8/14:
        return "过客"
    if 8/14 < r <= 9/14:
        return "归人"
    if 9/14 < r <= 10/14:
        return "一个人"
    if 10/14 < r <= 11/14:
        return "路人"
    if 11/14 < r <= 12/14:
        return "别人"
    if 12/14 < r <= 13/14:
        return "佳人"
    if 13/14 < r <= 14/14:
        return "小孩"

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
        return "暮年"
    if 5/16 < r <= 6/16:
        return "童年"
    if 6/16 < r <= 7/16:
        return "夜晚"
    if 7/16 < r <= 8/16:
        return "黄昏"
    if 8/16 < r <= 9/16:
        return "三月"
    if 9/16 < r <= 10/16:
        return "七月"
    if 10/16 < r <= 11/16:
        return "季节"
    if 11/16 < r <= 12/16:
        return "冷冬"
    if 12/16 < r <= 13/16:
        return "时候"
    if 13/16 < r <= 14/16:
        return "黑夜"
    if 14/16 < r <= 15/16:
        return "时刻"
    if 15/16 < r <= 16/16:
        return "醒时"

def qty_noun():
    r = random.random()
    if 0/29 < r <= 1/29:
        return "一杯烈酒"
    if 1/29 < r <= 2/29:
        return "一盏灯"
    if 2/29 < r <= 3/29:
        return "一秒"
    if 3/29 < r <= 4/29:
        return "一年"
    if 4/29 < r <= 5/29:
        return "一条街"
    if 5/29 < r <= 6/29:
        return "一寸"
    if 6/29 < r <= 7/29:
        return "三寸"
    if 7/29 < r <= 8/29:
        return "一个字"
    if 8/29 < r <= 9/29:
        return "一首歌"
    if 9/29 < r <= 10/29:
        return "一切"
    if 10/29 < r <= 11/29:
        return "一个人"
    if 11/29 < r <= 12/29:
        return "一本书"
    if 12/29 < r <= 13/29:
        return "一颗心"
    if 13/29 < r <= 14/29:
        return "一支笔"
    if 14/29 < r <= 15/29:
        return "有些人"
    if 15/29 < r <= 16/29:
        return "一道谜题"
    if 16/29 < r <= 17/29:
        return "一场梦"
    if 17/29 < r <= 18/29:
        return "一场雨"
    if 18/29 < r <= 19/29:
        return "一生"
    if 19/29 < r <= 20/29:
        return "一双手"
    if 20/29 < r <= 21/29:
        return "一地"
    if 21/29 < r <= 22/29:
        return "一棵树"
    if 22/29 < r <= 23/29:
        return "一身疲倦"
    if 23/29 < r <= 24/29:
        return "亲爱的"
    if 24/29 < r <= 25/29:
        return "脉脉春风"
    if 25/29 < r <= 26/29:
        return "一场空"
    if 26/29 < r <= 27/29:
        return "一场冒险"
    if 27/29 < r <= 28/29:
        return "一壶酒"
    if 28/29 < r <= 29/29:
        return "一句话"

def things_noun():
    r = random.random()
    if 0/37 < r <= 1/37:
        return "身躯"
    if 1/37 < r <= 2/37:
        return "瞳孔"
    if 2/37 < r <= 3/37:
        return "手"
    if 3/37 < r <= 4/37:
        return "皑皑白雪"
    if 4/37 < r <= 5/37:
        return "飞蛾"
    if 5/37 < r <= 6/37:
        return "身体"
    if 6/37 < r <= 7/37:
        return "白纸"
    if 7/37 < r <= 8/37:
        return "细雨"
    if 8/37 < r <= 9/37:
        return "酒"
    if 9/37 < r <= 10/37:
        return "蝴蝶"
    if 10/37 < r <= 11/37:
        return "窗口"
    if 11/37 < r <= 12/37:
        return "眼睛"
    if 12/37 < r <= 13/37:
        return "莲花"
    if 13/37 < r <= 14/37:
        return "灯火"
    if 14/37 < r <= 15/37:
        return "灯盏"
    if 15/37 < r <= 16/37:
        return "鸟"
    if 16/37 < r <= 17/37:
        return "飞鸟"
    if 17/37 < r <= 18/37:
        return "花瓣"
    if 18/37 < r <= 19/37:
        return "树"
    if 19/37 < r <= 20/37:
        return "书"
    if 20/37 < r <= 21/37:
        return "心"
    if 21/37 < r <= 22/37:
        return "白发"
    if 22/37 < r <= 23/37:
        return "笔"
    if 23/37 < r <= 24/37:
        return "容貌"
    if 24/37 < r <= 25/37:
        return "花香"
    if 25/37 < r <= 26/37:
        return "画像"
    if 26/37 < r <= 27/37:
        return "屋檐"
    if 27/37 < r <= 28/37:
        return "玻璃渣"
    if 28/37 < r <= 29/37:
        return "面具"
    if 29/37 < r <= 30/37:
        return "明眸"
    if 30/37 < r <= 31/37:
        return "繁花"
    if 31/37 < r <= 32/37:
        return "丛林"
    if 32/37 < r <= 33/37:
        return "曲调"
    if 33/37 < r <= 34/37:
        return "曲子"
    if 34/37 < r <= 35/37:
        return "川流"
    if 35/37 < r <= 36/37:
        return "青石"
    if 36/37 < r <= 37/37:
        return "河流"

def place_noun():
    r = random.random()
    if 0/23 < r <= 1/23:
        return "这里"
    if 1/23 < r <= 2/23:
        return "那里"
    if 2/23 < r <= 3/23:
        return "右边"
    if 3/23 < r <= 4/23:
        return "左边"
    if 4/23 < r <= 5/23:
        return "草原"
    if 5/23 < r <= 6/23:
        return "草原上"
    if 6/23 < r <= 7/23:
        return "沙漠"
    if 7/23 < r <= 8/23:
        return "沙漠里"
    if 8/23 < r <= 9/23:
        return "湖面"
    if 9/23 < r <= 10/23:
        return "河"
    if 10/23 < r <= 11/23:
        return "街道"
    if 11/23 < r <= 12/23:
        return "江南"
    if 12/23 < r <= 13/23:
        return "沼泽"
    if 13/23 < r <= 14/23:
        return "村庄"
    if 14/23 < r <= 15/23:
        return "海岸"
    if 15/23 < r <= 16/23:
        return "海岸边"
    if 16/23 < r <= 17/23:
        return "山"
    if 17/23 < r <= 18/23:
        return "大山"
    if 18/23 < r <= 19/23:
        return "海"
    if 19/23 < r <= 20/23:
        return "大海"
    if 20/23 < r <= 21/23:
        return "海边"
    if 21/23 < r <= 22/23:
        return "沧海"
    if 22/23 < r <= 23/23:
        return "石桥"

def abstract_noun():
    r = random.random()
    if 0/160 < r <= 1/160:
        return "以前"
    if 1/160 < r <= 2/160:
        return "以后"
    if 2/160 < r <= 3/160:
        return "将来"
    if 3/160 < r <= 4/160:
        return "过去"
    if 4/160 < r <= 5/160:
        return "路上"
    if 5/160 < r <= 6/160:
        return "路"
    if 6/160 < r <= 7/160:
        return "生活"
    if 7/160 < r <= 8/160:
        return "坚持"
    if 8/160 < r <= 9/160:
        return "风景"
    if 9/160 < r <= 10/160:
        return "回忆"
    if 10/160 < r <= 11/160:
        return "燃点"
    if 11/160 < r <= 12/160:
        return "愿望"
    if 12/160 < r <= 13/160:
        return "结局"
    if 13/160 < r <= 14/160:
        return "梦"
    if 14/160 < r <= 15/160:
        return "瞬间"
    if 15/160 < r <= 16/160:
        return "空间"
    if 16/160 < r <= 17/160:
        return "瞬间"
    if 17/160 < r <= 18/160:
        return "流水"
    if 18/160 < r <= 19/160:
        return "改变"
    if 19/160 < r <= 20/160:
        return "故事"
    if 20/160 < r <= 21/160:
        return "一寸"
    if 21/160 < r <= 22/160:
        return "三寸"
    if 22/160 < r <= 23/160:
        return "天"
    if 23/160 < r <= 24/160:
        return "天气"
    if 24/160 < r <= 25/160:
        return "明镜"
    if 25/160 < r <= 26/160:
        return "暖阳"
    if 26/160 < r <= 27/160:
        return "喧嚣"
    if 27/160 < r <= 28/160:
        return "无声"
    if 28/160 < r <= 29/160:
        return "沉默"
    if 29/160 < r <= 30/160:
        return "火焰"
    if 30/160 < r <= 31/160:
        return "神色"
    if 31/160 < r <= 32/160:
        return "眼神"
    if 32/160 < r <= 33/160:
        return "微风"
    if 33/160 < r <= 34/160:
        return "落日"
    if 34/160 < r <= 35/160:
        return "痛"
    if 35/160 < r <= 36/160:
        return "昔年"
    if 36/160 < r <= 37/160:
        return "世间"
    if 37/160 < r <= 38/160:
        return "生命"
    if 38/160 < r <= 39/160:
        return "面前"
    if 39/160 < r <= 40/160:
        return "伤痕"
    if 40/160 < r <= 41/160:
        return "长日"
    if 41/160 < r <= 42/160:
        return "远方"
    if 42/160 < r <= 43/160:
        return "泥沙"
    if 43/160 < r <= 44/160:
        return "大风"
    if 44/160 < r <= 45/160:
        return "过错"
    if 45/160 < r <= 46/160:
        return "病痛"
    if 46/160 < r <= 47/160:
        return "心头"
    if 47/160 < r <= 48/160:
        return "无人"
    if 48/160 < r <= 49/160:
        return "冰雪"
    if 49/160 < r <= 50/160:
        return "岁月"
    if 50/160 < r <= 51/160:
        return "灵魂"
    if 51/160 < r <= 52/160:
        return "自己"
    if 52/160 < r <= 53/160:
        return "绝望"
    if 53/160 < r <= 54/160:
        return "希望"
    if 54/160 < r <= 55/160:
        return "裂缝"
    if 55/160 < r <= 56/160:
        return "伤口"
    if 56/160 < r <= 57/160:
        return "错"
    if 57/160 < r <= 58/160:
        return "歧路"
    if 58/160 < r <= 59/160:
        return "佳境"
    if 59/160 < r <= 60/160:
        return "时间"
    if 60/160 < r <= 61/160:
        return "里面"
    if 61/160 < r <= 62/160:
        return "外面"
    if 62/160 < r <= 63/160:
        return "月光"
    if 63/160 < r <= 64/160:
        return "盛夏"
    if 64/160 < r <= 65/160:
        return "笑语"
    if 65/160 < r <= 66/160:
        return "全世界"
    if 66/160 < r <= 67/160:
        return "天地"
    if 67/160 < r <= 68/160:
        return "笑容"
    if 68/160 < r <= 69/160:
        return "风"
    if 69/160 < r <= 70/160:
        return "晨风"
    if 70/160 < r <= 71/160:
        return "旧梦"
    if 71/160 < r <= 72/160:
        return "歌声"
    if 72/160 < r <= 73/160:
        return "利刃"
    if 73/160 < r <= 74/160:
        return "光晕"
    if 74/160 < r <= 75/160:
        return "相遇"
    if 75/160 < r <= 76/160:
        return "初遇"
    if 76/160 < r <= 77/160:
        return "心事"
    if 77/160 < r <= 78/160:
        return "拥抱"
    if 78/160 < r <= 79/160:
        return "星空"
    if 79/160 < r <= 80/160:
        return "回答"
    if 80/160 < r <= 81/160:
        return "死亡"
    if 81/160 < r <= 82/160:
        return "光明"
    if 82/160 < r <= 83/160:
        return "一个字"
    if 83/160 < r <= 84/160:
        return "一首歌"
    if 84/160 < r <= 85/160:
        return "天空"
    if 85/160 < r <= 86/160:
        return "一切"
    if 86/160 < r <= 87/160:
        return "诗歌"
    if 87/160 < r <= 88/160:
        return "诗"
    if 88/160 < r <= 89/160:
        return "年华"
    if 89/160 < r <= 90/160:
        return "世故"
    if 90/160 < r <= 91/160:
        return "玩笑"
    if 91/160 < r <= 92/160:
        return "他人"
    if 92/160 < r <= 93/160:
        return "深处"
    if 93/160 < r <= 94/160:
        return "遗憾"
    if 94/160 < r <= 95/160:
        return "满月"
    if 95/160 < r <= 96/160:
        return "星河"
    if 96/160 < r <= 97/160:
        return "轨道"
    if 97/160 < r <= 98/160:
        return "青春"
    if 98/160 < r <= 99/160:
        return "长途"
    if 99/160 < r <= 100/160:
        return "假面"
    if 100/160 < r <= 101/160:
        return "人世间"
    if 101/160 < r <= 102/160:
        return "再见"
    if 102/160 < r <= 103/160:
        return "秘密"
    if 103/160 < r <= 104/160:
        return "理由"
    if 104/160 < r <= 105/160:
        return "原因"
    if 105/160 < r <= 106/160:
        return "暗香"
    if 106/160 < r <= 107/160:
        return "方向"
    if 107/160 < r <= 108/160:
        return "错误"
    if 108/160 < r <= 109/160:
        return "欢乐"
    if 109/160 < r <= 110/160:
        return "快乐"
    if 110/160 < r <= 111/160:
        return "悲欢"
    if 111/160 < r <= 112/160:
        return "陌路"
    if 112/160 < r <= 113/160:
        return "歌"
    if 113/160 < r <= 114/160:
        return "谜题"
    if 114/160 < r <= 115/160:
        return "深意"
    if 115/160 < r <= 116/160:
        return "安排"
    if 116/160 < r <= 117/160:
        return "思绪"
    if 117/160 < r <= 118/160:
        return "泪水"
    if 118/160 < r <= 119/160:
        return "云影"
    if 119/160 < r <= 120/160:
        return "事情"
    if 120/160 < r <= 121/160:
        return "北方"
    if 121/160 < r <= 122/160:
        return "南方"
    if 122/160 < r <= 123/160:
        return "长久"
    if 123/160 < r <= 124/160:
        return "颜色"
    if 124/160 < r <= 125/160:
        return "模样"
    if 125/160 < r <= 126/160:
        return "断句"
    if 126/160 < r <= 127/160:
        return "心情"
    if 127/160 < r <= 128/160:
        return "斜阳"
    if 128/160 < r <= 129/160:
        return "残阳"
    if 129/160 < r <= 130/160:
        return "时刻"
    if 130/160 < r <= 131/160:
        return "尘土"
    if 131/160 < r <= 132/160:
        return "微命"
    if 132/160 < r <= 133/160:
        return "信念"
    if 133/160 < r <= 134/160:
        return "路途"
    if 134/160 < r <= 135/160:
        return "时光"
    if 135/160 < r <= 136/160:
        return "洪荒"
    if 136/160 < r <= 137/160:
        return "灰尘"
    if 137/160 < r <= 138/160:
        return "流火"
    if 138/160 < r <= 139/160:
        return "春风"
    if 139/160 < r <= 140/160:
        return "声音"
    if 140/160 < r <= 141/160:
        return "山水"
    if 141/160 < r <= 142/160:
        return "喜悦"
    if 142/160 < r <= 143/160:
        return "埋怨"
    if 143/160 < r <= 144/160:
        return "哀愁"
    if 144/160 < r <= 145/160:
        return "冒险"
    if 145/160 < r <= 146/160:
        return "呼喊"
    if 146/160 < r <= 147/160:
        return "呐喊"
    if 147/160 < r <= 148/160:
        return "影子"
    if 148/160 < r <= 149/160:
        return "人影"
    if 149/160 < r <= 150/160:
        return "背影"
    if 150/160 < r <= 151/160:
        return "灰烬"
    if 151/160 < r <= 152/160:
        return "尘埃"
    if 152/160 < r <= 153/160:
        return "花开"
    if 153/160 < r <= 154/160:
        return "明天"
    if 154/160 < r <= 155/160:
        return "昨天"
    if 155/160 < r <= 156/160:
        return "朝夕"
    if 156/160 < r <= 157/160:
        return "潮汐"
    if 157/160 < r <= 158/160:
        return "名字"
    if 158/160 < r <= 159/160:
        return "烟火"
    if 159/160 < r <= 160/160:
        return "何处"

def connector():
    r = random.random()
    if 0/21 < r <= 1/21:
        return "可是"
    if 1/21 < r <= 2/21:
        return "可"
    if 2/21 < r <= 3/21:
        return "然而"
    if 3/21 < r <= 4/21:
        return "但是"
    if 4/21 < r <= 5/21:
        return "于是"
    if 5/21 < r <= 6/21:
        return "所以"
    if 6/21 < r <= 7/21:
        return "原来"
    if 7/21 < r <= 8/21:
        return "如果"
    if 8/21 < r <= 9/21:
        return "如同"
    if 9/21 < r <= 10/21:
        return "后来"
    if 10/21 < r <= 11/21:
        return "虽然"
    if 11/21 < r <= 12/21:
        return "还是"
    if 12/21 < r <= 13/21:
        return "若"
    if 13/21 < r <= 14/21:
        return "却"
    if 14/21 < r <= 15/21:
        return "其实"
    if 15/21 < r <= 16/21:
        return "便"
    if 16/21 < r <= 17/21:
        return "总是"
    if 17/21 < r <= 18/21:
        return "终于"
    if 18/21 < r <= 19/21:
        return "而"
    if 19/21 < r <= 20/21:
        return "本来"
    if 20/21 < r <= 21/21:
        return "总有"

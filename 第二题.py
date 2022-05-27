# -*- coding: utf-8 -*-
"""
Created on Fri May 27 14:48:07 2022

@author: heyuqing
"""

long_text = """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""
#str转换成list 
text = long_text.split('\n')
#text列表中第二个为name(第一部分)  第三个为lei（第二部分）
name = text[1]
lei =  text[2]
titles=[]
#第三部分为sub_fund
sub_fund_num = long_text.count('.')
list_string='.'
#找到text中带.的元素，.后面的字符串填充到titles列表中
all_titles=list(filter(lambda text:all([word in text for word in list_string]),text))
for i in range(0,sub_fund_num): 
    text.index(all_titles[i])
    begin=all_titles[i].find('.')
    temp=all_titles[i]
    title=temp[(begin+1):]
    titles.append(title)

a = long_text.count('.')
a1 = long_text.find('.')
a2 = long_text.find('FUND')
a5 = a1;
a6 = a2;
 
#定义数组存放内容
LU = []
isin = []
sub_fund = []
sub = []
SUB = []
fu = []

#lu数组
c = long_text.find('LU')
c1 = long_text.count('LU')
for i in range(0,a):
    "从fund开始到下一个.结束，将这里的LU放入素组"
    a3 = a1;
    a1 = long_text.find('.', a3 + 1);
    #从第一个“.”开始遍历，找到下一个点
    a4 = long_text.find('FUND',a3,a1)
    #从第一个“.”开始遍历，到下一个“.”结束，找到fund的位置
    c2 = long_text.count('LU', a4, a1);
    #从fund开始遍历，到下一个点结束，统计数字LU+数字的量
    c = long_text.find('LU', a4, a1);
    #从从fund开始遍历，到下一个点结束，找到第一个LU+数字的位置
    for j in range(0,c2):
        c5 = c
        LU.append(j)
        LU[j] = long_text[c5:c+12]
        c = long_text.find('LU', c5+1, a1)
    isin.append(i)
    isin.append(LU)
    LU = []
 
for i in range(0,len(isin)):
    if type(isin[i]) == int:
        sub.append(i)
    else:
        continue

str1 = "title"
str2 = "isin"
str3 = "："
str4 = '\n'
for j in range(0,a):
    sub_fund.append(j)
    e=sub[j]
    SUB.append(j)
    SUB[j] = ["title：",titles[j],'\n',"isin:",isin[e+1]]
    sub_fund.append({str1:titles[j],str2:isin[e+1]})
 
for l in range(0,len(sub_fund)):
    if type(sub_fund[l]) == int:
        fu.append(l)
    else:
        continue
 
sub_fund = [sub_fund[i] for i in range(len(sub_fund)) if(i not in fu)]
output = {
     'name': name,
     'lei': lei,
     'sub_fund':sub_fund
 
 }
print(output)
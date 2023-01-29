import re

"""
CAMERA A
  <area alt="" title="" href="" coords="701,483,1086,867" shape="rect">
  <area alt="" title="" href="" coords="1217,531,1891,867" shape="rect">
  <area alt="" title="" href="" coords="768,322,1045,469" shape="rect">
  <area alt="" title="" href="" coords="1166,324,1666,567" shape="rect">
  <area alt="" title="" href="" coords="838,41,1000,234" shape="rect">
  <area alt="" title="" href="" coords="1078,63,1397,322" shape="rect">
  <area alt="" title="" href="" coords="549,111,822,477" shape="rect">
CAMERA B
  <area alt="" title="" href="" coords="10,537,602,936" shape="rect">
  <area alt="" title="" href="" coords="783,551,1092,889" shape="rect">
  <area alt="" title="" href="" coords="254,412,703,680" shape="rect">
  <area alt="" title="" href="" coords="821,416,1076,596" shape="rect">
  <area alt="" title="" href="" coords="527,193,780,430" shape="rect">
  <area alt="" title="" href="" coords="897,139,1022,430" shape="rect">
CAMERA C
  <area alt="" title="" href="" coords="553,830,1358,1078" shape="rect">
  <area alt="" title="" href="" coords="223,713,610,1018" shape="rect">
  <area alt="" title="" href="" coords="791,352,990,516" shape="rect">
  <area alt="" title="" href="" coords="76,529,1137,871" shape="rect">
CAMERA D  
  <area alt="" title="" href="" coords="867,928,1412,1076" shape="rect">
  <area alt="" title="" href="" coords="1477,924,1911,1075" shape="rect">
  <area alt="" title="" href="" coords="832,717,1178,944" shape="rect">
  <area alt="" title="" href="" coords="1260,717,1665,965" shape="rect">
  <area alt="" title="" href="" coords="1180,559,1565,752" shape="rect">
  <area alt="" title="" href="" coords="781,400,1153,682" shape="rect">
"""

data = """
  <area alt="" title="" href="" coords="527,869,1194,1076" shape="rect">
  <area alt="" title="" href="" coords="1428,834,1866,1078" shape="rect">
  <area alt="" title="" href="" coords="828,611,1225,912" shape="rect">
  <area alt="" title="" href="" coords="1330,613,1790,873" shape="rect">
  <area alt="" title="" href="" coords="703,438,1012,649" shape="rect">
  <area alt="" title="" href="" coords="1047,414,1405,610" shape="rect">
"""

res = []
for match in re.finditer('coords="([0-9,]+)"', data):
    temp = match.group(1)
    x1,y1,x2,y2 = map(int, temp.split(','))
    res.append([[x1,y1],[x2,y1],[x2,y2],[x1,y2]])

print(res)
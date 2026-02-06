#Day3:List(列表)与Tuple(元组)

#---1.list(用方括号【】)---
my_portfolio=["ETH","BTC","SOL"]

#买入DOGE
my_portfolio.append("DOGE")

#动作：卖掉SOL
#0：ETH, 1:BTC, 2;SOL
my_portfolio.pop(2)

#---2.元组Tuple(用小括号（）)---
#不可修改
config=("127.0.0.1",8080)

#---3.打印结果---
print("当前持仓：",my_portfolio)
print("第一大持仓",my_portfolio[0])
print("系统配置",config)

#Day5 字典
#创建初始账本
print("\n---Dictionary Practice---")
exam_scores={"Alice":85,"Bob":92,"Charlie":78}
print("初始账本：",exam_scores)

#1.查找Bob考了多少分
print(f"Bob的分数是：{exam_scores['Bob']}")

#2.新增/修改
exam_scores["Dave"]=88
exam_scores["Alice"]=95

print("更新后的版本：",exam_scores)

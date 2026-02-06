print("---Function---")
#场景：开发一个交易所的VIP判断系统
#逻辑：持仓>1000u为VIP，否则为普通用户

#1.定义函数
#def是define的缩写
def check_vip(balance):
    if balance>=1000:
        return"VIP User"
    else:
        return"Normal User"

#2.调用函数
user1_bal=500
user2_bal=2000
user3_bal=1000

print(f"用户1({user1_bal}):{check_vip(user1_bal)}")
print(f"用户2({user2_bal}):{check_vip(user2_bal)}")
print(f"用户3({user3_bal}):{check_vip(user3_bal)}")
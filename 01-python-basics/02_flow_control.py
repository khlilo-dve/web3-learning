transfers=[50,2000,10,5000,300,1200]
whale_count=0
print("---开始审计---")
for x in transfers:
    if x>1000:
        print(f"whale alert:,{x}")
        whale_count=whale_count+1
print(f"总共发现{whale_count}笔巨鲸交易")
    
    
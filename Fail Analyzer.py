marks=[45,78,90,33,60]
pass_count=0
fail_count=0
for X in marks:
   if X> 50:
      pass_count+=1
   else:
      fail_count+=1
print("pass:",pass_count)
print("fail:", fail_count)          


logs=["INFO","ERROR","WARNING","ERROR"]
i=0
error_count=0
while i<len(logs):
   if logs[i]=="ERROR":
      error_count+=1
i+=1
print("Error count:",error_count)      
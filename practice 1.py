x = [2, 4, 5, 2, 6, 7, 3, 6, 1, 3, 8]
n=len(x)
sum=sum(x)
mean=sum/n
print("mean is:",str(mean))
x.sort()
if n%2==0:
    median1=x[n//2]
    median2=x[n//2-1] 
    median=(median1+median2)/2
else: 
    median=x[n//2] 
print("Median is:",str(median)) 
print("mode",(max(set(x),key=x.count)))



              
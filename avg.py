# X1=60
# X2=55
# X3=40
# X4=30
# X5=10

# sum= X1+X2+X3+X4+X5

# avg=sum/5

# if avg >=90:
#     print("ممتاز")
# elif avg >=80:
#     print("جيد جداً")
# elif avg >=70:
#     print("جيد")
# elif avg >=50:
#     print("مقبول")
# else:


balance= 10000
amont= int(input("ادخل قيمة المشتريات"))

if amont<= balance:
    balance -= amont
    print("تمت العملية بنجاح")
    print("رصيدك هو: ", balance)
    
else:
    print("رصيدك غير كافي")
    
    
print("hello")
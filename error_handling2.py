try:
    f=open("C:\\Daniel\\Supporting_files\\11_sample_2_2_1.html",encoding='utf-8')
    print(f.readlines())
except Exception as e:
    print("error")
    print(e)
    f=open("C:\Daniel\Supporting_files\11_sample_2_2_1.html",encoding='utf-8')
    print(f.readlines())
else:
    print("else")
finally:
    print("finally")
    
def profile(name,age,*language):
    print("성명:{}\t 나이:{}\t ".format(name,age),end=" ")
    for lang in language:
        print(lang,end=" ")
    print()
profile("거북이", 100 , "영어","프랑스어","독일어")
profile("황소",10,"한국어","일본어","중국어","힌두어","영어")
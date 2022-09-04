week=int(input("몇주차입니까 "))
with open(str(week)+"주차.txt","w",encoding="utf8") as report:
    report.write("부서 :",)
    report.write("\n이름 :",)
    report.write("\n업무요약 :")
with open("{0}주차.txt","r",encoding="utf8".format(week)) as report:
    print(report.read())
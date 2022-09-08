with open("study.txt","w",encoding="utf8") as study_file:
    study_file.write("code programing")
    study_file.write("code programing")
    study_file.write("code programing")
with open("study.txt","r",encoding="utf8") as sty:
     print(sty.readline())
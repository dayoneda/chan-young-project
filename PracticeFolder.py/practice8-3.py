#score_file=open("score.txt","w", encoding="utf8")
#print("수학 : 0", file=score_file)
#print("과학 : 0", file=score_file)
#score_file.close()

score_file=open("scroe_txt","w", encoding="utf8")
score_file.write("수학 : 0")
score_file.write("\n과학 : 100")
score_file.close()

score_file=open("scroe_txt","r", encoding="utf8")
#print(score_file.read())
#score_file.close()
#print(score_file.readline(),end="")
#print(score_file.readline())

#while True:
#    line=(score_file.readline())
#    if not line:
#        break
#    print(line)
#score_file.close()

lines=score_file.readlines()
for line in lines:
    print(line)
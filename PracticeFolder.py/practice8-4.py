from json import load
import pickle
#profile={"조찬영":"코딩","박준형":"섹시","최지훈":[1,2,3]}
#profile_file=open("profile.pickle","wb")
#pickle.dump(profile,profile_file) # profile에있는 정보를 file에 저장
#profile_file.close()


profile_read=open("profile.pickle","rb")
profile_load=pickle.load(profile_read) 
print(profile_load)
profile_read.close() 
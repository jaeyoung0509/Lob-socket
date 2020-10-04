from gensim.models import Word2Vec
ko = Word2Vec.load('./ko.bin')
'''
scan = input()
a = ko.wv.similarity(scan, '음식')
if a>0.3:
    c = ko.wv.most_similar(scan,'병')
    print(c)
'''
###b= ko.wv.most_similar(positive=['바나나','우유','음식'])

##print(ko.wv.most_similar(positive=['질병','음식','부정']))
##print(ko.wv.most_similar(positive=['질병'] , negative = ['음식']))


input_list = ['과자', '물'] 
output_list=[]
for i in input_list:
    if(ko.wv.similarity(i,'음식')>0.3):
        output_list.append(i)     
print(output_list)



'''
print(ko.wv.most_similar(positive=['당뇨','음식'] , negative = ['질환','부정']))
'''
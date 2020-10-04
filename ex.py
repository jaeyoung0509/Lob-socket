# -*- coding: utf-8 -*- 
from gensim.models import Word2Vec
ko = Word2Vec.load('./ko.bin')
input_list = ['김치','돌','귤','돈까스','동양미래대학교']
output_list=[]
for i in input_list:
    try:
        food_similar=ko.wv.similarity(i,'음식')
        if(food_similar>0.5):
             print(i)
             print("음식입니다") 
#            pnN_food = ko.wv.similarity(i, '긍정')
 #           if(pnN_food > 0.3):
  #              se = ko.wv.most_similar(positive=[ i, '비타민','영양소'], negative = ['음식'])
   #             print(i)
    #            print(se)
     #       else:
     #           ts = ko.wv.most_similar(positive=[ i, '질병','합병증','부정'], negative = ['음식','질환','천재지변','부패'])
      #          print(i)
       #         print(ts)                
           ### output_list.append(i)
           ### output_list.append(food_similar)

    except Exception as err:
         print('nop')       

###asd = collections.Counter(output_list)
###max_value =max(list(asd.values))



'''
print(ko.wv.most_similar(positive=['당뇨','음식'] , negative = ['질환','부정']))
'''

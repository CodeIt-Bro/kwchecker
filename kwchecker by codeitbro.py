## KWchecker by CodeItBro
## Support by visiting: https://www.codeitbro.com/free-seo-rank-tracking-software
print("------------KWchecker by CodeItBro---------")
from googlesearch import search
import re

keywordsList = ["soundboard software", "Manga Creator"] ## Define all your keywords here

def Results(query):
    Results= search(query, num_results=30)
    for i in range(len(Results)):
        # print(Results[i])
        x = re.search("codeitbro.com", Results[i])      ## Change your domain here
        if x:
            y = Results.index(Results[i])
            print("There is a match at", y+1)
        else:
            continue


for i in range(len(keywordsList)):
    query = keywordsList[i]
    print("\n-----Search Results of----->", query)
    Results(query)
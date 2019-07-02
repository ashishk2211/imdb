"""this program is design to scraping a website(www.ibmd.com)"""
""" NOTE : Enter movie name as given in the website """

from bs4 import BeautifulSoup
from urllib import request
url="https://www.imdb.com/chart/top"
link=request.urlopen(url)
imdb=BeautifulSoup(link)
link.close()
##print(imdb)
while(True):
    print("Menu \n")
    print("press 1 for top 250 movies names\n")
    print("press 2 for search any movie by name and get rating and year\n")
    print("press 3 for getting rating of all top 250 movies with year of release\n")
    print("press 4 for search movie by year\n ")
    print("print 5 for search movie by name get details of actors and director information\n")
    print("print 6 for summary of specific movie in top 250 movie\n")
   
    ch=input("Enter your choose :")
    if(ch=='1'):
        count=1
        for i in imdb.find_all("td",{"class":"titleColumn"}):
            
            print(count,end=" ")
            print(i.find_next("a").string)
            count=count+1
    if(ch=='2'):
        n=input("Enter movie name :")
        for i in imdb.find_all("td",{"class":["titleColumn"]}):
            a=i.find_next("a")
            if(n==a.string):
                print(a.string,a.find_next("strong").string,a.find_next("span").string)
    if(ch=='3'):
        count=1
        for i in imdb.find_all("td",{"class":["titleColumn"]}):
            a=i.find_next("a")
            print(count,end=" ")
            print(a.string,a.find_next("strong").string,a.find_next("span").string)
            count=count+1
    
    if(ch=='4'):
        n=input("Enter movie year :")
        for i in imdb.find_all("td",{"class":["titleColumn"]}):
            year="("+n+")"
            a=i.find_next("span")
            if(year==a.string):
                print(i.find_next("a").string,a.find_next("strong").string)
    if(ch=='5'):
        n=input("Enter movie name :")
        for lnk in imdb.find_all("td",{"class":"titleColumn"}):
             if(lnk.find_next("a").string ==n):
                  y="https://www.imdb.com"+lnk.find_next("a")["href"]
                  url2=request.urlopen(y)
                  imdb2=BeautifulSoup(url2)
                  url2.close()
                  for i in imdb2.find_all("span",{"itemprop":["director"]}):
                       a=i.find_next("a")
                       print("director name :",a.find_next("span").string)
                  print("\t\t\t\t\t\t\t\t Actors list:")
                  for i in imdb2.find_all("td",{"itemprop":["actor"]}):
                       a=i.find_next("a")
                       print(a.find_next("span").string,end="\n")
                  for i in imdb2.find_all("span",{"itemprop":["director"]}):
                       a=i.find_next("a")["href"]
                       b=i.find_next("a")
                       print("Director name :",b.find_next("span").string)
                       z="https://www.imdb.com"+a
                       url3=request.urlopen(z)
                       imdb3=BeautifulSoup(url3)
                       url3.close()
                       for i in imdb3.find_all("span",{"class":["see-more inline nobr-only"]}):
                            a=i.find_next("a")["href"]
                            b=i.find_next("a")
                            r="https://www.imdb.com"+a
                            url4=request.urlopen(r)
                            imdb4=BeautifulSoup(url4)
                            url4.close()
                            for i in imdb4.find_all("div",{"class":["soda odd"]}):
                                 print(i.get_text())
    if(ch=='6'):
        n=input("Enter movie name :")
        for lnk in imdb.find_all("td",{"class":"titleColumn"}):
             if(lnk.find_next("a").string ==n):
                  y="https://www.imdb.com"+lnk.find_next("a")["href"]
                  url2=request.urlopen(y)
                  imdb2=BeautifulSoup(url2)
                  url2.close()
                  for i in imdb2.find_all("span",{"itemprop":["director"]}):
                      a=i.find_next("a")
                      print("director name :",a.find_next("span").string)
                      for i in imdb2.find_all("span",{"itemprop":["description"]}):
                          print("\t\t\t\tMOVIE NAME:",n)
                          print(i.string,end="\n")
    choice=input("want to stop press space")
    if choice==' ':
        break
        
        
        
        
    

    


        
        
    
        
        

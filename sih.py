# -*- coding: utf-8 -*-
"""
@author: shyaam.ganesh

"""

from twitter_scraper import get_tweets, Profile


master_list = []

for tweet in get_tweets('checkout', pages=1):
    
    link = tweet['entries']['urls']
    
    if len(link) != 0:
        
        
        profile_details_list = []
        
        profile_details_list.append(tweet['username'])
        
        username = tweet['username']
        
        profile_link = 'twitter.com/' + username
        
        profile_details_list.append(profile_link)
        
        tweet_link = tweet['tweetUrl']
        
        profile_details_list.append(tweet_link)
        
        profile = Profile(username)
            
        profile_details_list.append(profile.location)
           
        profile_details_list.append(profile.name)  
        
        profile_details_list.append(link[0])

        master_list.append(profile_details_list)
        

print('---The entire list of profiles is ----')

print(master_list)


for each_value in master_list:
    
    entry = each_value[-1]
    
    print(entry)
        
    
    
    
    




#!/usr/bin/python

import urllib.request 
import json


#Get a  results of congressman's or congresswoman's rollcall 
#votes during a  specific congress
#@param congressman's id from govtrack.us
#@param amount of votes to show
#@return a dictionary of the votes id -> (Question, vote)
def searcher(gtId,amount):
   
   #Make url
   urlId = str(gtId)
   limit = str(amount)
   url = "http://www.govtrack.us/api/v2/vote_voter/?person=" +urlId +"&limit=" +limit

   request = urllib.request.Request(url)
   response = urllib.request.urlopen(request)
   data = json.loads(response.read().decode('ascii','ignore'))


   voteHistory = {}
   #i = 0 
   for key in data['objects']:
      #print (key['vote']['id'])
      #i = i + 1
      voteHistory[key['vote']['id']] = (key['vote']['question'], key['option']['value'])

   #xprint (i)
   print (voteHistory)
   return voteHistory

      
      






def main():
   
   gtid= 300088 #Senator Sessions
   amount = 1000 #Check last %amount bills
   
   searcher(gtid,10000)



if __name__ == '__main__':
    main()
    

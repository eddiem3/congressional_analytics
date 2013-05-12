#!/usr/bin/python

import urllib.request 
import json


#Get a  results of congressman's or congresswoman's rollcall 
#votes during a  specific congress
#@param Bioguide ID of a senator
#@param Number of congress ie. 111th, 112th
def searcher(bioguideId, congressNumber, apiKey):
   
   #Make url
   apiUrl = "http://congress.api.sunlightfoundation.com/"
   function = "votes?congress=" +congressNumber
   url = apiUrl +function 

   #Get roll call vote ids and place them in a dictionary
   #TODO: DELETE THE LIST AND PUT ITEMS STRAIGT INTO DICTIONARY
   #QUERYS WILL BE BASED ON DICTIONARY KEYS THEN
   rollCallRequest = urllib.request.Request(url,None,{'X-APIKEY':apiKey})
   rollCallResponse = urllib.request.urlopen(rollCallRequest)
   rollCallData = json.loads(rollCallResponse.read().decode('utf-8'))
   rollCallIds = []

   for key in rollCallData['results']:
      rollCallIds.append(key['roll_id'])

   print(rollCallIds)
   
   voteHistory = dict.fromkeys(rollCallIds) #Keys bill name values (description, vote)
   

#x   url = "http://congress.api.sunlightfoundation.com/votes?fields=roll_id=h1-2009,voters.Y000062"
   url = "http://congress.api.sunlightfoundation.com/votes?fields=voter_ids,roll_id=h1-2009"
   print (url)
   voteRequest = urllib.request.Request(url,None,{'X-APIKEY':apiKey})
   voteResponse = urllib.request.urlopen(voteRequest)
   voteData = json.loads(voteResponse.read().decode('utf-8'))

   for key in voteData['results']:
      print (key['voter_ids'])

#   print(voteData['results'][1]['voter_ids'])
#   print (voteData['results'][0][bioguideId])
#   print (voteData['results'][0]['voter_ids'][bioguideId])


      
      




#Find the votes of the senators bill  

def main():
    congressNumber = "111"
    bioguideID = "S001141"
    #bioguideID = "Y000062"
    apiKey = "cb15f61c310e498ca7ec2d32d91d20b8"
    searcher(bioguideID,congressNumber,apiKey)



if __name__ == '__main__':
    main()
    
    

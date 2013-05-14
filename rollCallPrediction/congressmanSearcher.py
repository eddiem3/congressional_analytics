#!/usr/bin/python

import urllib.request 
import json
import re
import string
import xml.etree.ElementTree as ET



#Get a  results of congressman's or congresswoman's rollcall votes on bills
#votes during a  specific congress
#@param congressman's id from govtrack.us
#@param amount of votes to show
#@param boolean to add bill text
#@return a dictionary of the votes in the form of Vote ID -> (Vote Question, Type, Congessman's Vote)
def rollCallSearch(gtId,amount,bill):
   
   #Make url
   urlId = str(gtId)
   limit = str(amount)
   url = "http://www.govtrack.us/api/v2/vote_voter/?person=" +urlId +"&limit=" +limit

   request = urllib.request.Request(url)
   response = urllib.request.urlopen(request)
   data = json.loads(response.read().decode('ascii','ignore'))

   voteHistory = {}
   i = 0 
   for key in data['objects']:
      print(key['vote']['id'])
      i = i + 1
      
      if bill:
         voteHistory[key['vote']['id']] = (key['vote']['question'],key['vote']['category']
                                           ,key['vote']['related_bill'],key['option']['value']
                                           ,key[getBillText(key['vote']['related_bill'])])
      else:
         voteHistory[key['vote']['id']] = (key['vote']['question'],key['vote']['category'],
                                           key['vote']['related_bill'],key['option']['value'])
         
   
   print (voteHistory)
   return voteHistory

#Get the bill text for a vote
#@param govtrack.us id for a bill
def getBillText(billId):

   billId = str(billId)
   billText = None

   #Get bill data
   url = "http://www.govtrack.us/api/v2/bill/" + str(billId)
   request = urllib.request.Request(url)
   response = urllib.request.urlopen(request)
   data = json.loads(response.read().decode('ascii','ignore'))
   
   #Get the display number 
   #Get the congress
   congress = str(data['congress'])  #Congress number

   billNumber = str(data['display_number']) #bill number in govtrack.us form with extra symbols
   billNumber = re.sub('[%s]' % re.escape(string.punctuation), '', billNumber) # removes punctuation
   billNumber = billNumber.lower() # make everything lowercase
   billNumber = ''.join(billNumber.split()) #remove space
   print(billNumber)
   
   #Compile the url of the bill 
   url = "http://www.govtrack.us/data/us/"
   url = ''.join([url,congress,"/", "bills","/",billNumber,".xml"]) 
   print(url)

   try:
      urllib2.urlopen(request_object)
      #uses except statement to detect a URLError  problem that was created by urllib2 by the failed request, then stores more info in an exception_variable
   except URLError:
      print ("Had an error")
      return None

   else:
      request = urllib.request.Request(url)
      response = urllib.request.urlopen(request)
   
      #Parse the xml file for the summary tag
      tree = ET.parse(response)
      root = tree.getroot()
      summary = root.find('summary')
      print (summary.text)
      return summary.text
      
                                    
#Get all the roll call votes of a Congressxman on a particular type of vote ie. passage
#@param dictionary of vote history id -> (question, type, congressman's vote)
#@param string corresponding to one of the vote types in the Govtrack.us api
#@return dictionary excluding those of a particular vote type
def parseRollCalls(voteHistory, voteType):

   parsedHistory = voteHistory.copy()

   for key, value in voteHistory.items():
      if value[1] != voteType:
         del parsedHistory[key]
         
   return parsedHistory



def main():
   
   gtid= 300088 #Senator Sessions
   amount = 10000 #Check last %amount bills
   addbills = True
   #exclude = ["passage"]
   voteHistory = rollCallSearch(gtid,amount,addbills)
   #passageHistory = parseRollCalls(voteHistory, "passage")
   #billId = 75747
   #getBillText(billId)

 

   


if __name__ == '__main__':
    main()
    

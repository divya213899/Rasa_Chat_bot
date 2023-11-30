# Importing required modules 
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker 
from rasa_sdk.executor import CollectingDispatcher 
import smtplib 

SENDER_EMAIL_ID="divyagupta21@iitk.ac.in"
PASSWORD="Aashi@123"

# Creating new class to send emails. 
class ActionEmail(Action): 

	def name(self) -> Text: 
		
		# Name of the action 
		return "action_email"

	def run(self, dispatcher: CollectingDispatcher, 
			tracker: Tracker, 
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 

		# Getting the data stored in the 
		# slots and storing them in variables. 
		print("In the 'run' function")
		user_name = tracker.get_slot("name") 
		email_id = tracker.get_slot("email") 
		
		# Code to send email 
		# Creating connection using smtplib module 
		s = smtplib.SMTP('smtp.cc.iitk.ac.in',465) 
		
		# Making connection secured 
		s.starttls() 
		
		# Authentication 
		s.login(SENDER_EMAIL_ID, PASSWORD) 
		
		# Message to be sent 
		message = "Hello {} , This is a demo message".format(user_name) 
		
		# Sending the mail 
		s.sendmail(SENDER_EMAIL_ID,email_id, message) 
		
		# Closing the connection 
		s.quit() 
		
		# Confirmation message 
		dispatcher.utter_message(text="Email has been sent.") 
		
		print("Exiting the 'run' function")
		return []


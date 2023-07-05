import requests
import pandas as pd
import sqlite3
from csv_contacts.views import write_log
import sys


def schedule_api():
	"""This is nothing but the job that scheduled for every 10 sec to download data from URL provided"""
	url = "https://docs.google.com/spreadsheets/d/1A77-RWx7x8PK2uDm_1XlXyCy2ID9-9lhwix8wPDd5X0/pub?gid=0&single=true&output=csv"
	file_name = "data.csv"
	try:
		# Send GET request to download the file
		response = requests.get(url)
	except Exception as err:
		write_log('error', err)
		sys.exit(1)

	# Check if the request was successful
	if response.status_code == 200:
		try:
			# Save the content as a CSV file
			with open(file_name, "wb") as file:
				file.write(response.content)
			print("File downloaded and saved as", file_name)
			write_log('info', "File downloaded and saved from CSV source")
		except Exception as err:
			write_log('error', err)
			sys.exit(1)
	else:
		print("Failed to download the file")
		write_log('info', "File download failed from CSV source")
		sys.exit(1)
	try:
		df = pd.read_csv("data.csv")
		conn = sqlite3.connect('db.sqlite3')  # Create or connect to a SQLite database
		table_name = "csv_contacts_contacts"  # Name of the table to be created
		cursor = conn.cursor()
		cursor.execute("DROP TABLE IF EXISTS csv_contacts_contacts")
		df.reset_index(inplace=True)
		df.rename(columns={'index': 'id'}, inplace=True)
		df.to_sql(table_name, conn, if_exists='replace', index=False)
		print("Data stored in database successfully.")
	except Exception as err:
		write_log('error', err)
		sys.exit(1)




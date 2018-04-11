# CSV Data Entry CLI

import sys
import pandas as pd
import click
from colorama import Fore, Style

# NOTES: 1. Keep file closed while working with it.
# 		 2. Press `q` when you're done to exit


def new_entry(index):

	print(Fore.GREEN + Style.BRIGHT + "LINE:" + str(index) + Style.RESET_ALL)
	print(Fore.YELLOW + Style.BRIGHT + headlines["Headline"][index] + Style.RESET_ALL)

	user_input = input().lower()

	# BACK
	if user_input == 'b':
		return (user_input, True);

	# QUIT
	elif user_input == 'q':
		print("EXIT")
		headlines.to_csv(path, sep=",")
		sys.exit()

	else:
		return (user_input, False)


def main():

	path = "../../data/scored_filtered_coindesk_headlines.csv"

	headlines = pd.read_csv(path, sep=",")

	# print(headlines)

	for idx in range(len(headlines["Sentiment"])):
		# print("CURR", headlines["Sentiment"][idx])

		valid = ["-2", "-1", "0", "1", "2", "x"]

		if str(headlines["Sentiment"][idx]) not in valid:
			output = new_entry(idx)
			repeat = output[1]
			user_input = output[0]

			# print(output)
			if repeat:
				user_input = new_entry(idx - 1)[0]
				if user_input in valid:
					headlines["Sentiment"][idx-1] = user_input

				user_input = new_entry(idx)[0]

			if user_input in valid:
				headlines["Sentiment"][idx] = user_input


	headlines.to_csv(path, sep=",")


def cli():
	sys.exit()


if __name__ == '__main__':
	cli()


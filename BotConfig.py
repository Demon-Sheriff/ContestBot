from selenium import webdriver
import scrapy
import random
import webbrowser

bot_name = "ContestBot"

def get_response(UserMessage):
	
	UserMessage = UserMessage.strip().lower()
	
	url_cf = "https://codeforces.com/contests"
	url_cc = "https://www.codechef.com/contests"
	# if user tries to greet the bot using hi or hello
	sample_responses = [
		"Hello! How can I assist you?",
		"Nice to meet you!",
		"How can I help you today?",
		"I'm here to answer your questions.",
		"Ask me anything!",
		"What would you like to talk about?",
	]
	contest_details_query = ["give me all the contest details","print the contest details","are there any upcoming contests","upcoming contests", "all upcoming contests", "all contest details", "all upcoming cp contests", "all -c d","give me all the upcoming contest details", "information about the upcoming contests", "upcoming contests data"]
	if UserMessage == "hi" or UserMessage == "hello" or UserMessage == "hey":
		return random.choice(sample_responses)
	# ask for redirection to codeforces using command redirect or rd and -c for current and upcoming contests
	# also by default if the user does rd -c it will redirect to cf if not website is specified.
	elif UserMessage == "redirect -c cf" or UserMessage == "rd -c cf" or UserMessage == "cf current contests" or UserMessage == "cf -c -ct":
		webbrowser.open(url_cf)
		return "redirected to current and upcoming codeforces contest page"
	# do the same for codechef as well
	# -c is for current, -u for upcoming, -ct for contests,
	elif UserMessage == "redirect -c cc" or UserMessage == "rd -c cc" or UserMessage == "cc current contests" or UserMessage == "codechef current contests":
		webbrowser.open(url_cc)
		return "redirected to current and upcoming codechef contest page"
	# query about the upcoming contest details
	elif contest_details_query.__contains__(UserMessage):
		return "In progress"
	# query about codeforces contest details
	else:
		return "I am not trained to answer this, sorry."
	
	
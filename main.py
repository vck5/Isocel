import discord, aiosonic, random, pyjokes, randfacts, json, asyncio
from discord.ext import commands 
from googletrans import Translator
from aiosonic import HTTPClient
bot = commands.Bot(command_prefix=';', intents=discord.Intents.all())
bot.remove_command('help')
c = HTTPClient()
@bot.event
async def on_ready():
	print(f"[ 1 ]: Logged in as: {bot.user}")
	print(f"[ 2 ]: ID: {bot.user.id}")
	await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="https://github.com/vck5"))

@bot.command(aliases=['lesbiangay','lesbianrate'])
async def lesbian(ctx, m: discord.Member = None):
	m = m or ctx.author
	
	l = random.randint(1,500)
	
	embed = discord.Embed(description=f"{ctx.author}: {m.mention} is {l}% Lesbian! 👩‍❤️‍💋‍👩")
	await ctx.send(embed=embed)

@bot.command(aliases=['howautistic','autismrate'])
async def autistic(ctx, m: discord.Member = None):
	m = m or ctx.author
	
	a= random.randint(1,500)
	
	embed = discord.Embed(description=f"{ctx.author}: {m.mention} is {a}% Autistic! 🦨")
	await ctx.send(embed=embed)

@bot.command()
async def say(ctx, *, args: str = None):
	try:
		await ctx.send(f"``` {args} ```")
	except Exception as e:
		await ctx.send(f"``` {{ + Error + }} : {e}")
		
@bot.command(aliases=['howgay','gayrate'])
async def gay (ctx, m: discord.Member = None):
	m = m or ctx.author
	
	g = random.randint(1,500)
	
	embed = discord.Embed(description=f"{ctx.author}: {m.mention} is {g}% Gay! 🌈")
	await ctx.send(embed=embed)

@bot.command()
async def joke (ctx):
	try:
		joke = pyjokes.get_joke()
		embed = discord.Embed(description=joke, color=discord.Color.random())
		embed.set_footer(text=ctx.author.name, icon_url=ctx.author.display_avatar.url)
		await ctx.send(embed=embed)
	except Exception as e:
		await ctx.message.add_reaction("👎")
		await ctx.send(f"``` {{ + Error + }} : {e} ```")

@bot.command()
async def cringe (ctx, m: discord.Member = None):
  if m is None:
    embed=discord.Embed(description=f"{ctx.author.mention}: *Considers everyone in the chat* **cringe**!", color=0xA4C4FF)
    embed.set_image(url="https://i.waifu.pics/gkB-aJ2.jpg")
    await ctx.send(embed=embed)
  else:
    e = discord.Embed(description=f"{ctx.author.mention}: *Considers {m.mention}* **cringe**!", color=0xA4C4FF)
    e.set_image(url="https://i.waifu.pics/gkB-aJ2.jpg")
    await ctx.send(embed=e)
    
@bot.command(aliases=["8ball"])
async def eightball(ctx, ques: str):
  res = ["Yes.","No.","Definitely yes!","Never.","sure.","Outlook good.","Outlook bad.","I think no.","I think yes."]
  r = random.choice(res)
  await ctx.send(embed=discord.Embed(title="The Magical Eightball Says: ", description=f"{ctx.author.mention}: {r}", color=discord.Color.random()))

@bot.command(aliases=["av"])
async def avatar (ctx, m: discord.Member = None):
	m = m or ctx.author
	
	embed = discord.Embed(description=f"{m.mention}'s **Avatar**", color=discord.Color.random())
	embed.set_image(url=m.display_avatar.url)
	await ctx.send(embed=embed)

@bot.command(aliases=["randfact","randomfacts","fact"])
async def facts (ctx):
	try:
		f = randfacts.get_fact(True)
		embed = discord.Embed(title="Did you know?", color=discord.Color.random())
		embed.add_field(name="Fact",value=f, inline=False)
		embed.set_footer(text=ctx.author.name, icon_url=ctx.author.display_avatar.url)
		await ctx.send(embed=embed)
	except Exception as e:
		await ctx.send(embed=discord.Embed(description=f"``` {{ + Error + }} : {e} ```", color=0x000001), delete_after=25)

@bot.command ()
async def translate (ctx, lang, *,arg):
	try:
		async with ctx.typing():
			t = Translator()
			r = await t.translate(arg, dest=lang)
			
		await ctx.reply(embed=discord.Embed(title="``` {  +   Translation  +   }  ```",description=r.text, color=0xA4C4FF))
	except Exception as e:
			await ctx.send(embed=discord.Embed(description=f"``` Error: {{ + {e}  +  }} ```"), delete_after=5)

@bot.command()
async def dog(ctx):
	try:
		async with ctx.typing():
			r = await c.get("https://dog.ceo/api/breeds/image/random")
			d = await r.json()
			dog = d["message"]
		
			embed = discord.Embed(description="Dog", color=discord.Color.random())
			embed.set_image(url=dog)
			embed.set_footer(text=ctx.author.name, icon_url=ctx.author.display_avatar.url)
			await ctx.send(embed=embed)
	except Exception as e:
		await ctx.send(embed=discord.Embed(description=f"{{ + Error + }} : {e}", color=0x000001), delete_after=25)
	
@bot.command()
async def coinflip(ctx):
	r = random.choice(["Head","Tails"])
	embed = discord.Embed(description=f" 🦨: The coin landed on: {r}!", color=discord.Color.random())
	embed.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar.url)
	embed.set_thumbnail(url=ctx.guild.icon.url if ctx.guild.icon else None)
	await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
	try:
		l = round(bot.latency * 1000)
		embed = discord.Embed(title="Latency: ", description=f"{ctx.author.mention}: {l}ms.", color=discord.Color.random())
		embed.set_thumbnail(url=ctx.guild.icon.url if ctx.guild.icon else None)
		embed.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar.url)
		await ctx.send(embed=embed)
	except Exception as e:
		await ctx.send(embed=discord.Embed(description=f"{{ + Error + }} : {e}.", color=discord.Color.random()))

@bot.command (aliases=["fakehack","fhack"])
async def hack (ctx, member: discord.Member = None):
	if member is None:
		member = ctx.author
		
	async with ctx.typing():
		city = ["Delhi","Patna","New York","Istanbul","Gaya","Islamabad","Lahore","Rome","Moscow","Jakarta","Jaipur","Pune","Mumbai","Purnea","Kabul"]
		vpn = ["True","False"]
		proxy = ["True","False"]
		
		embed = discord.Embed(title="```{{ + HACKED : }} : ⚡```", color=discord.Color.random())
		embed.add_field(name="Name: ", value=member.name, inline=False)
		embed.add_field(name="IP: ", value='.'.join(str(random.randint(1,254)) for _ in range(4)), inline=False)
		embed.add_field(name="City: ", value=random.choice(city), inline=False)
		embed.add_field(name="VPN: ", value=random.choice(vpn), inline=False)
		embed.add_field(name="Proxy: ", value=random.choice(proxy), inline=False)
		embed.add_field(name="Email: ", value=f"{member.name}@gmail.com", inline=False)
		embed.add_field(name="Password: ", value=f"{member.id}67", inline=False)
		embed.set_author(name=ctx.author.name,icon_url=ctx.author.display_avatar.url)
		await ctx.send(embed=embed)

@bot.command()
async def reverse(ctx, *, text):
    try:
    	await ctx.send(f"```{text[::-1]}```")
    except Exception as e:
    	await ctx.send(f"``` {{ + Error + }} : {e}.```")

@bot.command()
async def cat(ctx):
	try:
		async with ctx.typing():
			r = await c.get("https://api.thecatapi.com/v1/images/search")
			d = await r.json()
			cat = d[0]["url"]
		
			embed = discord.Embed(description="Cat", color=discord.Color.random())
			embed.set_image(url=cat)
			embed.set_footer(text=ctx.author.name, icon_url=ctx.author.display_avatar.url)
			await ctx.send(embed=embed)
	except Exception as e:
		await ctx.send(embed=discord.Embed(description=f"{{ + Error + }} : {e}", color=0x000001), delete_after=25)

@bot.command()
async def fox(ctx):
	try:
		async with ctx.typing():
			r = await c.get("https://some-random-api.com/animal/fox")
			a = await r.json()
			fox = a["image"]
				
			embed = discord.Embed(description="Fox", color=discord.Color.random())
			embed.set_image(url=fox)
			embed.set_footer(text=ctx.author.name, icon_url=ctx.author.display_avatar.url)
			await ctx.send(embed=embed)
	except Exception as e:
		await ctx.send(embed=discord.Embed(description=f"{{ + Error + }} : {e}", color=0x000001), delete_after=25)

@bot.command()
async def password(ctx):
	try:
		async with ctx.typing():
			r = await c.get("https://passwordwolf.com/api/?length=16&special=1")
			a = await r.json()
			p = a[0]['password']
			embed = discord.Embed(title="```{{ + Password + }} : ⚖️```",description=p, color=discord.Color.random())
			try:
				await ctx.author.send(embed=embed)
				await ctx.message.add_reaction("👍")
			except:
				await ctx.message.add_reaction("👎")
	except Exception as e:
		await ctx.send(embed=discord.Embed(description=f"```{{ + Error + }} : {e}```", color=discord.Color.random()))

@bot.command()
async def advice(ctx):
	try:
		async with ctx.typing():
			r = await c.get("https://api.adviceslip.com/advice")
			a = await r.json()
			advice = a['slip']['advice']
			
			embed = discord.Embed(title="{{ + Advice + }}", description=a, color=discord.Color.random())
			await ctx.send(embed=embed)
	except Exception as e:
		await ctx.send(f"``` {{ + Error }} : {e}```")

@bot.command()
async def guess(ctx):
	s = random.randint(1,100)
	attempt = 0
	
	await ctx.send("``` {{ + 'm thinking of a number between 1 and 100. Can you guess it? + }} ```")
	
	def check(m):
		return m.channel == ctx.channel and m.author == ctx.author and m.content.isdigit()
	try:
		while True:
			g = await bot.wait_for("message", timeout=60.0, check=check)
			guess = int(g.content)
			attempt += 1
			if guess < s:
				await ctx.reply("``` ⚡: Too low! Try again.```")
			elif guess > s:
				await ctx.reply("``` 🥈: Too high! Try again.```")
			else:
				await ctx.send(f"``` 🥇:  You got it! The number was **{s}**. It took you {attempt} attempt(s).```")
				break
				
	except asyncio.TimeoutError:
		await ctx.send(f"``` {{ + Timeout! + }} : Time's up! The number was **{s}**.")
	except Exception as e:
		await ctx.send(f"``` {{ + Error + }} : {e}```")

@bot.command()
async def servericon(ctx):
	try:
		if ctx.guild.icon:
			embed = discord.Embed(description=f"{{ + {ctx.guild.name} + }}")
			embed.set_image(url=ctx.guild.icon.url)
			await ctx.send(embed=embed)
		else:
			await ctx.send("``` This server doesn't have an icon. ```")
	except Exception as e:
		await ctx.send(f"``` {{ + Error + }} : {e}```")

@bot.command()
async def help(ctx):
	try:
		cmd = [c.name for c in bot.commands]
		h = '\n'.join(cmd)
	
		await ctx.send(f"``` {{ ^ Isocel Bot Help Panel ^ }} : \n{h} ```")
	except Exception as e:
		await ctx.send(f"```{{ + Error + }} : {e}```")
		
bot.run(token)

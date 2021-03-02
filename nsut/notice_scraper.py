import bs4
import requests
from rich.console import Console


IMS_URL = 'https://www.imsnsit.org/imsnsit/notifications.php'
console = Console()


def print_notices(max_notices):
	print("Loading...")

	res = requests.get(IMS_URL)

	soup = bs4.BeautifulSoup(res.text, 'html.parser')

	# each notice is within a td inside a tr
	notice_rows = soup.find_all("td", class_="list-data-focus")

	console.rule("[bold red] These are the " + str(max_notices) + " latest notices", style="red")

	for i in range(0, max_notices):
		console.print(i+1,  notice_rows[i].contents[0].contents[0].string, style="red")
		console.rule(style="red")

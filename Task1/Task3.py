import requests
import bs4

try:
	wa = "https://buynothingproject.org/find-a-group"
	res = requests.get(wa)
	#print(res)
	
	data = bs4.BeautifulSoup(res.text,"html.parser")
	print(data)
	
	info = data.find_all("tr",["even_row","odd_row"])
	print(info)

	for i in info:
		newinfo = i.find_all("td")
		print("place = ",newinfo[0].text,"price = ",newinfo[1].text)

except Exception as e:
	print("issue ",e)
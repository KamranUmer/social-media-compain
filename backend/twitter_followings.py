import requests



url = "https://twitter241.p.rapidapi.com/followings"

querystring = {"user":"2455740283","count":"20"}

headers = {
	"X-RapidAPI-Key": "from env",
	"X-RapidAPI-Host": "twitter241.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
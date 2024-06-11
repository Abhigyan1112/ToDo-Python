import tkinter as UI
import requests

category = 'inspirational'
quote=''
api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
response = requests.get(api_url, headers={'X-Api-Key': 'knOUuLi9nJWgllPOJsNirw==kJ1cUK6UEwWqkguF'})
if response.status_code == 200:
    quote=response.json()
    quote=quote[0]['quote']
else:
    print("Error:", response.status_code, response.text)
    
print(quote)
window=UI.Tk()
window.title("Your daily To-do. Have a great day")
window.geometry("600x600")
window.mainloop()


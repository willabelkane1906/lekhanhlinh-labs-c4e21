from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)

raw_data= conn.read()
html_page = raw_data.decode("utf-8")
soup = BeautifulSoup(html_page, "html.parser")

section  = soup.find("section")
print(section.prettify())
div_list = section.find_all("div")
for div in div_list:
    ul = div.ul
    li_list =  ul.find_all("li")
    news_list = []
    for li in li_list:
        c = li.h3.a
        name = c.string
        b = li.h4.a
        artist = b.string
        news = {
            "Names" : name,
            "Artists" : artist,
        }
        news_list.append(news)
        import pyexcel
        pyexcel.save_as(records= news_list, dest_file_name="song1.xlsx")
        
song_list = []
for song in song_list:
    name = song["Names"]
    artist = song["Artists"]
    song = name + " " + artist
    song_list.append(song)
    
from youtube_dl import YoutubeDL
options = {
    'default_search': 'ytsearch', 
    'max_downloads': 1 
}
dl = YoutubeDL(options)
dl.download(song_list)














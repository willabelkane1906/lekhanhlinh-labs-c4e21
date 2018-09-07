from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/4/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)

raw_data= conn.read()
html_page = raw_data.decode("utf-8")
soup = BeautifulSoup(html_page, "html.parser")
f_conn = open('vnm.html', 'wb')
f_conn.write (raw_data)
f_conn.close()

div = soup.find("div", "divTableHeader")
print(div.prettify())
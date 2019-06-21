# 1. 網路連線程式，以 HTTP 通訊協定為例
# 1.1 使用 urllib.request 模組
# 1.2 使用 urlopen(網址) 連線網址
# 1.3 使用 read() 讀取資料
# 1.4 使用 decode("utf-8")  處理中文資料
# 1.5 使用 json 模組，解讀 json 資料格式

# 2. 公開資料串接
# 2.1 使用台北市政府公開資料 (http://data.taipei/)
# 2.2 搜尋並取得資料的串接網址 (API)
# 2.3 測試串接網址，觀察資料格式
# 2.4 撰寫程式，自動連線並且擷取想要的資料

# 3. 儲存資料到檔案中
# 3.1 使用寫入模式開啟檔案
# 3.2 使用 utf-8 編碼處理中文資料
# 網路連線
# import urllib.request as request
# src="https://www.ntu.edu.tw/"
# with request.urlopen(src) as response:
#     data=response.read().decode("utf-8") # 取得台灣大學網站的原始碼(HTML、CSS、JS)
# print(data)

# 串接、擷取公開資料
import urllib.request as request
import json
src="https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=296acfa2-5d93-4706-ad58-e83cc951863c"
with request.urlopen(src) as response:
    data=json.load(response) # 利用json模組處理json資料格式
# print(data)

# 將公司名稱列表出來
clist=data["result"]["results"]
with open("data2.txt","w",encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n")
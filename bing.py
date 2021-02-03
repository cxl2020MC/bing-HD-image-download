import requests,time,os,base64
from fake_useragent import UserAgent
ua = UserAgent()
days=input("请输入你要下载的图片数量：")
stat=time.time()

day=0
def main():
    global day
    if day == 0:
        url = "https://bing.mcloc.cn/api/?type=json"
    else:
        url = "https://bing.mcloc.cn/api/?type=json&day="+str(day)
    #url = "https://bing.ioliu.cn/bing/json/"
    r = requests.get(url)
    image_get=r.json()
    name=image_get["bing_title"]
    #name=image_get["copyright"]
    name1=name.replace('(', '☺').replace(')', '☺')#.replace('，', '☹')
    print(image_get)
    image_url=image_get["bing_imgurluhd"]
    #image_url=image_get["url"]
    print("HD超高清图片url:"+image_url)

    if os.path.exists('必应壁纸'):
        pass
    else:
        os.mkdir('必应壁纸')
        print('目录创建成功')
        
    if os.path.exists(r'C:\bg'):
        pass
    else:
        os.mkdir(r'C:\bg')
        print('目录创建成功')
        

    user=ua.chrome
    print("当前UA："+user)
    headers = {
               "User-Agent":user
              }

    r = requests.get(image_url, headers=headers)
    temp = base64.b64decode(r.content)
    print(name1.split("☺")[0])
    path=".\\必应壁纸\\"+(name1.split("☺")[0])+".jpg"
    with open(path, mode="wb") as f:
            f.write(r.content)
    print("第"+str(day)+"天下载成功")

    #if day != "ytyug":
    if day == 0:
        with open(r"C:\bg\1.jpg", mode="wb") as f:
            f.write(r.content)
        os.system('chcp 65001')
        os.system("换壁纸.bat")
    day=day+1
    
while int(day) != int(days):
    main()
exit()
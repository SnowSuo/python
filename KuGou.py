import requests,re,sys,os

print('酷狗音乐播放下载器(输入歌曲名或者歌曲作者)')
dataDir=os.path.join(os.getcwd(),'Music')
if not os.path.exists(dataDir):
    os.mkdir(dataDir)
while True:
    print('-'*40)
    keyword = input("请输入想要听的歌曲：")
    url = "http://songsearch.kugou.com/song_search_v2?callback=jQuery1124006980366032059648_1518578518932&keyword="+keyword
    content = requests.get(url).text
    songname = re.findall('"SongName":"(.*?)"',content)
    k=0
    for i  in songname :
        k+=1
        print('{0}:{1}'.format(k,i))
    print('-'*40)
    choice=int(input('请选择下载歌曲编号：'))
    filehash = re.findall('"FileHash":"(.*?)"',content)[choice-1]
    
    hash_url = "http://www.kugou.com/yy/index.php?r=play/getdata&hash="+filehash 
    hash_content = requests.get(hash_url).text
    play_url = re.findall('"play_url":"(.*?)"',hash_content)
    play_url = ''.join(play_url)
    download_url = play_url.replace("\\","")

    with open(dataDir+os.sep+songname[choice-1]+".mp3","wb")as fp:
        fp.write(requests.get(download_url).content)
        print('歌曲{}下载成功'.format(songname[choice-1]))
        print('歌曲保存路径为：{}'.format(dataDir))
    #接收用户退出选项
    print('-'*40)
    choice=input('你确定要退出系统吗（y/n)')
    if choice.lower() == 'y':
        #退出系统
        sys.exit(0)
    else:
        continue
        pass
    pass
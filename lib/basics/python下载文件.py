from urllib import request
url = 'http://v4.qutoutiao.net/toutiao_video_zdgq_online/d637190678d54cf6aa221c238b645691/hd.mp4'
with request.urlopen(url) as web:
    with open('x.mp4', 'wb') as outfile:
        outfile.write(web.read())

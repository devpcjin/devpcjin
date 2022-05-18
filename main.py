import feedparser, datetime

velog_blog_rss_uri="https://v2.velog.io/rss/@pc_jin"
feed = feedparser.parse(velog_blog_rss_uri)

markdown_text = """
마크다운에 넣고 싶은 내용들.. 생략하겠습니다
### ✍ Recent blog posts 
""" # list of blog posts will be appended here


j=0
for i in feed['entries']:
    j+= 1
    if j >5:
        break
    else:
        # dt = datetime.datetime.strptime(i['published'], "%a, %d %B %Y %H:%M:%S %z").strftime("%B %d, %Y")
        dt = i['published']
        # markdown_text += f"[{i['title']}]({i['link']}) - {dt}<br>\n"
        markdown_text += f"[{i['title']}]({i['link']}) <br>\n"
        print(i['link'], i['title'])

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()  

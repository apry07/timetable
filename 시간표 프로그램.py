import ctypes
import datetime
import os
import sched
import time
from PIL import Image, ImageFont, ImageDraw

current_date = datetime.date.today()
a = current_date
print(a)
img = Image.new("RGB",(1980,1080), (255,255,255))
d = ImageDraw.Draw(img)

weekdays = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
current_weekday = weekdays[current_date.weekday()]

datetime1 = datetime.datetime.now()

nyear = datetime1.year
nmoth = datetime1.month
ndays = datetime1.day

print(nyear,nmoth,ndays)

b = current_weekday
print(b)
if b == '월요일':
    def mon():
        fnt = ImageFont.truetype("malgunbd.ttf", 60)
        d.text((1550,150), "월요일", font=fnt, fill=(000,000,000))

        fnt = ImageFont.truetype("malgunbd.ttf", 60)
        d.text((1350,150), " %d일"%ndays , font=fnt, fill=(000,000,000))
        fnt = ImageFont.truetype("malgunbd.ttf", 60)
        d.text((1000,150), "%d년"%nyear , font=fnt, fill=(000,000,000))
        fnt = ImageFont.truetype("malgunbd.ttf", 60)
        d.text((1200,150), " %d월"%nmoth , font=fnt, fill=(000,000,000))
        #1교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,300), "자습", font=fnt, fill=(000,000,000))
        #2교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,400), "한국사 A", font=fnt, fill=(000,000,000))
        #3교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,500), "체육", font=fnt, fill=(000,000,000))
        #4교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,600), "수학", font=fnt, fill=(000,000,000))
        #5교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,700), "과학탐구실험", font=fnt, fill=(000,000,000))
        #6교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,800), "영어 B", font=fnt, fill=(000,000,000))
        #7교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,900), "한국사 A", font=fnt, fill=(000,000,000))
    mon()

if b == '화요일':
    def tue():
        fnt = ImageFont.truetype("malgunbd.ttf", 60)
        d.text((1550,150), "화요일", font=fnt, fill=(000,000,000))

        fnt = ImageFont.truetype("malgunbd.ttf", 60)
        d.text((1350,150), " %d일"%ndays , font=fnt, fill=(000,000,000))
        fnt = ImageFont.truetype("malgunbd.ttf", 60)
        d.text((1000,150), "%d년"%nyear , font=fnt, fill=(000,000,000))
        fnt = ImageFont.truetype("malgunbd.ttf", 60)
        d.text((1200,150), " %d월"%nmoth , font=fnt, fill=(000,000,000))
        #1교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,300), "국어", font=fnt, fill=(000,000,000))
        #2교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,400), "수학", font=fnt, fill=(000,000,000))
        #3교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,500), "사회", font=fnt, fill=(000,000,000))
        #4교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,600), "과학", font=fnt, fill=(000,000,000))
        #5교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,700), "영어", font=fnt, fill=(000,000,000))
        #6교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,800), "한국사", font=fnt, fill=(000,000,000))
        #7교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,900), "자율", font=fnt, fill=(000,000,000))
    tue()

if b == '수요일':
    def wed():
        fnt = ImageFont.truetype("malgunbd.ttf", 60)
        d.text((1550,150), "수요일", font=fnt, fill=(000,000,000))

        fnt = ImageFont.truetype("malgunbd.ttf", 60)
        d.text((1350,150), " %d일"%ndays , font=fnt, fill=(000,000,000))
        fnt = ImageFont.truetype("malgunbd.ttf", 60)
        d.text((1000,150), "%d년"%nyear , font=fnt, fill=(000,000,000))
        fnt = ImageFont.truetype("malgunbd.ttf", 60)
        d.text((1200,150), " %d월"%nmoth , font=fnt, fill=(000,000,000))
        #1교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,300), "사회", font=fnt, fill=(000,000,000))
        #2교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,400), "미술", font=fnt, fill=(000,000,000))
        #3교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,500), "진로", font=fnt, fill=(000,000,000))
        #4교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,600), "수학", font=fnt, fill=(000,000,000))
        #5교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,700), "영어A", font=fnt, fill=(000,000,000))
        #6교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,800), "과학C", font=fnt, fill=(000,000,000))
        #7교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,900), "국어A", font=fnt, fill=(000,000,000))
    wed()

if b == '목요일':
    def thur():
        fnt = ImageFont.truetype("malgunbd.ttf", 60)
        d.text((1550,150), "목요일", font=fnt, fill=(000,000,000))

        fnt = ImageFont.truetype("malgunbd.ttf", 60)
        d.text((1350,150), " %d일"%ndays , font=fnt, fill=(000,000,000))
        fnt = ImageFont.truetype("malgunbd.ttf", 60)
        d.text((1000,150), "%d년"%nyear , font=fnt, fill=(000,000,000))
        fnt = ImageFont.truetype("malgunbd.ttf", 60)
        d.text((1200,150), " %d월"%nmoth , font=fnt, fill=(000,000,000))

        #1교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,300), "국어", font=fnt, fill=(000,000,000))
        #2교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,400), "수학", font=fnt, fill=(000,000,000))
        #3교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,500), "사회", font=fnt, fill=(000,000,000))
        #4교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,600), "과학", font=fnt, fill=(000,000,000))
        #5교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,700), "영어", font=fnt, fill=(000,000,000))
        #6교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,800), "한국사", font=fnt, fill=(000,000,000))
        #7교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,900), "자율", font=fnt, fill=(000,000,000))
    thur()

if b == '금요일':
    def fri():
        fnt = ImageFont.truetype("malgunbd.ttf", 60)
        d.text((1550,150), "금요일", font=fnt, fill=(000,000,000))

        fnt = ImageFont.truetype("malgunbd.ttf", 60)
        d.text((1350,150), " %d일"%ndays , font=fnt, fill=(000,000,000))
        fnt = ImageFont.truetype("malgunbd.ttf", 60)
        d.text((1000,150), "%d년"%nyear , font=fnt, fill=(000,000,000))
        fnt = ImageFont.truetype("malgunbd.ttf", 60)
        d.text((1200,150), " %d월"%nmoth , font=fnt, fill=(000,000,000))

        #1교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,300), "국어", font=fnt, fill=(000,000,000))
        #2교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,400), "수학", font=fnt, fill=(000,000,000))
        #3교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,500), "사회", font=fnt, fill=(000,000,000))
        #4교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,600), "과학", font=fnt, fill=(000,000,000))
        #5교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,700), "영어", font=fnt, fill=(000,000,000))
        #6교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,800), "한국사", font=fnt, fill=(000,000,000))
        #7교시
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,900), "자율", font=fnt, fill=(000,000,000))
    fri()

if b == '토요일':
    def sat():
        fnt = ImageFont.truetype("malgunbd.ttf", 60)
        d.text((1550,150), "토요일", font=fnt, fill=(000,000,000))

        fnt = ImageFont.truetype("malgunbd.ttf", 60)
        d.text((1350,150), " %d일"%ndays , font=fnt, fill=(000,000,000))
        fnt = ImageFont.truetype("malgunbd.ttf", 60)
        d.text((1000,150), "%d년"%nyear , font=fnt, fill=(000,000,000))
        fnt = ImageFont.truetype("malgunbd.ttf", 60)
        d.text((1200,150), " %d월"%nmoth , font=fnt, fill=(000,000,000))
        
        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,300), "일정 없음", font=fnt, fill=(000,000,000))
    sat()

if b == '일요일':
    def sun():
        fnt = ImageFont.truetype("malgunbd.ttf", 60)
        d.text((1550,150), "일요일", font=fnt, fill=(000,000,000))
        
        fnt = ImageFont.truetype("malgunbd.ttf", 60)
        d.text((1350,150), " %d일"%ndays , font=fnt, fill=(000,000,000))
        fnt = ImageFont.truetype("malgunbd.ttf", 60)
        d.text((1000,150), "%d년"%nyear , font=fnt, fill=(000,000,000))
        fnt = ImageFont.truetype("malgunbd.ttf", 60)
        d.text((1200,150), " %d월"%nmoth , font=fnt, fill=(000,000,000))

        fnt = ImageFont.truetype("malgun.ttf", 40)
        d.text((1500,300), "일정 없음", font=fnt, fill=(000,000,000))
    sun()

img.save('c:/Users/user/Desktop/images/images.png')
new_wallpaper_path = "c:/Users/user/Desktop/images/images.png"
img.show()

SystemParametersInfo = ctypes.windll.user32.SystemParametersInfoW

def set_wallpaper(path):
    result = SystemParametersInfo(20, 0, path, 3)
    return result

def schedule_wallpaper_change(change_time, wallpaper_path):
    scheduler = sched.scheduler(time.time, time.sleep)
    current_time = datetime.datetime.now()
    
    if current_time > change_time:
        change_time += datetime.timedelta(days=1)
    
    time_diff = (change_time - current_time).total_seconds()
    scheduler.enter(time_diff, 1, set_wallpaper, (wallpaper_path,))
    
    print(f"배경화면 변경이 예약되었습니다. 변경 시간: {change_time}")
    scheduler.run()
print("오늘은", current_weekday, "입니다.")
target_time = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
schedule_wallpaper_change(target_time, new_wallpaper_path)
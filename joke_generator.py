import random

jokes = [
    "為什麼數學書總是感到沮喪？因為它有太多的問題！",
    "為什麼海洋是藍色的？因為魚會游泳，不會上岸！",
    "為什麼電腦累？因為它在處理數據！",
    "為什麼狗狗喜歡坐在陽光下？因為它們想成為熱狗！"
]

def tell_joke():
    return random.choice(jokes)

# 調用函數並顯示一個隨機笑話
print(tell_joke())
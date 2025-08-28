from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# ヘッドレスモードでブラウザ起動
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)

# NHKニュースのトップページへアクセス
driver.get("https://www3.nhk.or.jp/news/")

# 少し待機（ページ読み込みのため）
time.sleep(2)

# 見出しを取得
headlines = driver.find_elements(By.CLASS_NAME, "content--title")

# 結果を表示
print("📢 NHKニュース見出し一覧：")
for idx, headline in enumerate(headlines, 1):
    print(f"{idx}. {headline.text}")

# ブラウザを閉じる
driver.quit()

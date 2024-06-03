from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os

def main():
    
    os.system("title fLUIDscripts. Choukettas twich")

    print("SELECTION DU PROXY")
    print("Sélectionnez un serveur. Entrez le numéro du serveur et appuyez sur Entrée.")
    for i in range(1, 5):
        print(f"Server {i} (en ligne)")

    proxy_choice = int(input(">> "))
    proxy_servers = {
        1: "https://www.blockaway.net",
        2: "https://www.croxy.network",
        3: "https://www.croxy.org",
        4: "https://www.youtubeunblocked.live",
    }
    proxy_url = proxy_servers.get(proxy_choice)

    print("\n" * 3)
    print("NOM DU COMPTE TWITCH CIBLE")
    print("Entrez le nom du compte Twitch cible (uniquement le nom d'utilisateur) :")
    twitch_username = input(">> ")

    print("\n" * 3)
    print("NOMBRE DE TÉLÉSPECTATEURS")
    print("Combien de téléspectateurs doivent être envoyés ? (Des nombres plus élevés peuvent causer des erreurs !)")
    proxy_count = int(input(">> "))

    chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    driver_path = 'chromedriver.exe'

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--disable-extensions')

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(proxy_url)

    for i in range(proxy_count):
        driver.execute_script("window.open('" + proxy_url + "')")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(proxy_url)

        text_box = driver.find_element(By.ID, 'url')
        text_box.send_keys(f'www.twitch.tv/{twitch_username}')
        text_box.send_keys(Keys.RETURN)

if __name__ == '__main__':
    main()

# ==========================================
# Copyright 2024 - Choukettas Corp 
# ==========================================
import requests
import warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from colorama import Fore, Style, init
from pystyle import Center, Colors, Colorate
import os
import time

class Colors:
    reset = '\033[0m'

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_escape(r, g, b):
    return f'\033[38;2;{r};{g};{b}m'

def gradient_text(text, start_color, end_color, steps=10):
    start_rgb = hex_to_rgb(start_color)
    end_rgb = hex_to_rgb(end_color)
    
    gradient_text = ""
    length = len(text)
    step_size = max(1, length // steps)
    
    for i in range(0, length, step_size):
        r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * i / length)
        g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * i / length)
        b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * i / length)
        chunk = text[i:i+step_size]
        gradient_text += rgb_to_escape(r, g, b) + chunk
        
    return gradient_text + Colors.reset

def center_text(text):
    terminal_width = os.get_terminal_size().columns
    text_length = len(text)
    return ' ' * ((terminal_width - text_length) // 2) + text

def main():

    os.system(f"title Choukettasviewer. bot_Viewer 2.0.1 ")

    # Proxy URLS
    proxy_servers = {

        1: "https://www.blockaway.net",
        2: "https://www.croxy.network",
        3: "https://www.croxy.org",
        4: "https://www.youtubeunblocked.live",
        5: "https://www.croxyproxy.net",
    }

    # Selecting proxy server

    for i in range(1, 5):
        print(gradient_text(center_text(f"Server (online) {i}"), '#0000FF', '#800080'))
    proxy_choice = int(input(gradient_text(">>", '#0000FF', '#800080')))
    proxy_url = proxy_servers.get(proxy_choice)

    # Select Twitch Account
    print('')
    print('')
    print(gradient_text(center_text("Veuillez fournir le nom d’utilisateur ( Compte Twitch cible)"), '#0000FF', '#800080'))
    print(gradient_text(center_text("Example: timkt94_off "), '#0000FF', '#800080'))
    twitch_username = input(gradient_text(">>", '#0000FF', '#800080'))

    # Select Proxys Amount
    print('')
    print('')
    print(gradient_text(center_text("Combien de spectateurs faut-il envoyer ?"), '#0000FF', '#800080'))
    print(gradient_text(center_text("(Des nombres plus élevés peuvent provoquer des bugs)!"), '#0000FF', '#800080'))
    print(gradient_text(center_text("(je recomende entre 20 et 50)!"), '#0000FF', '#800080'))   
    proxy_count = int(input(gradient_text(">>", '#0000FF', '#800080')))

    # Next Step
    os.system("cls")

    print('')
    print('')
    print(gradient_text(center_text("Le bot démarre et envoie les spectateurs."), '#0000FF', '#800080'))
    print(gradient_text(center_text("Si tous les spectateurs n’arrivent pas,"), '#0000FF', '#800080'))
    print(gradient_text(center_text("redémarrez le bot ou modifiez le serveur proxy."), '#0000FF', '#800080'))


    chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    driver_path = 'chromedriver.exe'

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.binary_location = chrome_path
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(proxy_url)

    for i in range(proxy_count):
        driver.execute_script("window.open('" + proxy_url + "')")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(proxy_url)

        text_box = driver.find_element(By.ID, 'url')
        text_box.send_keys(f'www.twitch.tv/{twitch_username}')
        text_box.send_keys(Keys.RETURN)

    # Ende
    os.system("cls")

    print(gradient_text(center_text("Les téléspectateurs sont arrivés."), '#00FFFF', '#0000FF'))
    print(gradient_text(center_text(""), '#00FFFF', '#0000FF'))
    print(gradient_text(center_text("Si le nombre de spectateurs diminue ou si le bot cesse de fonctionner,"), '#00FFFF', '#0000FF'))
    print(gradient_text(center_text("redémarrer le script ou d’essayer un autre serveur proxy."), '#00FFFF', '#0000FF'))
    print(gradient_text(center_text(""), '#00FFFF', '#0000FF'))
    print(gradient_text(center_text("Gardez la fenêtre ouverte aussi longtemps que vous souhaitez utiliser le bot."), '#00FFFF', '#0000FF'))
    print(gradient_text(center_text("Lorsque vous souhaitez quitter le bot, appuyez sur la touche ENTRÉE ou fermez la fenêtre."), '#00FFFF', '#0000FF'))
    input(gradient_text(">>", '#00FFFF', '#0000FF'))    
    driver.quit()


if __name__ == '__main__':
    main()

# ==========================================
# Copyright 2024 - Choukettas94.
# ==========================================

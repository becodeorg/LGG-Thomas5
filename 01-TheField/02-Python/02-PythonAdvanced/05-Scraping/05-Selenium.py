# =======================================================
# Name: Hamers Robin
# GitHub: Rhodham96
# Year: 2025
# Description: Scrap informations on NYTimes
# =======================================================

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

url = "https://www.nytimes.com/"

# may need to change Safari with Firefox
driver = webdriver.Safari()
driver.get(url)

sleep(2)

# You may need to change the cookie Value (check in you browser -> Web Inspector -> Storage -> Cookies, after clicking the first button, this cookie will appear)

cookie = {'name' : 'fides_consent', 'value' : '%7B%22consent%22%3A%7B%7D%2C%22identity%22%3A%7B%22fides_user_device_id%22%3A%22fc660568-3ec2-42ea-8320-35e830640263%22%7D%2C%22fides_meta%22%3A%7B%22version%22%3A%220.9.0%22%2C%22createdAt%22%3A%222025-03-25T09%3A02%3A30.940Z%22%2C%22updatedAt%22%3A%222025-03-25T09%3A03%3A01.645Z%22%2C%22consentMethod%22%3A%22reject%22%7D%2C%22tcf_consent%22%3A%7B%22system_consent_preferences%22%3A%7B%7D%2C%22system_legitimate_interests_preferences%22%3A%7B%7D%7D%2C%22fides_string%22%3A%22CQO03QAQO03QAGXABBENBiFgAAAAAAAAAAAAAAAAAAAA%2C1~%22%2C%22tcf_version_hash%22%3A%2209336ff51657%22%7D', 'domain': '.nytimes.com'}
driver.add_cookie(cookie)

driver.refresh()

sleep(2)

# Trouver l'élément avec la classe 'css-hqisq1' et cliquer sur le bouton enfant avec JavaScript
driver.execute_script("""
    var parentElement = document.querySelector('.css-hqisq1'); 
    if (parentElement) {
        var button = parentElement.querySelector('button');  // Trouver le bouton dans cet élément
        if (button) {
            button.click();  // Cliquer sur le bouton
        } else {
            console.log('Bouton introuvable');
        }
    } else {
        console.log('Élément parent introuvable');
    }
""")

sleep(2)

article_titles = driver.find_elements(By.XPATH, "//section[@class='story-wrapper']//a//div[@class='css-xdandi']//p")
all_titles = []
for title in article_titles:
    all_titles.append(title.text)

print(all_titles)

sleep(2)

driver.close()
import time
from selenium import webdriver

# initialise the selenium webdriver
driver = webdriver.Chrome()

def load_twitch():
    # load the current twitch live streams that have the tag 'drops enabled'
    driver.get('https://www.twitch.tv/directory/all/tags/c2542d6d-cd10-4532-919b-3d19f30a768b')
    print("twitch loaded correctly")


def get_element(xpath):
     # wait for the previous command to be executed (e.g. page load)
    time.sleep(5)
    return driver.find_element_by_xpath(xpath)


def load_stream():
    first_twitch_stream = get_element("/html/body/div[1]/div/div[2]/div[2]/main/div[1]/div[3]/div/div/div/div[4]/div/div[1]/div[2]/div/div/div/div/article/div[1]/div/div/div[1]/div/a")
    print("twitch stream successfully found")
    first_twitch_stream.click()
    print("twitch stream successfully loaded")


def main():
    load_twitch()
    load_stream()

    video_player = get_element("/html/body/div[1]/div/div[2]/div[2]/main/div[2]/div[3]/div/div/div[2]/div/div[2]/div/div/div/div[5]")
    print("video player element successfully found")

    if not video_player.get_attribute("class") == "tw-c-text-overlay":
        print("stream is no longer live")
        print(video_player.get_attribute("class"))
        print("loading new stream...")
        load_twitch()
        load_stream()
    else:
        print("stream is live")

if __name__ == "__main__": 
    main()
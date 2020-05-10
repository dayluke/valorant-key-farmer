import time
from selenium import webdriver

time_out_delay = 5

# every x minutes, we will check if the stream is still live
live_time_checker = 1 * 60

# initialise the selenium webdriver
driver = webdriver.Chrome()

def load_twitch():
    # load the current twitch live streams that have the tag 'drops enabled'
    driver.get('https://www.twitch.tv/directory/all/tags/c2542d6d-cd10-4532-919b-3d19f30a768b')
    print("twitch loaded correctly")


def get_element(xpath):
     # wait for the previous command to be executed (e.g. page load)
    time.sleep(time_out_delay)
    return driver.find_element_by_xpath(xpath)


def load_stream():
    first_twitch_stream = get_element("/html/body/div[1]/div/div[2]/div[2]/main/div[1]/div[3]/div/div/div/div[4]/div/div[1]/div[2]/div/div/div/div/article/div[1]/div/div/div[1]/div/a")
    print("twitch stream successfully found")
    first_twitch_stream.click()
    print("twitch stream successfully loaded")


def is_stream_live():
    video_player = get_element("/html/body/div[1]/div/div[2]/div[2]/main/div[2]/div[3]/div/div/div[2]/div/div[2]/div/div/div/div[5]")
    print("video player element successfully found")

    return video_player.get_attribute("class") == "tw-c-text-overlay" or 
        get_element("/html/body/div[1]/div/div[2]/div[2]/main/div[2]/div[3]/div/div/div[2]/div/div[2]/div/div/div/div[4]").get_attribute("class") == "tw-c-text-overlay"


def get_current_time():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)


def main():
    load_twitch()
    load_stream()
    
    while True:
        if not is_stream_live():
            print("stream is no longer live")
            get_current_time()
            print("loading new stream...")
            load_twitch()
            load_stream()
        else:
            print("stream is still live")
            get_current_time()
            time.sleep(live_time_checker)


if __name__ == "__main__": 
    main()
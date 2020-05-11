import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

time_out_delay = 5

# every x minutes, we will check if the stream is still live
live_time_checker = 1 * 60

# initialise the selenium webdriver
driver = webdriver.Chrome()

def load_twitch():
    # load the current twitch live streams that have the tag 'drops enabled'
    driver.get('https://www.twitch.tv/directory/all/tags/c2542d6d-cd10-4532-919b-3d19f30a768b')
    print("twitch loaded correctly")


def get_element(classname):
    # wait for the previous command to be executed (e.g. page load)
    time.sleep(time_out_delay)
    try:
        # finds all elements that contain the given classname
        elem = driver.find_element_by_class_name(classname)
        return elem
    except NoSuchElementException:
        print("cannot find element with class name", classname)
        return None



def load_stream():
    first_twitch_stream = get_element("tw-c-text-alt")
    print("twitch stream successfully found")
    first_twitch_stream.click()
    print("twitch stream successfully loaded")


def is_stream_live():
    video_player = get_element("extensions-video-overlay-size-container")
    if video_player == None:
        return False
    else:
        print("video player element successfully found")
        return True


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
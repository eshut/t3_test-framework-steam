from framework.BaseElement import *


class GetTextXpath:
    def __init__(self, Xpath):
        element = driver.find_element_by_xpath(Xpath)
        return(element.text)
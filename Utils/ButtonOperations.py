from framework.framework import *


class ClickButtonClass:
    def __init__(self, ButoonClass):
        toClick = driver.find_element_by_class_name(ButoonClass)
        toClick.click()
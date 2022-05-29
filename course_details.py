import logging
import time

import pymongo
from selenium import webdriver as wd

class course_details():
    """Class: Called to extract data about course details from iNeuron website
        Description: Contains collection and extraction functions that collect and extract
        data from the website"""

    def __init__(a, u):
        a.u = u

    def collection(a):
        """Method : Collects list of all available courses in the given website

        Description : Scans the webpage for titles of the courses"""

        browser = wd.Chrome()
        browser.maximize_window()
        browser.get(a.u)

        course = {}
        n = []
        try:
            course_name = browser.find_elements_by_xpath("//h5[@class='Course_course-title__2rA2S']")
            time.sleep(1)
            for i in course_name:
                N = i.text
                n.append(N)
            return n
        except Exception as d:
            logging.info(d)

    def extraction(a):
        """
        Method : Collects details of given course in the given website

        Description : Scans the webpage for description, syllabus and price of the courses"""
        ###Selects the course names and collects course description, syllabus and price details of the course###

        try:
            browser = wd.Chrome()
            browser.maximize_window()
            browser.get(a.u)

            url_op = browser.find_element_by_link_text(e)
            url_op.click()
            time.sleep(1)

            course_description = browser.find_element_by_class_name("Hero_course-desc__26_LL")
            cd = course_description.text
            time.sleep(1)

            syll = browser.find_element_by_xpath("//div[@class='CourseLearning_card__WxYAo card']")
            course_syllabus = syll.find_element_by_tag_name("ul")
            cs = course_syllabus.text
            time.sleep(1)

            course_price = browser.find_element_by_xpath('//span[@style="font-family: Poppins;"]')
            p = course_price.text
            time.sleep(1)

            course = {'Course name': e, 'Description': cd, 'Topics covered': cs, 'Price': p}
            course['Course name'] = e
            course['Description'] = cd
            course['Topics covered'] = cs
            course['Price'] = p
            return course
        except Exception as d:
            logging.info(d)

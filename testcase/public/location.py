#-*- coding: utf-8 -*-
__author__ = 'tsbc'

from selenium import webdriver
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def find_Element(driver, tag, criteria):
	if tag.lower() == "id":
		return driver.find_element_by_id(criteria)
	elif tag.lower() == "name":
		return driver.find_element_by_name(criteria)
	elif tag.lower() == "class_name":
		return driver.find_element_by_class_name(criteria)
	elif tag.lower() == "tag_name":
		return driver.find_element_by_tag_name(criteria)
	elif tag.lower() == "link_text":
		return driver.find_element_by_link_text(criteria)
	elif tag.lower() == "partial_link_text":
		return driver.find_element_by_partial_link_text(criteria)
	elif tag.lower() == "css":
		return driver.find_element_by_css_selector(criteria)
	elif tag.lower() == "xpath":
		return driver.find_element_by_xpath(criteria)

def findId(driver, id):

	element = driver.find_element_by_id(id)
	return element

def findName(driver, name):
	element = driver.find_element_by_name(name)
	return element


def findClassName(driver, name):
	element = driver.find_element_by_class_name(name)
	return element


def findTagName(driver, name):
	element = driver.find_element_by_tag_name(name)
	return element


def findLinkText(driver, text):
	element = driver.find_element_by_link_text(text)
	return element


def findPartialLink(driver, text):
	element = driver.find_element_by_partial_link_text(text)
	return element


def findXpath(driver, xpath):
	element = driver.find_element_by_xpath(xpath)
	return element


def findCss(driver, css):
	element = driver.find_element_by_css_selector(css)
	return element


"""
定位一组元素：
find_elements_by_id()
find_elements_by_name()
find_elements_by_class_name()
find_elements_by_tag_name()
find_elements_by_link_text()
find_elements_by_partial_link_text()
find_elements_by_xpath()
find_elements_by_css_selector()
"""


def findsId(driver, id):
	elements = driver.find_elements_by_id(id)
	return elements


def findsName(driver, name):
	elements = driver.find_elements_by_name(name)
	return elements


def findsClassName(driver, name):
	elements = driver.find_elements_by_class_name(name)
	return elements


def findsTagName(driver, name):
	elements = driver.find_elements_by_tag_name(name)
	return elements


def findsLinkText(driver, text):
	elements = driver.find_elements_by_link_text(text)
	return elements


def findsPartialLink(driver, text):
	elements = driver.find_elements_by_partial_link_text(text)
	return elements


def findsXpath(driver, xpath):
	elements = driver.find_elements_by_xpath(xpath)
	return elements


def findsCss(driver, css):
	elements = driver.find_elements_by_css_selector(css)
	return elements
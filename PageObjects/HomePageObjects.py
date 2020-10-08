from Resources.Locators import Locators
from Resources.TestData import TestData


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.gethired_button = Locators.GETHIRED_BUTTON_XPATH
        self.signin_button = Locators.SIGNIN_BUTTON_XPATH
        self.nav_menu = Locators.NAVBAR_MENU_XPATH
        self.applybpo_logo = Locators.APPLYBPO_lOGO_XPATH
        self.trustedpartner_button = Locators.TRUSTEDPARTNER_BUTTON_XPATH
        self.talent_button = Locators.TALENT_BUTTON_XPATH
        self.onevideotext_text = Locators.ONEVIDEO_TEXT_XPATH
        self.hero_image = Locators.HERO_IMAGE_XPATH
        self.dreamjobinterview_text = Locators.DREAMJOBINTERVIEW_TEXTVIEW_XPATH
        self.search_input = Locators.SEARCH_INPUT_XPATH
        self.alllocation_button = Locators.ALLLOCATION_BUTTON_XPATH
        self.urgentslidetoggle_button = Locators.URGENTSLIDETOGGLE_BUTTON_XPATH
        self.urgent_text = Locators.URGENT_TEXT_XPATH
        self.cardview = Locators.CARD_VIEW_XPATH
        self.cardview_image = Locators.CARDIMAGE_IMAGE_XPATH
        self.cardgroupprimary_text = Locators.CARDGROUPPRIMARYINFORMATION_TEXT_XPATH
        self.cardtitle_text = Locators.CARDTITLEINFROMATION_VIEW_XPATH
        self.cardtitlebelow_text = Locators.CARDTITLEINFROMATIONBELOW_VIEW_XPATH
        self.cardgroupsecondaryinfo_text = Locators.CARDGROUPSECONDARYINFORMATION_TEXT_XPATH
        self.category_text = Locators.CARDCATEGORYINFROMATION_VIEW_XPATH
        self.copylink_button = Locators.CARDCOPYLINK_BUTTON_XPATH
        self.currencyvalue_text = Locators.CARDCURRENCY_TEXT_XPATH
        self.details_button = Locators.CARDDETAILS_BUTTON_XPATH
        self.backarrowcount_button = Locators.BACKARROWCOUNT_BUTTON_XPATH
        self.numbercount_button = Locators.NUMBERCOUNT_BUTTON_XPATH
        self.frontarrowcount_button = Locators.FRONTARROWCOUNT_BUTTON_XPATH
        self.applybpo2_logo = Locators.APPLYBPO2_lOGO_XPATH
        self.areyouexhausted_text = Locators.AREYOUEXHAUSTED_TEXT_XPATH
        self.footerblock_text = Locators.FOOTERBLOCK_TEXT_XPATH
        self.followus_text = Locators.FOLLOWUS_TEXT_XPATH
        self.affiliates_text = Locators.AFFILIATTES_TEXT_XPATH
        self.facebookfooter_button = Locators.FACEBOOKFOOTER_BUTTON_XPATH
        self.twitterfooter_button = Locators.TWITTERFOOTER_BUTTON_XPATH
        self.instagramfooter_button = Locators.INSTAGRAMFOOTER_BUTTON_XPATH
        self.bposeats_image = Locators.BPOSEATSFOOTERICON_IMAGE_XPATH
        self.bposeatsfooter_text = Locators.BPOSEATSFOOTER_TEXT_XPATH
        self.contactus_text = Locators.CONTACTUSFOOTER_TEXT_XPATH
        self.legalfooter_text = Locators.LEGALFOOTER_TEXT_XPATH
        self.emailfooter_text = Locators.EMAILFOOTER_TEXT_XPATH
        self.phonefooter_text = Locators.PHONEFOOTER_TEXT_XPATH
        self.privacypolicyfooter_text = Locators.PRIVACYPOLICYFOOTER_TEXT_XPATH
        self.copyrightfooter_text = Locators.COPYRIGHTFOOTER_TEXT_XPATH

    def click_signin_button(self):
        self.driver.find_element_by_xpath(self.signin_button).click()

    def click_gethired_button(self):
        self.driver.find_element_by_xpath(self.gethired_button).click()

    def nav_menu(self):
        self.driver.find_element_by_xpath(self.nav_menu())

    def applybpologo_image(self):
        self.driver.find_element_by_xpath(self.applybpo_logo)

    def click_trustedpartner_button(self):
        self.driver.find_element_by_xpath(self.trustedpartner_button).click()

    def click_talent_button(self):
        self.driver.find_element_by_xpath(self.talent_button).click()

    def onevideo_text(self):
        self.driver.find_element_by_xpath(self.onevideotext_text)

    def hero_image(self):
        self.driver.find_element_by_xpath(self.hero_image)

    def dreamjobinterview_text(self):
        self.driver.find_element_by_xpath(self.dreamjobinterview_text)

    def search_input(self):
        self.driver.find_element_by_xpath(self.search_input).sendKeys(TestData.SEARCH_TEXT)

    def alllocation_button(self):
        self.driver.find_element_by_xpath(self.alllocation_button).click()

    def urgentslider_button(self):
        self.driver.find_element_by_xpath(self.urgentslidetoggle_button).click()

    def urgent_text(self):
        self.driver.find_element_by_xpath(self.urgent_text)

    def cardview(self):
        self.driver.find_element_by_xpath(self.cardview)

    def cardview_image(self):
        self.driver.find_element_by_xpath(self.cardview_image)

    def cardgroupprimary_text(self):
        self.driver.find_element_by_xpath(self.cardgroupprimary_text)

    def cardtitle_text(self):
        self.driver.find_element_by_xpath(self.cardtitle_text)

    def cardtitlebelow_text(self):
        self.driver.find_element_by_xpath(self.cardtitlebelow_text)

    def cardgroupsecondayinfromation_text(self):
        self.driver.find_element_by_xpath(self.cardgroupsecondayinfromation_text)

    def category_text(self):
        self.driver.find_element_by_xpath(self.category_text)

    def copylink_button(self):
        self.driver.find_element_by_xpath(self.copylink_button).click()

    def currencyvalue_text(self):
        self.driver.find_element_by_xpath(self.currencyvalue_text)

    def details_button(self):
        self.driver.find_element_by_xpath(self.details_button).click()

    def backarrowcount_button(self):
        self.driver.find_element_by_xpath(self.backarrowcount_button).click()

    def numbercount_button(self):
        self.driver.find_element_by_xpath(self.numbercount_button).click()

    def frontarrowcount_button(self):
        self.driver.find_element_by_xpath(self.frontarrowcount_button).click()

    def applybpologo2_image(self):
        self.driver.find_element_by_xpath(self.applybpo2_logo)

    def areyouexhausted_text(self):
        self.driver.find_element_by_xpath(self.areyouexhausted_text)

    def footerblock_text(self):
        self.driver.find_element_by_xpath(self.footerblock_text)

    def followus_text(self):
        self.driver.find_element_by_xpath(self.followus_text)

    def affiliates_text(self):
        self.driver.find_element_by_xpath(self.affiliates_text)

    def facebookfooter_button(self):
        self.driver.find_element_by_xpath(self.facebookfooter_button).click()

    def twitterfooter_button(self):
        self.driver.find_element_by_xpath(self.twitterfooter_button).click()

    def instagramfooter_button(self):
        self.driver.find_element_by_xpath(self.instagramfooter_button).click()

    def bposeats_image(self):
        self.driver.find_element_by_xpath(self.bposeats_image)

    def bposeatsfooter_text(self):
        self.driver.find_element_by_xpath(self.bposeatsfooter_text)

    def contactus_text(self):
        self.driver.find_element_by_xpath(self.contactus_text)

    def legalfooter_text(self):
        self.driver.find_element_by_xpath(self.legalfooter_text)

    def emailfooter_text(self):
        self.driver.find_element_by_xpath(self.emailfooter_text)

    def phonefooter_text(self):
        self.driver.find_element_by_xpath(self.phonefooter_text)

    def privacypolicyfooter_text(self):
        self.driver.find_element_by_xpath(self.privacypolicyfooter_text)

    def copyrightfooter_text(self):
        self.driver.find_element_by_xpath(self.copyrightfooter_text)
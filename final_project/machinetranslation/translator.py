"""
Instantiate watson translator and use it
"""
import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

def englishToFrench(englishText):
    """
    returns the french translation of englishText
    """
    if len(englishText)<1:
        return None
    result = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
    frenchText = result['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    """
    returns the english translation of frenchText
    """
    if len(frenchText)<1:
        return None
    result = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()
    englishText = result['translations'][0]['translation'] 
    return englishText

load_dotenv()
API_KEY = os.environ['apikey']
URL = os.environ['url']

API_VERSION = '2018-05-01'

try:
    authenticator = IAMAuthenticator(API_KEY)
    language_translator = LanguageTranslatorV3(
        version = API_VERSION,
        authenticator=authenticator
    )
    language_translator.set_service_url(URL)
except ApiException as ex:
    print ("Method failed with status code " + str(ex.code) + ": " + ex.message)

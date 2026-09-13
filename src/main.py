import csv
import asyncio
from urllib.parse import quote
import requests
import json
from urllib.parse import quote
from openai import OpenAI
from brightdata import SyncBrightDataClient, BrightDataClient
from google import genai


filepath = "questions.csv"
brightdataKey = "BRIGHT_DATA_API_KEY"
geminiKey = "GEMINI_API_KEY"
openAIApikey = "OPENAI_API_KEY"
openAIClient = OpenAI(
  api_key = openAIApikey
)
geminiClient = genai.Client(api_key = geminiKey)

def main():
  allrows = readCsv(filepath)
  row = [
    "Question", 
    # "ChatGPT", "Gemini", "Google", "Bing",
    "Wikipedia"
  ]
  with open('output-wikipedia2.csv', "w", newline = "", encoding = "utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(row)
    for row in allrows[22:]:
      question = row[1]
      print(question)
      chatGPTResponse = runQueryChatGPT(question)
      print("------")
      geminiResponse = runQueryGemini(question)
      print("------")
      googleResponse = runQueryGoogle(question)
      print("------")
      bingResponse = runQueryBing(question)
      print("------")
      wikipediaResponse = runQueryWikipedia(question)
      print(wikipediaResponse)
      row = [
        question,
        chatGPTResponse,
        geminiResponse,
        googleResponse,
        bingResponse,
        wikipediaResponse
      ]
      writer.writerow(row)

def readCsv(filepath):
  allrows = []
  with open(filepath) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      allrows.append(row)
    
  return allrows

def runQueryChatGPT(question):
  response = openAIClient.responses.create(
    model = "gpt-5.4-mini",
    instructions = "You are a helpful knowledgeable assistant. Answer as concisely as possible - one or two sentences maximum. Do not give examples",
    input = question
  )
  print(response.output_text)
  return response.output_text

def runQueryGemini(question):
  interaction = geminiClient.interactions.create(
    model = "gemini-3.5-flash",
    input = "You are a helpful knowledgeable assistant. Answer as concisely as possible - one or two sentences maximum. Do not give examples. " + question
  )
  print(interaction.output_text)  
  return interaction.output_text

def runQueryGoogle(question):
  url = "https://www.google.com/search?q=" + quote(question)
  link = fetchBrightDataResponse(url, "parsed")
  return getContents(link)

def runQueryWikipedia(question):
  url = "https://www.google.com/search?q=" + quote(question + " site:wikipedia.org") 
  link = fetchBrightDataResponse(url, "parsed")
  return getContents(link)

def runQueryBing(question):
  url = "https://www.bing.com/search?q=" + quote(question)
  link = fetchBrightDataResponse(url, "parsed_bing")
  return getContents(link)


def fetchBrightDataResponse(url, dataFormat):
  apiUrl = "https://api.brightdata.com/request"
  payload = {
    "zone": "surya_project_",
    "url": url,
    "format": "json",
    "data_format": dataFormat
  }
  headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + brightdataKey
  }
  response = requests.post(
    apiUrl,
    json = payload,
    headers = headers,
  )

  results = response.json()
  body = json.loads(results["body"])
  return body["organic"][0]["link"]


def getContents(link):  
  response = openAIClient.responses.create(
    model = "gpt-5.4-mini",
    instructions = "You are a helpful knowledgeable assistant. Answer as concisely as possible - one or two sentences maximum. Do not give examples. Summarize the following website and only output the main idea instead of a third person voice.",
    input = link
  )

  print(response.output_text)
  return response.output_text



main()
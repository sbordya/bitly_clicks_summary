import requests
import os
import sys
import argparse
from dotenv import load_dotenv

def createParser():
  parser = argparse.ArgumentParser(
    prog='Bitly clicks summary',
    description='''This program gives a bitly link for a url and the summary of clicks for a bitly link''',
    epilog='(c) Serghei Bordea. This program was created as part of education on dvmn.org'
  )
  parser.add_argument('--url', required=True, help='''a url to get bitly link or bitly link to get 
  clicks summary''')

  return parser

def shorten_link(bitly_token, link):
  payload = {'long_url': link}
  headers = {'Authorization': f'Bearer {bitly_token}'}
  url = 'https://api-ssl.bitly.com/v4/bitlinks'
  response = requests.post(url, headers=headers, json=payload)
  response.raise_for_status()
  bitlink = response.json()["id"]
  return bitlink

def count_clicks(bitly_token, bitlink):
  payload = {'unit': 'day'}
  headers = {'Authorization': f'Bearer {bitly_token}'}
  url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
  response = requests.get(url, headers=headers, params=payload)
  response.raise_for_status()
  clicks_count = response.json()["total_clicks"]
  return clicks_count

def main():
  load_dotenv()
  bitly_token = os.getenv("BITLY_TOKEN")
  parser = createParser()
  namespace = parser.parse_args()

  if namespace.url.startswith("bit.ly"):
    bitlink = namespace.url
  else:
    bitlink = shorten_link(bitly_token, namespace.url)
    print("Your bitly link:", bitlink)

  clicks_count = count_clicks(bitly_token, bitlink)
  print(f'The total amount of clicks - {clicks_count}')

if __name__ == "__main__":
  try:
    main()
  except requests.exceptions.HTTPError as e:
    print(e)
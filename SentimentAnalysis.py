# Installing and Importing Baseline Dependencies
from transformers import PegasusTokenizer, PegasusForConditionalGeneration
from bs4 import BeautifulSoup
import requests
import re
import csv
from transformers import pipeline


# Setup the Model
model_name = "human-centered-summarization/financial-summarization-pegasus"
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name)

# Sumarize article
url = "https://finance.yahoo.com/news/3-strong-buy-stocks-too-144947041.html"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
paragraphs = soup.find_all('p')

text = [paragraph.text for paragraph in paragraphs]
words = ' '.join(text).split(' ')[:400]
ARTICLE = ' '.join(words)

input_ids = tokenizer.encode(ARTICLE, return_tensors='tf')
output = tmodel.generate(input_ids, max_length=75, num_beams=7, early_stopping=True)
summary = tokenizer.decode(output[0], skip_special_tokens=True)


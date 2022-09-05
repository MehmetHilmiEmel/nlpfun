from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd
import joblib
import torch
from googletrans import Translator

from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
model = AutoModelForSequenceClassification.from_pretrained("savasy/bert-base-turkish-sentiment-cased")
tokenizer = AutoTokenizer.from_pretrained("savasy/bert-base-turkish-sentiment-cased")
same_pipe= pipeline("sentiment-analysis", tokenizer=tokenizer, model=model)



import torch
from transformers import BertTokenizerFast, EncoderDecoderModel
ckpt = 'mrm8488/bert2bert_shared-turkish-summarization'
same_pipe_token = BertTokenizerFast.from_pretrained(ckpt)
same_pipe_model = EncoderDecoderModel.from_pretrained(ckpt)


from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

same_pipe_token_chat = AutoTokenizer.from_pretrained("facebook/blenderbot-400M-distill")

same_pipe_model_chat = AutoModelForSeq2SeqLM.from_pretrained("facebook/blenderbot-400M-distill")


def generate_summary(text):

   inputs = same_pipe_token([text], padding="max_length", truncation=True, max_length=512, return_tensors="pt")
   input_ids = inputs.input_ids
   attention_mask = inputs.attention_mask
   output = same_pipe_model.generate(input_ids, attention_mask=attention_mask)
   return same_pipe_token.decode(output[0], skip_special_tokens=True)

# Create your views here.
def index(request):
    name="Hilmi"
    return render(request,"index.html",{"name":name})

def counter(request):
    text=request.POST['text']
    number_of_words=len(text.split(" "))
    return render(request,"counter.html",{"text":text,"amount":number_of_words})

def metin_summary(request):

    return render(request,"metin_summary.html")

def metin_summary_sonuc(request):
    text=request.POST['metin']
    text=generate_summary(text)
    return render(request,"metin_summary.html",{"text":text})



def chatbot(request):
  return render(request,"chatbot.html")


def chatbot_sonuc(request):
  translator = Translator()
  text=request.POST['metin']

  translated_en = translator.translate(text, src='tr', dest='en')

  inputs = same_pipe_token_chat([translated_en.text], return_tensors="pt")
  reply_ids = same_pipe_model_chat.generate(**inputs)
  result=same_pipe_token_chat.batch_decode(reply_ids, skip_special_tokens=True)[0]

  translated_tr = translator.translate(result, src='en', dest='tr')
  metin=translated_tr.text
  return render(request,"chatbot.html",{"result":metin})








def sentiment(request):

  return render(request,"sentiment.html")


def sentiment_sonuc(request):
  text=request.POST['metin']
  result=same_pipe(text)

  return render(request,"sentiment.html",{"result":result[0]['label'],"score":(result[0]['score'])*100})

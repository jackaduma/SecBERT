#!python
# -*- coding: utf-8 -*-
# @author: Kun

'''
Author: Kun
Date: 2022-01-21 18:28:21
LastEditTime: 2022-01-21 18:50:56
LastEditors: Kun
Description: 
FilePath: /projects/my_open_projects/SecBERT/lm/eval_fillmask_roberta.py
'''


from transformers import pipeline

fill_mask_google_bert = pipeline(
    "fill-mask",
    model="bert-base-cased",
    tokenizer="bert-base-cased"
)

fill_mask_roberta = pipeline(
    "fill-mask",
    model="roberta-base",
    tokenizer="roberta-base"
)

fill_mask_scibert = pipeline(
    "fill-mask",
    model="allenai/scibert_scivocab_uncased",
    tokenizer="allenai/scibert_scivocab_uncased",
)

fill_mask_secbert = pipeline(
    "fill-mask",
    model="jackaduma/SecBERT",
    tokenizer="jackaduma/SecBERT"
)

fill_mask_secroberta = pipeline(
    "fill-mask",
    model="jackaduma/SecRoBERTa",
    tokenizer="jackaduma/SecRoBERTa"
)


s0 = 'We able find spear phishing e-mail <mask> attackers'
s1 = 'He called the WannaCry attack a reckless attack that caused "havoc and destruction" by locking <mask> information away from users.'  # vital
s2 = 'FireEye, a cybersecurity <mask>.'  # consultancy
s3 = 'The extent of the WannaCry attack prompted questions about what to do in the event of a ransomware <mask>.'  # infection
s4 = 'In spear phishing scheme attackers send <mask> targeted people'  # e-mails
s = s4

print("\n\n"+"Eval the followed sentence: ")
print(s)


print("\n" + "#"*20 + " "*10 + "Google BERT")
result_google_bert = fill_mask_google_bert(s.replace("<mask>", "[MASK]"))
for res in result_google_bert:
    print(res)

# print("\n" + "#"*20 + " "*10 + "RoBERTa")
# result_roberta = fill_mask_roberta(s)
# for res in result_roberta:
#     print(res)

print("\n" + "#"*20 + " "*10 + "SciBERT")
result_scibert = fill_mask_scibert(s.replace("<mask>", "[MASK]"))
for res in result_scibert:
    print(res)

print("\n" + "#"*20 + " "*10 + "Our SecBERT")
result = fill_mask_secbert(s.replace("<mask>", "[MASK]"))
for res in result:
    print(res)

print("\n" + "#"*20 + " "*10 + "Our SecRoBERTa")
result = fill_mask_secroberta(s)
for res in result:
    print(res)

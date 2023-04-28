<!--
 * @Author: Kun
 * @Date: 2020-11-24 22:58:24
 * @LastEditTime: 2023-04-29 06:13:36
 * @LastEditors: Kun
 * @Description: 
 * @FilePath: /my_open_projects/SecBERT/README.zh-CN.md
-->
# <p align=center>**`SecBERT`**</p>

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/jackaduma/SecBERT)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://paypal.me/jackaduma?locale.x=zh_XC)

[**中文说明**](./README.zh-CN.md) | [**English**](./README.md)

`SecBERT` 是一个在网络安全领域的文本上训练得到的 `BERT` 模型，旨在学习网络安全领域的知识。

本项目使用预训练的语言模型BERT（Bidirectional Encoder Representations from Transformers）来处理网络安全领域的文本数据，以提高恶意软件分类的准确性。BERT是一种基于Transformer架构的深度学习模型，可以捕捉句子中的上下文信息，从而更好地理解文本数据。该项目使用BERT作为预训练的语言模型，在其基础上进行微调，以适应网络安全领域的文本分类任务。具体来说，该项目使用了一个名为SecBERT的BERT模型，用于对恶意软件进行分类，其输入数据包括二进制文件和文本文档等。通过对SecBERT模型的微调，该项目取得了在公开数据集上的较好表现，证明了利用预训练的语言模型处理网络安全文本数据的可行性和有效性。

* `SecBERT` 模型在如下的 文章和数据corpus上训练得到：
  
  * [APTnotes](https://github.com/kbandla/APTnotes)
  
  * [Stucco-Data: Cyber security data sources](https://stucco.github.io/data/)  
  
  * [CASIE: Extracting Cybersecurity Event Information from Text](https://ebiquity.umbc.edu/_file_directory_/papers/943.pdf)
  
  * [SemEval-2018 Task 8: Semantic Extraction from CybersecUrity REports using Natural Language Processing (SecureNLP)](https://competitions.codalab.org/competitions/17262). 

* `SecBERT` 有自己的 vocabulary (`secvocab`) ， 适应于训练使用的数据 corpus。 已完成训练的模型有 [SecBERT](https://huggingface.co/jackaduma/SecBERT)  和 [SecRoBERTa](https://huggingface.co/jackaduma/SecRoBERTa) 版本。


## **Table of Contents**


## **下载预训练模型**

SecBERT 模型目前可以直接通过 Huggingface的框架直接安装使用:

```
from transformers import AutoTokenizer, AutoModelForMaskedLM

tokenizer = AutoTokenizer.from_pretrained("jackaduma/SecBERT")

model = AutoModelForMaskedLM.from_pretrained("jackaduma/SecBERT")


tokenizer = AutoTokenizer.from_pretrained("jackaduma/SecRoBERTa")

model = AutoModelForMaskedLM.from_pretrained("jackaduma/SecRoBERTa")

```

------

## **预训练模型权重** 

已发布了预训练模型的 pytorch 版本。  使用 [Hugging Face](https://github.com/huggingface/pytorch-pretrained-BERT) library 创建了pytorch 版本， 在此，本 repo 展示了如何使用。

[Huggingface Modelhub](https://huggingface.co/models)

  * [SecBert](https://huggingface.co/jackaduma/SecBERT)

  * [SecRoBERTa](https://huggingface.co/jackaduma/SecRoBERTa)


### **在你自己的模型中使用 SecBERT**

SecBERT 模型包含了所有必须的文件，和BERT的格式一直，可以在你自己的模型中插入使用。

If you use PyTorch, refer to [Hugging Face's repo](https://github.com/huggingface/pytorch-pretrained-BERT) where detailed instructions on using BERT models are provided. 


## **Fill Mask**

我们旨在建立一个 网络安全领域的文本上的语言模型，可预见的是， 它可以明显提高网络安全领域的文本相关的下游任务 (NER, 文本分类, 语义理解，问答等)。

如下，展示了 Fill-Mask pipeline ，对比 [Google Bert](), [AllenAI SciBert](https://github.com/allenai/scibert) 和 这里训练的 [SecBERT](https://github.com/jackaduma/SecBERT) .

```
cd lm
python eval_fillmask_lm.py
```

<img src="./fill-mask-result.png" width="150%" height="150%">


## **Downstream-tasks** 

### TODO

------
## **Star-History**

![star-history](https://api.star-history.com/svg?repos=jackaduma/SecBERT&type=Date "star-history")

------

## Donation
If this project help you reduce time to develop, you can give me a cup of coffee :) 

AliPay(支付宝)
<div align="center">
	<img src="./misc/ali_pay.png" alt="ali_pay" width="400" />
</div>

WechatPay(微信)
<div align="center">
    <img src="./misc/wechat_pay.png" alt="wechat_pay" width="400" />
</div>

------

## **License**

[MIT](LICENSE) © Kun
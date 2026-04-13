# 📄 Text Summarization Using Hugging Face Transformers

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat&logo=python)
![Hugging Face](https://img.shields.io/badge/HuggingFace-Transformers-yellow?style=flat&logo=huggingface)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-red?style=flat&logo=pytorch)


---

## 📌 Project Overview

This project implements an **abstractive text summarization system** using a pretrained transformer model from the [Hugging Face Transformers](https://huggingface.co/docs/transformers) library. The model is fine-tuned on a custom dataset containing text–summary pairs to generate concise, coherent, and meaningful summaries from longer textual content.

The system leverages state-of-the-art **Sequence-to-Sequence (Seq2Seq)** transformer architecture to deeply understand the semantic context of input text and produce human-like, abstractive summaries — going beyond mere extraction to deliver intelligent summarization.

---

## 🎯 Objectives

- Automatically generate short and meaningful summaries from long-form text
- Fine-tune a pretrained transformer model for domain-specific summarization tasks
- Evaluate summarization quality using industry-standard NLP metrics

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Hugging Face Transformers | Pretrained model and tokenizer |
| PyTorch | Deep learning framework |
| Hugging Face Datasets | Dataset loading and processing |
| Evaluate (ROUGE) | Performance evaluation |
| Pandas & Scikit-learn | Data handling and preprocessing |

---

## 🤖 Model

This project uses the **`facebook/bart-large-cnn`** pretrained model — a Transformer-based Seq2Seq architecture specifically designed and optimized for abstractive text summarization. The model is further fine-tuned on a custom dataset to enhance domain-specific performance.

---

## 📂 Dataset

The dataset consists of paired entries of:

- **Input Text** — Long-form source content
- **Target Summary** — Corresponding concise reference summary

---

## ⚙️ Methodology

The project follows a structured NLP pipeline:

1. **Data Collection & Preprocessing** — Clean and prepare raw text-summary pairs
2. **Dataset Splitting** — Partition into training, validation, and test sets
3. **Model & Tokenizer Loading** — Load `facebook/bart-large-cnn` from Hugging Face Hub
4. **Tokenization** — Encode input texts and target summaries
5. **Fine-Tuning** — Train the model on the custom dataset
6. **Evaluation** — Assess performance using ROUGE metrics
7. **Model Saving** — Persist the fine-tuned model for reuse
8. **Inference** — Generate summaries for new, unseen input text

---

## 🚀 Key Features

- ✅ Pretrained transformer model for high-quality abstractive summarization
- ✅ Custom dataset fine-tuning support
- ✅ Generates human-like, coherent summaries
- ✅ Modular and extensible codebase
- ✅ Ready for integration into web applications or NLP pipelines

---

## 📁 Project Structure

<img width="626" height="686" alt="image" src="https://github.com/user-attachments/assets/14b52d24-df7a-4dff-bc57-5190d3652f9d" />


---

## 📌 Sample Output

**Input Text:**
> *"Artificial Intelligence is rapidly transforming industries by enabling automation, improving decision-making, and analyzing large datasets efficiently."*

**Generated Summary:**
> *"Artificial Intelligence is transforming industries through automation and data analysis."*

---

## 🔮 Future Improvements

- [ ] Train on larger, more diverse datasets for improved generalization
- [ ] Experiment with advanced architectures such as **PEGASUS** and **FLAN-T5**
- [ ] Deploy the model as a **REST API** or interactive web application
- [ ] Extend support for **multilingual summarization**

---

## 📚 Conclusion

This project demonstrates how pretrained Seq2Seq transformer models can be effectively fine-tuned to perform domain-specific text summarization. By combining the power of the Hugging Face ecosystem with a structured fine-tuning pipeline, the system successfully produces concise, meaningful summaries — showcasing the capabilities of modern Natural Language Processing techniques.

---

## 👨‍💻 Author

**Madhava Reddy Yanamala**

---

> ⭐ If you found this project helpful, consider giving it a star on GitHub!

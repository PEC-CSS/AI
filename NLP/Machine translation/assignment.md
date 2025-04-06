# 🌍 Beginner Assignment: Try Machine Translation with Transformers

Welcome to your first assignment on **Machine Translation (MT)**!  
You’ll explore how AI models translate text from English to French using a small dataset and a ready-made model.

---

## 🧾 Sample Dataset

We’ll use these 6 sentence pairs (English → French):

| English                    | French                       |
|----------------------------|------------------------------|
| I love learning languages. | J'aime apprendre les langues. |
| Where is the nearest bank? | Où est la banque la plus proche ? |
| I need a doctor.           | J'ai besoin d'un médecin.    |
| Can you help me?           | Pouvez-vous m'aider ?        |
| The weather is nice today. | Il fait beau aujourd'hui.    |
| I am hungry.               | J'ai faim.                   |

---

## 🛠️ Task: Translate Using a Pretrained Model

We’ll use **M2M100 by Meta** via Hugging Face.  
It supports direct translation between many languages.

### 🔹 Install Required Library
```bash
pip install transformers sentencepiece
```

### 🔹 Python Code to Translate English → French
```python
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

# Load model and tokenizer
model = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_418M")
tokenizer = M2M100Tokenizer.from_pretrained("facebook/m2m100_418M")

# Translate sentences
sentences = [
    "I love learning languages.",
    "Where is the nearest bank?",
    "I need a doctor.",
    "Can you help me?",
    "The weather is nice today.",
    "I am hungry."
]

tokenizer.src_lang = "en"
for sentence in sentences:
    encoded = tokenizer(sentence, return_tensors="pt")
    generated_tokens = model.generate(
        **encoded,
        forced_bos_token_id=tokenizer.get_lang_id("fr")
    )
    output = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
    print(f"{sentence} → {output}")
```

---

## 📊 Optional Task: Try BLEU Score

You can compare the model’s translation with the original French using BLEU score.

### 🔹 Sample Code
```python
from nltk.translate.bleu_score import sentence_bleu

# Reference and candidate
reference = [["J'aime", "apprendre", "les", "langues", "."]]
candidate = ["J'adore", "apprendre", "les", "langues", "."]

score = sentence_bleu(reference, candidate)
print("BLEU Score:", score)
```

Try BLEU score for a couple of sentences just for fun 😊

---

## 💭 Reflection Questions

Answer these in your notebook or just think about them:

1. Which translation looked the best to you?
2. Did the model make any mistakes or awkward translations?
3. Was the translation grammar correct and natural?
4. How do you think this kind of model works?
5. Where do you think machine translation is most useful in real life?

---

## 🎁 Bonus (Optional)

Try translating these extra sentences:
- “I am going to school.”
- “Do you speak English?”

---

Enjoy translating! 🌐✨  
This is your first step toward understanding how AI understands languages.

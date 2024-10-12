def summarize(text, model, tokenizer, length_multiplier=0.1):
    tokens = len(tokenizer.tokenize(text))
    max_length = int(tokens * length_multiplier)  # Adjust summary length based on document size
    inputs = tokenizer(text, truncation=True, padding='longest', return_tensors="pt")
    summary_ids = model.generate(inputs['input_ids'],min_length=round(max_length*0.025), max_length=round(max_length*0.1), num_beams=5, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary


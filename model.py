from transformers import PegasusTokenizer, PegasusForConditionalGeneration

def textsum_model():
    tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")
    model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")
    return model, tokenizer

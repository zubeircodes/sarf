from transformers import LlamaForCausalLM, LlamaTokenizer

# Load the model and tokenizer
model_name = "meta-llama/llama-2-7b"  # Change to appropriate model version (e.g., 13B or 7B)
model = LlamaForCausalLM.from_pretrained(model_name)
tokenizer = LlamaTokenizer.from_pretrained(model_name)

# Function to ask Llama 2 for the root of a given Arabic word
def get_arabic_root(word):
    prompt = f"Extract the root of the Arabic word: {word}"

    # Tokenize input and generate output
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs['input_ids'], max_length=50, num_return_sequences=1)

    # Decode and print the result
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return result

# Test with an Arabic word
arabic_word = "مكتوب"
root = get_arabic_root(arabic_word)
print(f"The root of '{arabic_word}' is: {root}")

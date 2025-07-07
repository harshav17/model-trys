import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell(disabled=True)
def _():
    from transformers import AutoModelForCausalLM, AutoTokenizer

    model_name = "mistralai/Mistral-7B-v0.1"
    model = AutoModelForCausalLM.from_pretrained(
        model_name, torch_dtype="auto", device_map="auto"
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return model, tokenizer


@app.cell(disabled=True)
def _(model, tokenizer):
    prompt = "Once there was a dog named"
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    return (inputs,)


@app.cell(disabled=True)
def _(inputs, model, tokenizer):
    output = model.generate(**inputs, max_new_tokens=10)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    print(generated_text)
    return


if __name__ == "__main__":
    app.run()

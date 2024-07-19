from transformers import AutoModelForCausalLM, AutoTokenizer

class TextImprover:
    def __init__(self, model_name="gpt2"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)


    def improve_text(self, text):
        if not text:
            return "Texto vacío no puede ser mejorado."

        try:
            inputs = self.tokenizer(text, return_tensors="pt")
            outputs = self.model.generate(inputs.input_ids, max_length=800, num_return_sequences=1)
            improved_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            return improved_text
        except Exception as e:
            return f"Error al mejorar el texto: {str(e)}"


class GptService:
    def __init__(self, text_improver):
        self.text_improver = text_improver

    def improve_wikipedia_text(self, text):
        return self.text_improver.improve_text(text)


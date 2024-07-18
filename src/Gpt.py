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
            outputs = self.model.generate(inputs.input_ids, max_length=512, num_return_sequences=1)
            improved_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            return improved_text
        except Exception as e:
            return f"Error al mejorar el texto: {str(e)}"


class GptService:
    def __init__(self, text_improver):
        self.text_improver = text_improver

    def improve_wikipedia_text(self, text):
        return self.text_improver.improve_text(text)

# Ejemplo de uso
if __name__ == "__main__":
    content_enrichment = ContentEnrichment()

    while True:
        sample_text = input("Ingrese un texto para mejorar (o 'salir' para terminar): ")
        if sample_text.lower() == 'salir':
            break
        improved_text = content_enrichment.improve_text(sample_text)
        print("Texto mejorado:", improved_text)
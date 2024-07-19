# eso es el incio no hace falta importar nada mas
from src.Content_enrichment import Content_enrichment
def main():
    app = Content_enrichment()
    app.run()

main()


"""from .src.Gpt import GptService, TextImprover
def main():
    ti = TextImprover
    gpt = GptService(textimprover=ti)

    while True:
        i = input('Write some text or quit to exit')

        if i == 'quit':
            return

        result = gpt.textimprover(i)
        print(result)

if name == '__main':
    main()"""


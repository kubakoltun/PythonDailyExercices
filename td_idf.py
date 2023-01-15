import math


text = '''he really really loves coffee
my sister dislikes coffee
my sister loves tea'''


def main(text):
    docs = [line.split() for line in text.splitlines()]

    N = len(docs)

    vocabulary = list(set(text.split()))

    df = {}
    tf = {}
    for word in vocabulary:
        tf[word] = [doc.count(word) / len(doc) for doc in docs]

        df[word] = sum([word in doc for doc in docs]) / N

    for doc_index, doc in enumerate(docs):
        tfidf = []
        for word in vocabulary:
            x = tf[word][doc_index]
            y = df[word]

            tfidf.append(x * math.log(1 / y, 10))

            x = 0
        print(tfidf)

main(text)

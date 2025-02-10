from pypdf import PdfReader

class PDFRag:
    def __init__(self, url, collection):
        self.url = url
        self.collection = collection

    def load(self):
        reader = PdfReader(self.url)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        self.collection.add(
            documents=[text],
            ids=["pdf_1"]
        )
    def retrieve(self, query):
        results = self.collection.query(
            query_texts=query,
            n_results=3  # 检索前 3 个最相关的文档
        )
        # 提取检索到的文档
        documents = results['documents'][0]
        return documents
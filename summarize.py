import os
from langchain_community.chat_models import ChatOpenAI
from langchain.docstore.document import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain


from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')


class Summmarization:
    def __init__(self, model_name="gpt-4o-mini", temperature=0.3):
        self.llm = ChatOpenAI(model_name=model_name, temperature=temperature)

    def summarize_text(self, text: str):
        try:
            docs = [Document(page_content=text)]

            prompt = ChatPromptTemplate.from_messages(
                [("system", "Write a concise summary of the following:\\n\\n{context}")]
            )

            # Instantiate chain
            chain = create_stuff_documents_chain(self.llm, prompt)

            # Invoke chain
            result = chain.invoke({"context": docs})

            return result

        except Exception as e:
            return f"Error generating summary: {str(e)}"

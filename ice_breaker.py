import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from third_parties.linkedin import scrap_linkedin_profile


if __name__ == '__main__':
    print("Hello LangChain!")

    summary_template = """
        given the linkedin information {information} about a person, I want you to create:
        1. A summary of the person's profile
        2. Two interesting facts about the person
    """

    summary_prompt_template = PromptTemplate(input_variables="information", template=summary_template)

    llm = ChatOllama(model='gemma2')
    linkedin_data = scrap_linkedin_profile(linkedin_profile_url="www.linkedin.com/in/oludare-adekunle", mock=False)
    chain = summary_prompt_template | llm | StrOutputParser()
    response = chain.invoke(input={"information": linkedin_data})

    print(response)


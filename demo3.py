from langchain.chat_models import init_chat_model
# Import message types for structuring conversations
from langchain_core.messages import HumanMessage, SystemMessage
from typing import Optional
from pydantic import BaseModel, Field

#initialize a gpt-4o-mini model from OpenAI
model = init_chat_model("gpt-4o-mini", model_provider="openai", temperature=0)

class PublicCompanyInfo(BaseModel):
    """Detailed info about a public company"""
    name: str = Field(description="name of the company")
    tickerSymbol: str = Field(description="The tiker symbol of the company on NYSE")
    marketCap: float = Field(description="the current market cap of the company")

structured_llm = model.with_structured_output(PublicCompanyInfo)
response = structured_llm.invoke("Give me all info about Lyft")
print(response)
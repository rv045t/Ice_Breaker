from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List


class PersonIntel(BaseModel):
    summary: str = Field(description="Summary of the person")
    facts: List[str] = Field(description="Interesting facts about the Person")
    topics_of_interests: List[str] = Field(
        description="Topics that may interest the Person"
    )
    ice_breakers: List[str] = Field(
        description="Create icebreakers to open a conversation with the Person"
    )

    def to_dict(self):
        return {
            "summary": self.summary,
            "facts": self.facts,
            "topic_of_interests": self.topics_of_interests,
            "ice_breakers": self.ice_breakers,
        }


person_intel_parser: PydanticOutputParser = PydanticOutputParser(
    pydantic_object=PersonIntel
)

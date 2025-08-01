# graph_logic.py
import os
from dotenv import load_dotenv
from typing import TypedDict, Annotated, List
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph, END

# Load API key
load_dotenv()

# Define the state for our graph
class InterviewState(TypedDict):
    job_description: str
    interview_history: List[dict]
    current_question: str
    user_answer: str
    feedback: str
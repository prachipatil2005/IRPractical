from transformers import pipeline

# Load the summarization pipeline
qa_pipeline = pipeline("question-answering",model="deepset/roberta-base-squad2")

# Define the Context and the Question
context = """
Hugging Face is a technology company based in New York and Paris. It is known for its open-source library called Transformers,
which provides state-of-the-art machine learning models for natural language processing tasks.
"""

question = "What is Hugging Face known for?"

# Get the Answer
result = qa_pipeline(question=question,context=context)

# Print the Answer
print(f"Question : {question}")
print(f"Answer : {result['answer']}")
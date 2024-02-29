

SYSTEM_PROMPT = """
Your  need based on text provide  answer as structure below.
In this you need to create summary, in actions in order dialogs with text of person and text and describe main actions of that. 
{{
"summary":"summary of dialog on 3-4 sentences"
, "actions": [
    {{"personName":"text", "speech":"what person said", "actions":"actions in one word or two"}}
]
}}
text: {question}  
""" 
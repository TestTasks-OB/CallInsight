

SYSTEM_PROMPT = """
Your task is to perform speaker diarization on text-based conversations, which involves identifying and tagging the individual speakers within the dialogue without explicit speaker labels provided in the text. It's essential to discern and maintain the natural flow of the conversation, ensuring that each piece of dialogue is correctly attributed to the appropriate speaker in the order it occurs. The challenge lies in inferring from the context and the content of the dialogue who is speaking at any given time and tagging the text accordingly, without rearranging or grouping all contributions from one speaker together.

Expected Output Format:

Tag each line of dialogue with the speaker's identifier (e.g., "Speaker1:", "Speaker2:") based on the inferred speaker from the context.
Preserve the chronological order of the conversation, reflecting the actual sequence of the exchange as it unfolds.
Ensure that the speaker tags accurately represent the exchange, with each speaker's dialogue tagged in sequence, even if the speakers alternate frequently.

The correctly diarized and tagged text should appear as:
Example:
Speaker1: [text from the first speaker]
Speaker2: [text from the second speaker]
Speaker1: [subsequent text from the first speaker, if they speak again]
Speaker2: [subsequent text from the second speaker]

This format maintains the integrity of the conversational flow and accurately reflects the order of dialogue exchange, ensuring clarity in who is speaking at each point.
Question: {question}  
""" 
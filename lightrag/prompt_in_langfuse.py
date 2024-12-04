from langfuse import Langfuse

langfuse = Langfuse()

def get_latest_prompt(prompt_name):
    return langfuse.get_prompt(prompt_name, label="latest").prompt

GRAPH_FIELD_SEP = "<SEP>"

PROMPTS = {
    "DEFAULT_LANGUAGE": "English",
    "DEFAULT_TUPLE_DELIMITER": "<|>",
    "DEFAULT_RECORD_DELIMITER": "##",
    "DEFAULT_COMPLETION_DELIMITER": "<|COMPLETE|>",
    "process_tickers": ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"],
    "DEFAULT_ENTITY_TYPES": [get_latest_prompt(f"DEFAULT_ENTITY_TYPES_{i}") for i in range(4)],
    "entity_extraction": get_latest_prompt("entity_extraction"),
    "entity_extraction_examples": [get_latest_prompt(f"entity_extraction_examples_{i}") for i in range(3)],
    "summarize_entity_descriptions": get_latest_prompt("summarize_entity_descriptions"),
    "entiti_continue_extraction": get_latest_prompt("entiti_continue_extraction"),
    "entiti_if_loop_extraction": get_latest_prompt("entiti_if_loop_extraction"),
    "fail_response": get_latest_prompt("fail_response"),
    "rag_response": get_latest_prompt("rag_response"),
    "keywords_extraction": get_latest_prompt("keywords_extraction"),
    "keywords_extraction_examples": [get_latest_prompt(f"keywords_extraction_examples_{i}") for i in range(3)],
    "naive_rag_response": get_latest_prompt("naive_rag_response")
}

if __name__ == '__main__':
    prompt = get_latest_prompt("naive_rag_response")
    print(prompt)

from langfuse import Langfuse

langfuse = Langfuse()

GRAPH_FIELD_SEP = "<SEP>"

PROMPTS = {}

PROMPTS["DEFAULT_LANGUAGE"] = "English"
PROMPTS["DEFAULT_TUPLE_DELIMITER"] = "<|>"
PROMPTS["DEFAULT_RECORD_DELIMITER"] = "##"
PROMPTS["DEFAULT_COMPLETION_DELIMITER"] = "<|COMPLETE|>"
PROMPTS["process_tickers"] = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]

PROMPTS["DEFAULT_ENTITY_TYPES"] = [langfuse.get_prompt(f"DEFAULT_ENTITY_TYPES_{i}") for i in range(0, 4)]

PROMPTS["entity_extraction"] = langfuse.get_prompt("entity_extraction")

PROMPTS["entity_extraction_examples"] = [langfuse.get_prompt(f"entity_extraction_examples_{i}") for i in range(0, 3)]

PROMPTS[
    "summarize_entity_descriptions"
] = langfuse.get_prompt("summarize_entity_descriptions")

PROMPTS[
    "entiti_continue_extraction"
] = langfuse.get_prompt("entiti_continue_extraction")

PROMPTS[
    "entiti_if_loop_extraction"
] = langfuse.get_prompt("entiti_if_loop_extraction")

PROMPTS["fail_response"] = langfuse.get_prompt("fail_response")

PROMPTS["rag_response"] = langfuse.get_prompt("rag_response")

PROMPTS["keywords_extraction"] = langfuse.get_prompt("keywords_extraction")

PROMPTS["keywords_extraction_examples"] = [langfuse.get_prompt(f"keywords_extraction_examples_{i}") for i in
                                           range(0, 3)]
PROMPTS["naive_rag_response"] = langfuse.get_prompt("naive_rag_response")

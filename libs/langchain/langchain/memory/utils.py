from typing import Any, Dict, List


def get_prompt_input_key(inputs: Dict[str, Any], memory_variables: List[str]) -> str:
    """
    Get the prompt input key.

    Args:
        inputs: Dict[str, Any]
        memory_variables: List[str]

    Returns:
        A prompt input key.
    """

    prompt_input_keys = None
    for key in inputs:
        if key not in memory_variables and key != "stop":
            if prompt_input_keys is not None:
                raise ValueError("One input key expected, got multiple")
            prompt_input_keys = key

    if prompt_input_keys is None:
        raise ValueError("One input key expected, got None")

    return prompt_input_keys

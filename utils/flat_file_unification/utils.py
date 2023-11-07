import random
import jinja2
import openai
from openai.error import RateLimitError
import time
from typing import List, Dict

def wrap_umsg(msg: str) -> dict[str, str]:
    return {"role": "user", "content": msg}


def wrap_sys_msg(msg: str) -> dict[str, str]:
    return {"role": "system", "content": msg}


def wrap_amsg(msg: str) -> dict[str, str]:
    return {"role": "assistant", "content": msg}

def assemble_system_chat_message(context: str, files: list[str]) -> list[dict[str, str]]:
    return wrap_sys_msg(system_chat_message_template.render(context=context, files=files))

system_chat_message_template = jinja2.Template(
    """You are a staff data scientist named dubo. You help your company to unify flat files.
    The context of the files you want to merge is: {{ context }}.
    The list of files you want to merge is:
    {% for file in files %}
    {{ file }}
    {% endfor %}
    User will send you sample lines from some files for you to get a common schema for the files.
    Once user agrees with the schema, you will write Python code to merge the files.
"""
)

def grab_response_from_chatgpt_sync(
    messages: List[Dict[str, str]],
    model: str = "gpt-4",
    max_retries: int = 3,
    delay_between_retries: int = 1,
    temperature: float = 0.0,
    frequency_penalty: float = 0.0,
) -> str:
    """Grab a response from the OpenAI chat API synchronously.
    Args:
        messages: The messages to send to the API.
        model: The model to use.
        max_retries: Maximum number of retries if the API returns an error.
        delay_between_retries: Time to wait in seconds before each retry.
    """
    print("Sending messages to OpenAI's API...")
    print(messages[-2:])
    for retry_count in range(max_retries + 1):
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                temperature=temperature,
                frequency_penalty=frequency_penalty,
            )
            if getattr(response, "choices", None):
                query_response = response["choices"][0]["message"]["content"]  # type: ignore
                return query_response.strip()
            raise ValueError("No response")
        except RateLimitError:
            if retry_count < max_retries:
                time.sleep(delay_between_retries)
        except openai.OpenAIError as e:
            print(f"OpenAIError on attempt {retry_count + 1}: {e}")
            if retry_count < max_retries and (
                "Server error" in str(e) or "Bad gateway" in str(e)
            ):
                time.sleep(delay_between_retries)
            else:
                raise e
    raise ValueError("No response")

def get_sample_lines_from_file(file_path: str, leading_lines_num: int = 10, trailing_lines_num: int = 5, random_lines_num: int = 5) -> str:
    """
    Get a sample of lines from the file.
    """
    with open(file_path) as f:
        lines = f.readlines()
        # get the number of lines in the file
        lines_num = len(lines)
        # if the file has less than total sample lines, just return the whole file
        if lines_num < leading_lines_num + trailing_lines_num + random_lines_num:
            return "\n".join(lines)
        # get the leading lines
        leading_lines = lines[0:leading_lines_num]
        # get the trailing lines
        trailing_lines = lines[lines_num-trailing_lines_num:lines_num]
        # get the random lines
        random_lines = random.sample(lines[leading_lines_num:-trailing_lines_num], random_lines_num)
        # combine all lines
        sample_lines = leading_lines + random_lines + trailing_lines
        # convert to string
        sample_lines = "\n".join(sample_lines)
        return sample_lines


if __name__ == "__main__":
    sample_lines = get_sample_lines_from_file("data/hospital_price_transparency_010034_Community_Hospital_Machine_Readable_Standard_Charges_12_2020.csv")
    print(sample_lines)
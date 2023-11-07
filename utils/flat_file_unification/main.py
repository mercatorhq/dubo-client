import random
import typer
import subprocess
# from PyInquirer import prompt
from rich import print as rprint
from rich.prompt import Prompt
import os
import openai
import json

from utils import get_sample_lines_from_file, assemble_system_chat_message, wrap_amsg, wrap_umsg, grab_response_from_chatgpt_sync

app = typer.Typer()


@app.command("merge")
def merge_func():
    rprint("[green bold]==============================================[/green bold]")
    rprint("[green bold]Hello! Welcome to the merge tool![/green bold]")
    rprint("[green bold]==============================================[/green bold]")
    rprint("[yellow]Please enter the context of the files you want to merge, this will help us to better understand the files.[/yellow]")
    context_satisfied = False
    while not context_satisfied:
        context = Prompt.ask("[yellow]Context[/yellow]")
        rprint("You have entered: [green bold]" + context + "[/green bold]")
        context_satisfied = typer.confirm("Is this correct?")

    rprint("[yellow]Please enter the path to a file that contains the list of files you want to merge. Please make sure that the files are in the same directory as the file containing the list.[/yellow]")
    file_list_satisfied = False
    while not file_list_satisfied:
        file_list_valid = True
        path_to_file_list = typer.prompt("File list")
        rprint("You have entered: [green bold]" + path_to_file_list + "[/green bold]")
        # Check if file exists and print the content
        if os.path.isfile(path_to_file_list):
            with open(path_to_file_list) as f:
                rprint("[yellow]The list of files you want to merge is:[/yellow]")
                files = f.readlines()
                # trim whitespace
                files = [x.strip() for x in files]
                for file in files:
                    if os.path.isfile(file):
                        rprint(file)
                    else:
                        rprint("[red bold] " + file + " does not exist![/red bold]")
                        file_list_valid = False
                        continue
        else:
            rprint("[red bold]File does not exist! Please re-enter![/red bold]")
            file_list_valid = False
            continue
        if file_list_valid:
            file_list_satisfied = typer.confirm("Do you want to proceed?")
        else:
            file_list_satisfied = False
            rprint("Please re-enter the path to the file that contains the list of files you'd like to merge.")

    # construct helper dict to store info about the files
    files_info = {}
    class FileInfo:
        def __init__(self, sampled: bool = False, sample_lines: str = "", code: str = "", code_path: str = ""):
            self.sampled = sampled
            self.sample_lines = sample_lines
    for file in files:
        files_info[file] = FileInfo()

    # prompt user for the API key to use for calling OpenAI's API, this should be secret
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        rprint("[yellow]Please enter your OpenAI API key.[/yellow]")
        api_key_satisfied = False
        while not api_key_satisfied:
            api_key = Prompt.ask("[yellow]OpenAI API key[/yellow]", password=True)
            if len(api_key) < 20:
                rprint("[red bold]The API key is too short![/red bold]")
                continue
            api_key_masked = api_key[0:3] + "*" * (len(api_key)-6) + api_key[-3:]
            rprint("You have entered: [green bold]" + api_key_masked + "[/green bold]")
            api_key_satisfied = typer.confirm("Is this correct?")
    openai.api_key = api_key

    # Start the merge process
    # [STEP 1] Get the common schema of the files by randomly picking 3 files from the list,
    # sending the leading 10 lines + random 5 lines in the middle + trailing 10 lines from each
    # file to dubo, and try to generate a common schema.
    rprint("[yellow]Generating a common schema for the files...[/yellow]")
    # randomly pick 3 files or less if there are less than 3 files
    num_files_to_sample = min(len(files), 3)
    files_to_sample = random.sample(files, num_files_to_sample)
    # get the sample lines from each file
    for file in files_to_sample:
        files_info[file].sampled = True # mark the file as sampled
        files_info[file].sample_lines = get_sample_lines_from_file(file)
        rprint("[yellow]Sample lines from " + file + "[/yellow]")
        # rprint(files_info[file].sample_lines)
    
    system_prompt = assemble_system_chat_message(context, files_to_sample)
    # rprint(system_prompt)

    # assemble a user message that contains the sample lines from the files and instructions
    user_message_provide_sample = f"Below are the sample lines from {num_files_to_sample} files.\n\n"
    for file in files_to_sample:
        user_message_provide_sample += f"Sample lines from {file}:\n"
        user_message_provide_sample += "```\n" + files_info[file].sample_lines + "\n```\n"
        user_message_provide_sample += "\n"
    user_message_provide_sample += "Please combine them into one common schema.\n"
    user_message_provide_sample += "Your response shoule be in the form of a JSON object.\n"
    user_message_provide_sample += "The common schema should be in 'schema' field, which is a comma delimited list of column names. Any reasons and explainations should be in 'reason' field.\n"
    user_message_provide_sample += "Do not wrap your response in backticks '```'.\n"
    user_message_provide_sample = wrap_umsg(user_message_provide_sample)
    # rprint(user_message_provide_sample)

    chat_messages = [system_prompt, user_message_provide_sample] # the chat messages to send to OpenAI's API
    last_gpt_response = "" # the last response from OpenAI's API
    last_user_feedback = "" # the last user feedback
    common_schema = "" # the common schema
    try:
        schema_satified = False
        while not schema_satified:
            if last_gpt_response and last_user_feedback:
                chat_messages.append(wrap_amsg(last_gpt_response))
                chat_messages.append(wrap_umsg(last_user_feedback))
            # model = "gpt-3.5-turbo-16k"
            model = "gpt-4"
            response = last_gpt_response = grab_response_from_chatgpt_sync(messages=chat_messages, model=model)
            output_content = json.loads(response)
            rprint("[yellow]The common schema is:[/yellow]")
            rprint(output_content["schema"])
            rprint("[yellow]The reason is:[/yellow]")
            rprint(output_content["reason"])
            
            # Ask the user if the schema is appropriate. If not, incorporate the user's feedback and try to generate a new schema.
            schema_satified = typer.confirm("Do you want to proceed merging with this schema?")
            if schema_satified:
                rprint("[green bold]Great! Let's proceed![/green bold]")
                common_schema = output_content["schema"]
                break
            last_user_feedback = Prompt.ask("[yellow]Please write your feedback[/yellow]")
    except Exception as e:
        rprint("[red bold]Error in generating the common schema![/red bold]")
        rprint(e)
        raise typer.Exit(1)

    # [STEP 2] Ask GPT to generate Python function(s) that will map all files to that schema
    chat_messages.append(wrap_amsg(last_gpt_response)) # add the accepted schema to the chat messages
    # assemble a user message that contains the common schema and instructions for generating the mapping function
    user_message_generate_mapping_instructions = f"""
Below is the common schema we both agreed on:
```
{common_schema}
```
I will work with you to generate a Python script that will map all files to that common schema. You may use the following Python libraries:
- pandas
- numpy
- json
- csv
Make sure that the script is executable and can be run in a Linux environment.
Make sure that the script is idempotent, i.e. running the script multiple times will not change the result.
Make sure that the script is efficient, i.e. it can handle large files.
Make sure that the script can handle all files you have samples from.
Make sure that the script can run without any user input, you may hardcode the file paths.
The script should write the output to a file named 'output.csv' in the same directory as the script.
I will send you sample lines from the rest of the files for you to test and improve your script.
Do not apologize or explain anything.
Return only the Python code.
Do not wrap your response in backticks '```'.
"""
    user_message_generate_mapping_instructions = wrap_umsg(user_message_generate_mapping_instructions)
    chat_messages.append(user_message_generate_mapping_instructions)
    
    try:
        last_gpt_response = "" # the last response from OpenAI's API
        last_user_feedback = "" # the last user feedback
        exception_in_script = "" # the exception in the script
        script = ""
        script_satisfied = False
        script_validity_try_count = 0
        script_validity_max_try_count = 3

        while not script_satisfied and script_validity_try_count < script_validity_max_try_count:
            if last_gpt_response and last_user_feedback:
                chat_messages.append(wrap_amsg(last_gpt_response))
                # check if output.csv exists. if so, send sample lines from it to GPT
                if os.path.isfile("output.csv"):
                    output_samples = get_sample_lines_from_file("output.csv")
                user_message = f"""
{last_user_feedback}
Here are the sample lines from output.csv created by the last Python code execution, please use them to improve the script:
```
{output_samples}
```
Pay attention to the schema of the output, make sure that it matches the common schema.
Do not apologize or explain anything. Return only the Python code. Do not wrap your response in backticks '```'.
"""
                chat_messages.append(wrap_umsg(user_message))
            elif last_gpt_response and exception_in_script:
                chat_messages.append(wrap_amsg(last_gpt_response))
                chat_messages.append(wrap_umsg(exception_in_script + "\n Do not apologize or explain anything. Return only the Python code. Do not wrap your response in backticks '```'."))
            # reset
            last_gpt_response = ""
            last_user_feedback = ""
            exception_in_script = ""

            # model = "gpt-3.5-turbo-16k"
            model = "gpt-4"
            response = last_gpt_response = grab_response_from_chatgpt_sync(messages=chat_messages, model=model)
            script = response
            # GPT keeps wrapping the response in ```...```, so we need to remove them if they exist
            if script.startswith("```python") and script.endswith("```"):
                script = script[10:-3]
            elif script.startswith("```") and script.endswith("```"):
                script = script[3:-3]

            rprint("[yellow]The script is:[/yellow]")
            rprint(script)
            
            try:
                rprint("[yellow]Trying to execute the script...[/yellow]")
                exec(script)
                exception_in_script = ""
                rprint("[green bold]The script is executable! Please find the result in output.csv.[/green bold]")
                script_validity_try_count = 0
            except Exception as e:
                rprint(f"[red bold]The script is not executable! Collecting the exception and sending to GPT for revise...[/red bold]")
                exception_in_script = str(e)
                rprint(exception_in_script)
                script_validity_try_count += 1
                continue

            # Need to feed the rest of files that haven't been sampled to GPT and update the script if necessary
            script_satisfied = typer.confirm(f"Are you satisfied with the script? {'' if len(files) == len(files_to_sample) else (str(len(files) - len(files_to_sample)) + ' files have not been sampled yet. If you are not satisfied, write your feedback or send the sample lines from one of those files and ask GPT to revise the script.')}")
            if not script_satisfied and len(files) == len(files_to_sample):
                # ask user to write feedback
                last_user_feedback = Prompt.ask("[yellow]Please write your feedback[/yellow]")
            elif not script_satisfied and len(files) > len(files_to_sample):
                last_user_feedback = Prompt.ask("[yellow]Please write your feedback or leave empty to send sample lines from unsampled files.[/yellow]")
                if not last_user_feedback:
                    # pick 1 file from the rest of files
                    file_to_sample = random.choice(list(set(files) - set(files_to_sample)))
                    files_to_sample.append(file_to_sample)
                    files_info[file_to_sample].sampled = True
                    files_info[file_to_sample].sample_lines = get_sample_lines_from_file(file_to_sample)
                    last_user_feedback = f"""
Here are the sample lines from {file_to_sample}, please use them to improve the script:
```
{files_info[file_to_sample].sample_lines}
```
Make sure that the revised script can handle all files you have samples from.
Return only the Python code, do not wrap your response in backticks '```'.
"""
        if script_validity_try_count >= script_validity_max_try_count and not script_satisfied:
            rprint("[red bold]The script is not executable after multiple tries! Please try again later.[/red bold]")
            script_path = "script.py"
            with open(script_path, "w") as f:
                f.write(script)
            raise typer.Exit(1)
    except Exception as e:
        rprint("[red bold]Error in generating the script![/red bold]")
        rprint(e)
        raise typer.Exit(1)


    # [STEP 3] Save the script to a file for future reference
    script_path = "script.py"
    with open(script_path, "w") as f:
        f.write(script)
    rprint("[green bold]==============================================[/green bold]")
    rprint("[green bold]Merging completed. Script used is saved as script.py. Final result is saved as output.csv. Bye![/green bold]")
    rprint("[green bold]==============================================[/green bold]")

if __name__ == "__main__":
    app() 
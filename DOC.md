# Dubo SDK

* [ask\_dubo](#ask_dubo)
  * [ask](#ask_dubo.ask)
  * [dispatch\_query](#ask_dubo.dispatch_query)
  * [retrieve\_result](#ask_dubo.retrieve_result)
  * [dispatch\_and\_retrieve](#ask_dubo.dispatch_and_retrieve)
  * [delete\_doc](#ask_dubo.delete_doc)

<a id="ask_dubo.ask"></a>

## ask

```python
def ask(
    query: str,
    data: List[pd.DataFrame] | pd.DataFrame,
    verbose: bool = True,
    rtype: Type = pd.DataFrame,
    column_descriptions: Optional[Dict[str,
                                       str]] = None) -> pd.DataFrame | List
```

Ask Dubo a question about your data.

**Arguments**:

- `query` (`str`): The question to ask Dubo.
- `data`: The DataFrame to ask Dubo about.
- `verbose`: Whether to print the query that Dubo is running.
- `rtype` (`pd.DataFrame or list`): Expected returned type.
- `column_descriptions`: A dictionary of column names to descriptions.

**Returns**:

The result of the query.
##### Example
```python
import pandas as pd
from dubo import ask

data = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
ask('What is the sum of a?', data, rtype=list)
> [(6,)]
```

<a id="ask_dubo.dispatch_query"></a>

## dispatch\_query

```python
def dispatch_query(query: str, fast: bool = False) -> str
```

Dispatch the query and get a tracking_id.

<a id="ask_dubo.retrieve_result"></a>

## retrieve\_result

```python
def retrieve_result(tracking_id: str) -> DataResult
```

Poll for the result using the provided tracking_id.

<a id="ask_dubo.dispatch_and_retrieve"></a>

## dispatch\_and\_retrieve

```python
def dispatch_and_retrieve(query: str, fast: bool = False) -> DataResult
```

Convenience function to generate the query and retrieve the result.

<a id="ask_dubo.delete_doc"></a>

## delete\_doc

```python
def delete_doc(data_source_documentation_id: str) -> bool
```

Delete a document by its ID.

**Arguments**:

- `documentation_id` _str_ - The ID of the document to delete.
  

**Returns**:

- `bool` - True if the deletion was successful, False otherwise.


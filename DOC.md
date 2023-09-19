# Dubo SDK

* [ask\_dubo](#ask_dubo)
  * [ask](#ask_dubo.ask)
  * [chart](#ask_dubo.chart)
  * [dispatch\_query](#ask_dubo.dispatch_query)
  * [retrieve\_result](#ask_dubo.retrieve_result)
  * [dispatch\_and\_retrieve](#ask_dubo.dispatch_and_retrieve)
  * [create\_doc](#ask_dubo.create_doc)
  * [update\_doc](#ask_dubo.update_doc)
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

# [(6,)]
```

<a id="ask_dubo.chart"></a>

## chart

```python
def chart(query: str,
          df: pd.DataFrame,
          specify_chart_type: ChartType | None = None,
          verbose=False,
          **kwargs)
```

Ask Dubo to generate a chart.

**Arguments**:

- `query` (`str`): The chart to ask Dubo to generate.
- `df` (`pd.DataFrame`): The DataFrame for the chart.
- `specify_chart_type` (`ChartType | None`): Type of chart: ChartType.DECK_GL or ChartType.VEGA_LITE.
- `verbose` (`bool`): Whether to print verbose logs.

**Returns**:

The chart.
##### Example
```python
import pandas as pd

from dubo import chart
from dubo.api_client.models import ChartType

housing_df = pd.read_csv("https://raw.githubusercontent.com/ajduberstein/geo_datasets/master/housing.csv")

res = chart(
    query="Map the houses",
    df=housing_df,
    specify_chart_type=ChartType.DECK_GL,
    as_string=True,
)
# <!DOCTYPE html>
#    <html>
#    ...
#    <body>
#        <div id="deck-container">
#        </div>
#    </body>
#    <script>
#        const container = document.getElementById('deck-container');
#        ...
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

<a id="ask_dubo.create_doc"></a>

## create\_doc

```python
def create_doc(file_path: str,
               shingle_length: int = 1000,
               step: int = 500) -> DataSourceDocument
```

Create Documentation.

**Arguments**:

- `file_path`: The path to the file to upload.
- `shingle_length`: TBC.
- `step`: TBC.

**Returns**:

The documentation
##### Example
```python
from dubo import update_doc

update_doc(
    data_source_documentation_id=res.id,
    file_path="./documentation.txt",
    shingle_length=1000,
    step=500,
)
# > True

res = create_doc(
    file_path="./documentation.txt",
    shingle_length=1000,
    step=500,
)
# > DataSourceDocument(
#     id='c1d62c33-4561-4b5f-b2c2-e0203cee1f7b',
#     file_name='documentation.txt',
#     data_source_id=...,
#     organization_id=...,
#     created_at=...,
#     updated_at=...,
# )
```

<a id="ask_dubo.update_doc"></a>

## update\_doc

```python
def update_doc(data_source_documentation_id: str,
               file_path: str,
               shingle_length: int = 1000,
               step: int = 500) -> bool
```

Update Document.

**Arguments**:

- `data_source_documentation_id`: The ID of the document to update.
- `file_path`: The path to the file to upload.
- `shingle_length`: TBC.
- `step`: TBC.

**Returns**:

True if successful, False otherwise
##### Example
```python
from dubo import update_doc

update_doc(
    data_source_documentation_id="c1d62c33-4561-4b5f-b2c2-e0203cee1f7b",
    file_path="./documentation.txt",
    shingle_length=1000,
    step=500,
)
# > True
```

<a id="ask_dubo.delete_doc"></a>

## delete\_doc

```python
def delete_doc(data_source_documentation_id: str) -> bool
```

Delete a document by its ID.

**Arguments**:

- `data_source_documentation_id`: The ID of the document to delete.

**Returns**:

True if the deletion was successful, False otherwise
##### Example
```python
from dubo import delete_doc

delete_doc("c1d62c33-4561-4b5f-b2c2-e0203cee1f7b")
# > True
```


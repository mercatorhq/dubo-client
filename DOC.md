# Dubo SDK

* [ask\_dubo](#ask_dubo)
  * [ask](#ask_dubo.ask)
  * [chart](#ask_dubo.chart)
  * [query](#ask_dubo.query)
  * [generate\_sql](#ask_dubo.generate_sql)
  * [search\_tables](#ask_dubo.search_tables)
  * [create\_doc](#ask_dubo.create_doc)
  * [get\_doc](#ask_dubo.get_doc)
  * [get\_all\_docs](#ask_dubo.get_all_docs)
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

chart(
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

<a id="ask_dubo.query"></a>

## query

```python
def query(query_text: str, fast: bool = False) -> DataResult
```

Ask Dubo a question.

**Arguments**:

- `query_text` (`str`): The question to ask Dubo.
- `fast` (`bool`): Use faster, less accurate model

**Returns**:

The SQL query.
##### Example
```python
from dubo import query

query("How many area types are there?")

# DataResult(
#  id='query-56513883-6749-4f2b-ad57-7bb8cb350161',
#  query_text='How many area types are there?',
#  status=QueryStatus.SUCCESS,
#  results_set=[{'count': 9}],
#  row_count=1
# )
```

<a id="ask_dubo.generate_sql"></a>

## generate\_sql

```python
def generate_sql(query_text: str, fast: bool = False) -> str
```

Ask Dubo to generate a SQL query.

**Arguments**:

- `query_text` (`str`): The plain text query.
- `fast` (`bool`): Use faster, less accurate model

**Returns**:

The SQL query.
##### Example
```python
from dubo import query

query("How many area types are there?")

# "SELECT COUNT(DISTINCT type) AS num_area_types FROM public.area"
```

<a id="ask_dubo.search_tables"></a>

## search\_tables

```python
def search_tables(query_text: str, fast: bool = False) -> List[AttenuatedDDL]
```

Ask Dubo to return the list of tables that are a potential match for this query.

**Arguments**:

- `query_text` (`str`): The plain text query.
- `fast` (`bool`): Use faster, less accurate model

**Returns**:

The list of tables.
##### Example
```python
from dubo import query

query("How many area types are there?")

# [
#   AttenuatedDDL(
#      cols=[
#          TableColumn(column_name='name', data_type='character varying', is_nullable=False, table_name='area_type', schema_name='public', is_partitioning_column=None),
#          TableColumn(column_name='parent', data_type='integer', is_nullable=True, table_name='area_type', schema_name='public', is_partitioning_column=None),
#          TableColumn(column_name='description', data_type='text', is_nullable=True, table_name='area_type', schema_name='public', is_partitioning_column=None),
#          TableColumn(column_name='gid', data_type='uuid', is_nullable=False, table_name='area_type', schema_name='public', is_partitioning_column=None),
#          TableColumn(column_name='id', data_type='integer', is_nullable=False, table_name='area_type', schema_name='public', is_partitioning_column=None),
#          TableColumn(column_name='child_order', data_type='integer', is_nullable=False, table_name='area_type', schema_name='public', is_partitioning_column=None),
#      ],
#      table_name='area_type',
#      schema_name='public',
#      id='e3e10474-aa55-4654-bfb8-6592dc540127',
#      database_name='postgres',
#      description='Table storing different types of areas, including their parent-child relationships and descriptions',
#   ),
#  ...
# ]
```

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
from dubo import create_doc

create_doc(
    file_path="./documentation.txt",
    shingle_length=1000,
    step=500,
)

# DataSourceDocument(
#   id='c1d62c33-4561-4b5f-b2c2-e0203cee1f7b',
#   file_name='documentation.txt',
#   data_source_id=...,
#   organization_id=...,
#   created_at=...,
#   updated_at=...,
# )
```

<a id="ask_dubo.get_doc"></a>

## get\_doc

```python
def get_doc(data_source_documentation_id: str) -> DataSourceDocument
```

Get one document by ID.

**Arguments**:

- `data_source_documentation_id`: The ID of the document to get.

**Returns**:

The document
##### Example
```python
from dubo import get_doc

get_doc("c1d62c33-4561-4b5f-b2c2-e0203cee1f7b")

# DataSourceDocument(
#   id='c1d62c33-4561-4b5f-b2c2-e0203cee1f7b',
#   file_name='documentation.txt',
#   data_source_id=...,
#   organization_id=...,
#   created_at=...,
#   updated_at=...,
# )
```

<a id="ask_dubo.get_all_docs"></a>

## get\_all\_docs

```python
def get_all_docs() -> List[Dict[str, str]]
```

Get All Documents.

**Returns**:

The list of documents (file_name and id)
##### Example
```python
from dubo import get_all_docs

get_all_docs()

# [{'file_name': 'documentation.txt', 'id': 'c1d62c33-4561-4b5f-b2c2-e0203cee1f7b'}]
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

# True
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

# True
```


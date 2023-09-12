from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.query_status import QueryStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ask_dispatch_response_results_set_item import AskDispatchResponseResultsSetItem
    from ..models.attenuated_ddl import AttenuatedDDL


T = TypeVar("T", bound="AskDispatchResponse")


@_attrs_define
class AskDispatchResponse:
    """Response to a developer API query dispatch request. NOTE: DO NOT use this in other parts of the application. Prefer
    QueryExecution.

        Attributes:
            id (str):
            query_text (str):
            status (QueryStatus): An enumeration.
            tables (Union[Unset, List['AttenuatedDDL']]):
            results_set (Union[Unset, List['AskDispatchResponseResultsSetItem']]):
            sql_text (Union[Unset, str]):
            row_count (Union[Unset, int]):
    """

    id: str
    query_text: str
    status: QueryStatus
    tables: Union[Unset, List["AttenuatedDDL"]] = UNSET
    results_set: Union[Unset, List["AskDispatchResponseResultsSetItem"]] = UNSET
    sql_text: Union[Unset, str] = UNSET
    row_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        query_text = self.query_text
        status = self.status.value

        tables: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tables, Unset):
            tables = []
            for tables_item_data in self.tables:
                tables_item = tables_item_data.to_dict()

                tables.append(tables_item)

        results_set: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.results_set, Unset):
            results_set = []
            for results_set_item_data in self.results_set:
                results_set_item = results_set_item_data.to_dict()

                results_set.append(results_set_item)

        sql_text = self.sql_text
        row_count = self.row_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "query_text": query_text,
                "status": status,
            }
        )
        if tables is not UNSET:
            field_dict["tables"] = tables
        if results_set is not UNSET:
            field_dict["results_set"] = results_set
        if sql_text is not UNSET:
            field_dict["sql_text"] = sql_text
        if row_count is not UNSET:
            field_dict["row_count"] = row_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ask_dispatch_response_results_set_item import AskDispatchResponseResultsSetItem
        from ..models.attenuated_ddl import AttenuatedDDL

        d = src_dict.copy()
        id = d.pop("id")

        query_text = d.pop("query_text")

        status = QueryStatus(d.pop("status"))

        tables = []
        _tables = d.pop("tables", UNSET)
        for tables_item_data in _tables or []:
            tables_item = AttenuatedDDL.from_dict(tables_item_data)

            tables.append(tables_item)

        results_set = []
        _results_set = d.pop("results_set", UNSET)
        for results_set_item_data in _results_set or []:
            results_set_item = AskDispatchResponseResultsSetItem.from_dict(results_set_item_data)

            results_set.append(results_set_item)

        sql_text = d.pop("sql_text", UNSET)

        row_count = d.pop("row_count", UNSET)

        ask_dispatch_response = cls(
            id=id,
            query_text=query_text,
            status=status,
            tables=tables,
            results_set=results_set,
            sql_text=sql_text,
            row_count=row_count,
        )

        ask_dispatch_response.additional_properties = d
        return ask_dispatch_response

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryExecutionCreateMinimal")


@_attrs_define
class QueryExecutionCreateMinimal:
    """
    Attributes:
        data_source_id (str):
        user_query (Union[Unset, str]):
        sql_text (Union[Unset, str]):
        thread_id (Union[Unset, str]):
        debug (Union[Unset, bool]):
        fast (Union[Unset, bool]):
    """

    data_source_id: str
    user_query: Union[Unset, str] = UNSET
    sql_text: Union[Unset, str] = UNSET
    thread_id: Union[Unset, str] = UNSET
    debug: Union[Unset, bool] = False
    fast: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_source_id = self.data_source_id
        user_query = self.user_query
        sql_text = self.sql_text
        thread_id = self.thread_id
        debug = self.debug
        fast = self.fast

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data_source_id": data_source_id,
            }
        )
        if user_query is not UNSET:
            field_dict["user_query"] = user_query
        if sql_text is not UNSET:
            field_dict["sql_text"] = sql_text
        if thread_id is not UNSET:
            field_dict["thread_id"] = thread_id
        if debug is not UNSET:
            field_dict["debug"] = debug
        if fast is not UNSET:
            field_dict["fast"] = fast

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        data_source_id = d.pop("data_source_id")

        user_query = d.pop("user_query", UNSET)

        sql_text = d.pop("sql_text", UNSET)

        thread_id = d.pop("thread_id", UNSET)

        debug = d.pop("debug", UNSET)

        fast = d.pop("fast", UNSET)

        query_execution_create_minimal = cls(
            data_source_id=data_source_id,
            user_query=user_query,
            sql_text=sql_text,
            thread_id=thread_id,
            debug=debug,
            fast=fast,
        )

        query_execution_create_minimal.additional_properties = d
        return query_execution_create_minimal

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

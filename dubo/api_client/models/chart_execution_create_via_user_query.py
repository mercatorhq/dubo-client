from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chart_type import ChartType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ChartExecutionCreateViaUserQuery")


@_attrs_define
class ChartExecutionCreateViaUserQuery:
    """
    Attributes:
        user_query (str):
        chart_type (ChartType): An enumeration.
        thread_id (str):
        query_execution_id (str):
        fast (Union[Unset, bool]):
        include_results (Union[Unset, bool]):
    """

    user_query: str
    chart_type: ChartType
    thread_id: str
    query_execution_id: str
    fast: Union[Unset, bool] = False
    include_results: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_query = self.user_query
        chart_type = self.chart_type.value

        thread_id = self.thread_id
        query_execution_id = self.query_execution_id
        fast = self.fast
        include_results = self.include_results

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_query": user_query,
                "chart_type": chart_type,
                "thread_id": thread_id,
                "query_execution_id": query_execution_id,
            }
        )
        if fast is not UNSET:
            field_dict["fast"] = fast
        if include_results is not UNSET:
            field_dict["include_results"] = include_results

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_query = d.pop("user_query")

        chart_type = ChartType(d.pop("chart_type"))

        thread_id = d.pop("thread_id")

        query_execution_id = d.pop("query_execution_id")

        fast = d.pop("fast", UNSET)

        include_results = d.pop("include_results", UNSET)

        chart_execution_create_via_user_query = cls(
            user_query=user_query,
            chart_type=chart_type,
            thread_id=thread_id,
            query_execution_id=query_execution_id,
            fast=fast,
            include_results=include_results,
        )

        chart_execution_create_via_user_query.additional_properties = d
        return chart_execution_create_via_user_query

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

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chart_execution_chart_spec import ChartExecutionChartSpec
    from ..models.chart_execution_results_set_item import ChartExecutionResultsSetItem


T = TypeVar("T", bound="ChartExecution")


@_attrs_define
class ChartExecution:
    """
    Attributes:
        id (str):
        chart_spec (ChartExecutionChartSpec):
        query_execution_id (str):
        user_query (Union[Unset, str]):
        chart_type (Union[Unset, str]):
        thread_id (Union[Unset, str]):
        results_set (Union[Unset, List['ChartExecutionResultsSetItem']]):
    """

    id: str
    chart_spec: "ChartExecutionChartSpec"
    query_execution_id: str
    user_query: Union[Unset, str] = UNSET
    chart_type: Union[Unset, str] = UNSET
    thread_id: Union[Unset, str] = UNSET
    results_set: Union[Unset, List["ChartExecutionResultsSetItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        chart_spec = self.chart_spec.to_dict()

        query_execution_id = self.query_execution_id
        user_query = self.user_query
        chart_type = self.chart_type
        thread_id = self.thread_id
        results_set: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.results_set, Unset):
            results_set = []
            for results_set_item_data in self.results_set:
                results_set_item = results_set_item_data.to_dict()

                results_set.append(results_set_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "chart_spec": chart_spec,
                "query_execution_id": query_execution_id,
            }
        )
        if user_query is not UNSET:
            field_dict["user_query"] = user_query
        if chart_type is not UNSET:
            field_dict["chart_type"] = chart_type
        if thread_id is not UNSET:
            field_dict["thread_id"] = thread_id
        if results_set is not UNSET:
            field_dict["results_set"] = results_set

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.chart_execution_chart_spec import ChartExecutionChartSpec
        from ..models.chart_execution_results_set_item import ChartExecutionResultsSetItem

        d = src_dict.copy()
        id = d.pop("id")

        chart_spec = ChartExecutionChartSpec.from_dict(d.pop("chart_spec"))

        query_execution_id = d.pop("query_execution_id")

        user_query = d.pop("user_query", UNSET)

        chart_type = d.pop("chart_type", UNSET)

        thread_id = d.pop("thread_id", UNSET)

        results_set = []
        _results_set = d.pop("results_set", UNSET)
        for results_set_item_data in _results_set or []:
            results_set_item = ChartExecutionResultsSetItem.from_dict(results_set_item_data)

            results_set.append(results_set_item)

        chart_execution = cls(
            id=id,
            chart_spec=chart_spec,
            query_execution_id=query_execution_id,
            user_query=user_query,
            chart_type=chart_type,
            thread_id=thread_id,
            results_set=results_set,
        )

        chart_execution.additional_properties = d
        return chart_execution

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

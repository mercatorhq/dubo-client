from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dubo_chart_query_chart_spec import DuboChartQueryChartSpec
    from ..models.dubo_chart_query_data_snippet_item import DuboChartQueryDataSnippetItem


T = TypeVar("T", bound="DuboChartQuery")


@_attrs_define
class DuboChartQuery:
    """
    Attributes:
        user_query (str):
        data_snippet (List['DuboChartQueryDataSnippetItem']):
        fast (Union[Unset, bool]): Use faster less accurate model
        chart_spec (Union[Unset, DuboChartQueryChartSpec]):
        chart_type (Union[Unset, str]):  Default: 'vega_lite'.
        thread_id (Union[Unset, str]):
    """

    user_query: str
    data_snippet: List["DuboChartQueryDataSnippetItem"]
    fast: Union[Unset, bool] = False
    chart_spec: Union[Unset, "DuboChartQueryChartSpec"] = UNSET
    chart_type: Union[Unset, str] = "vega_lite"
    thread_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_query = self.user_query
        data_snippet = []
        for data_snippet_item_data in self.data_snippet:
            data_snippet_item = data_snippet_item_data.to_dict()

            data_snippet.append(data_snippet_item)

        fast = self.fast
        chart_spec: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.chart_spec, Unset):
            chart_spec = self.chart_spec.to_dict()

        chart_type = self.chart_type
        thread_id = self.thread_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_query": user_query,
                "data_snippet": data_snippet,
            }
        )
        if fast is not UNSET:
            field_dict["fast"] = fast
        if chart_spec is not UNSET:
            field_dict["chart_spec"] = chart_spec
        if chart_type is not UNSET:
            field_dict["chart_type"] = chart_type
        if thread_id is not UNSET:
            field_dict["thread_id"] = thread_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dubo_chart_query_chart_spec import DuboChartQueryChartSpec
        from ..models.dubo_chart_query_data_snippet_item import DuboChartQueryDataSnippetItem

        d = src_dict.copy()
        user_query = d.pop("user_query")

        data_snippet = []
        _data_snippet = d.pop("data_snippet")
        for data_snippet_item_data in _data_snippet:
            data_snippet_item = DuboChartQueryDataSnippetItem.from_dict(data_snippet_item_data)

            data_snippet.append(data_snippet_item)

        fast = d.pop("fast", UNSET)

        _chart_spec = d.pop("chart_spec", UNSET)
        chart_spec: Union[Unset, DuboChartQueryChartSpec]
        if isinstance(_chart_spec, Unset):
            chart_spec = UNSET
        else:
            chart_spec = DuboChartQueryChartSpec.from_dict(_chart_spec)

        chart_type = d.pop("chart_type", UNSET)

        thread_id = d.pop("thread_id", UNSET)

        dubo_chart_query = cls(
            user_query=user_query,
            data_snippet=data_snippet,
            fast=fast,
            chart_spec=chart_spec,
            chart_type=chart_type,
            thread_id=thread_id,
        )

        dubo_chart_query.additional_properties = d
        return dubo_chart_query

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

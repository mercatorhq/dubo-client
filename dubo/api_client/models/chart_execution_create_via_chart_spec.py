from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chart_type import ChartType

if TYPE_CHECKING:
    from ..models.chart_execution_create_via_chart_spec_chart_spec import ChartExecutionCreateViaChartSpecChartSpec


T = TypeVar("T", bound="ChartExecutionCreateViaChartSpec")


@_attrs_define
class ChartExecutionCreateViaChartSpec:
    """
    Attributes:
        chart_spec (ChartExecutionCreateViaChartSpecChartSpec):
        chart_type (ChartType): An enumeration.
        thread_id (str):
        query_execution_id (str):
    """

    chart_spec: "ChartExecutionCreateViaChartSpecChartSpec"
    chart_type: ChartType
    thread_id: str
    query_execution_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        chart_spec = self.chart_spec.to_dict()

        chart_type = self.chart_type.value

        thread_id = self.thread_id
        query_execution_id = self.query_execution_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chart_spec": chart_spec,
                "chart_type": chart_type,
                "thread_id": thread_id,
                "query_execution_id": query_execution_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.chart_execution_create_via_chart_spec_chart_spec import ChartExecutionCreateViaChartSpecChartSpec

        d = src_dict.copy()
        chart_spec = ChartExecutionCreateViaChartSpecChartSpec.from_dict(d.pop("chart_spec"))

        chart_type = ChartType(d.pop("chart_type"))

        thread_id = d.pop("thread_id")

        query_execution_id = d.pop("query_execution_id")

        chart_execution_create_via_chart_spec = cls(
            chart_spec=chart_spec,
            chart_type=chart_type,
            thread_id=thread_id,
            query_execution_id=query_execution_id,
        )

        chart_execution_create_via_chart_spec.additional_properties = d
        return chart_execution_create_via_chart_spec

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

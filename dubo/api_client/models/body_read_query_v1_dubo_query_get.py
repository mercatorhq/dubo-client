from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dubo_example import DuboExample


T = TypeVar("T", bound="BodyReadQueryV1DuboQueryGet")


@_attrs_define
class BodyReadQueryV1DuboQueryGet:
    """
    Attributes:
        query_examples (Union[Unset, List['DuboExample']]): The query examples to use
        data_sample (Union[Unset, List[List[Any]]]): The data sample to use
    """

    query_examples: Union[Unset, List["DuboExample"]] = UNSET
    data_sample: Union[Unset, List[List[Any]]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        query_examples: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.query_examples, Unset):
            query_examples = []
            for query_examples_item_data in self.query_examples:
                query_examples_item = query_examples_item_data.to_dict()

                query_examples.append(query_examples_item)

        data_sample: Union[Unset, List[List[Any]]] = UNSET
        if not isinstance(self.data_sample, Unset):
            data_sample = []
            for data_sample_item_data in self.data_sample:
                data_sample_item = data_sample_item_data

                data_sample.append(data_sample_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query_examples is not UNSET:
            field_dict["query_examples"] = query_examples
        if data_sample is not UNSET:
            field_dict["data_sample"] = data_sample

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dubo_example import DuboExample

        d = src_dict.copy()
        query_examples = []
        _query_examples = d.pop("query_examples", UNSET)
        for query_examples_item_data in _query_examples or []:
            query_examples_item = DuboExample.from_dict(query_examples_item_data)

            query_examples.append(query_examples_item)

        data_sample = []
        _data_sample = d.pop("data_sample", UNSET)
        for data_sample_item_data in _data_sample or []:
            data_sample_item = cast(List[Any], data_sample_item_data)

            data_sample.append(data_sample_item)

        body_read_query_v1_dubo_query_get = cls(
            query_examples=query_examples,
            data_sample=data_sample,
        )

        body_read_query_v1_dubo_query_get.additional_properties = d
        return body_read_query_v1_dubo_query_get

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

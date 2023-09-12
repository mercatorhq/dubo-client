from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dubo_example import DuboExample


T = TypeVar("T", bound="DuboQuery")


@_attrs_define
class DuboQuery:
    """
    Attributes:
        user_query (str):
        schemas (Union[Unset, List[str]]):
        descriptions (Union[Unset, List[str]]):
        query_examples (Union[Unset, List['DuboExample']]):
        data_header (Union[Unset, List[str]]):
        data_sample (Union[Unset, List[List[Any]]]):
        syntax_type (Union[Unset, str]):
        macros (Union[Unset, bool]): Enable or disable macros
        fast (Union[Unset, bool]): Use faster less accurate model
        model (Union[Unset, str]):
    """

    user_query: str
    schemas: Union[Unset, List[str]] = UNSET
    descriptions: Union[Unset, List[str]] = UNSET
    query_examples: Union[Unset, List["DuboExample"]] = UNSET
    data_header: Union[Unset, List[str]] = UNSET
    data_sample: Union[Unset, List[List[Any]]] = UNSET
    syntax_type: Union[Unset, str] = UNSET
    macros: Union[Unset, bool] = False
    fast: Union[Unset, bool] = False
    model: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_query = self.user_query
        schemas: Union[Unset, List[str]] = UNSET
        if not isinstance(self.schemas, Unset):
            schemas = self.schemas

        descriptions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.descriptions, Unset):
            descriptions = self.descriptions

        query_examples: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.query_examples, Unset):
            query_examples = []
            for query_examples_item_data in self.query_examples:
                query_examples_item = query_examples_item_data.to_dict()

                query_examples.append(query_examples_item)

        data_header: Union[Unset, List[str]] = UNSET
        if not isinstance(self.data_header, Unset):
            data_header = self.data_header

        data_sample: Union[Unset, List[List[Any]]] = UNSET
        if not isinstance(self.data_sample, Unset):
            data_sample = []
            for data_sample_item_data in self.data_sample:
                data_sample_item = data_sample_item_data

                data_sample.append(data_sample_item)

        syntax_type = self.syntax_type
        macros = self.macros
        fast = self.fast
        model = self.model

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_query": user_query,
            }
        )
        if schemas is not UNSET:
            field_dict["schemas"] = schemas
        if descriptions is not UNSET:
            field_dict["descriptions"] = descriptions
        if query_examples is not UNSET:
            field_dict["query_examples"] = query_examples
        if data_header is not UNSET:
            field_dict["data_header"] = data_header
        if data_sample is not UNSET:
            field_dict["data_sample"] = data_sample
        if syntax_type is not UNSET:
            field_dict["syntax_type"] = syntax_type
        if macros is not UNSET:
            field_dict["macros"] = macros
        if fast is not UNSET:
            field_dict["fast"] = fast
        if model is not UNSET:
            field_dict["model"] = model

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dubo_example import DuboExample

        d = src_dict.copy()
        user_query = d.pop("user_query")

        schemas = cast(List[str], d.pop("schemas", UNSET))

        descriptions = cast(List[str], d.pop("descriptions", UNSET))

        query_examples = []
        _query_examples = d.pop("query_examples", UNSET)
        for query_examples_item_data in _query_examples or []:
            query_examples_item = DuboExample.from_dict(query_examples_item_data)

            query_examples.append(query_examples_item)

        data_header = cast(List[str], d.pop("data_header", UNSET))

        data_sample = []
        _data_sample = d.pop("data_sample", UNSET)
        for data_sample_item_data in _data_sample or []:
            data_sample_item = cast(List[Any], data_sample_item_data)

            data_sample.append(data_sample_item)

        syntax_type = d.pop("syntax_type", UNSET)

        macros = d.pop("macros", UNSET)

        fast = d.pop("fast", UNSET)

        model = d.pop("model", UNSET)

        dubo_query = cls(
            user_query=user_query,
            schemas=schemas,
            descriptions=descriptions,
            query_examples=query_examples,
            data_header=data_header,
            data_sample=data_sample,
            syntax_type=syntax_type,
            macros=macros,
            fast=fast,
            model=model,
        )

        dubo_query.additional_properties = d
        return dubo_query

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

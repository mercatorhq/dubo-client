from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyAskAnLlmV1DuboLlmPost")


@_attrs_define
class BodyAskAnLlmV1DuboLlmPost:
    """
    Attributes:
        query (Union[Unset, str]): The query
        model (Union[Unset, str]): The model to use Default: 'llama2-7b'.
    """

    query: Union[Unset, str] = UNSET
    model: Union[Unset, str] = "llama2-7b"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        query = self.query
        model = self.model

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query is not UNSET:
            field_dict["query"] = query
        if model is not UNSET:
            field_dict["model"] = model

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        query = d.pop("query", UNSET)

        model = d.pop("model", UNSET)

        body_ask_an_llm_v1_dubo_llm_post = cls(
            query=query,
            model=model,
        )

        body_ask_an_llm_v1_dubo_llm_post.additional_properties = d
        return body_ask_an_llm_v1_dubo_llm_post

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

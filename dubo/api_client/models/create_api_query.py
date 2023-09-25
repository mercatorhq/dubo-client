from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_api_query_mode import CreateApiQueryMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateApiQuery")


@_attrs_define
class CreateApiQuery:
    """Developer API query POST body. NOTE: DO NOT use this in other parts of the application. Prefer QueryExecutionCreate.

    Attributes:
        query_text (str):
        fast (Union[Unset, bool]):
        mode (Union[Unset, CreateApiQueryMode]): Developer API query POST body. NOTE: DO NOT use this in other parts of
            the application. Prefer QueryExecutionCreate. Default: CreateApiQueryMode.FULL_EXECUTION.
    """

    query_text: str
    fast: Union[Unset, bool] = False
    mode: Union[Unset, CreateApiQueryMode] = CreateApiQueryMode.FULL_EXECUTION
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        query_text = self.query_text
        fast = self.fast
        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query_text": query_text,
            }
        )
        if fast is not UNSET:
            field_dict["fast"] = fast
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        query_text = d.pop("query_text")

        fast = d.pop("fast", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, CreateApiQueryMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = CreateApiQueryMode(_mode)

        create_api_query = cls(
            query_text=query_text,
            fast=fast,
            mode=mode,
        )

        create_api_query.additional_properties = d
        return create_api_query

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

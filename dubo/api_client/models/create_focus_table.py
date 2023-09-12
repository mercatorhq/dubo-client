from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateFocusTable")


@_attrs_define
class CreateFocusTable:
    """
    Attributes:
        thread_id (str):
        prompt_table_ids (Union[Unset, List[str]]):
    """

    thread_id: str
    prompt_table_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        thread_id = self.thread_id
        prompt_table_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.prompt_table_ids, Unset):
            prompt_table_ids = self.prompt_table_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "thread_id": thread_id,
            }
        )
        if prompt_table_ids is not UNSET:
            field_dict["prompt_table_ids"] = prompt_table_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        thread_id = d.pop("thread_id")

        prompt_table_ids = cast(List[str], d.pop("prompt_table_ids", UNSET))

        create_focus_table = cls(
            thread_id=thread_id,
            prompt_table_ids=prompt_table_ids,
        )

        create_focus_table.additional_properties = d
        return create_focus_table

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

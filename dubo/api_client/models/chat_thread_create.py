from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatThreadCreate")


@_attrs_define
class ChatThreadCreate:
    """
    Attributes:
        data_source_id (str):
        name (Union[Unset, str]):  Default: 'New Analysis'.
        description (Union[Unset, str]):
        forked_from_event_id (Union[Unset, str]):
        forked_from_thread_id (Union[Unset, str]):
    """

    data_source_id: str
    name: Union[Unset, str] = "New Analysis"
    description: Union[Unset, str] = UNSET
    forked_from_event_id: Union[Unset, str] = UNSET
    forked_from_thread_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_source_id = self.data_source_id
        name = self.name
        description = self.description
        forked_from_event_id = self.forked_from_event_id
        forked_from_thread_id = self.forked_from_thread_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data_source_id": data_source_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if forked_from_event_id is not UNSET:
            field_dict["forked_from_event_id"] = forked_from_event_id
        if forked_from_thread_id is not UNSET:
            field_dict["forked_from_thread_id"] = forked_from_thread_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        data_source_id = d.pop("data_source_id")

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        forked_from_event_id = d.pop("forked_from_event_id", UNSET)

        forked_from_thread_id = d.pop("forked_from_thread_id", UNSET)

        chat_thread_create = cls(
            data_source_id=data_source_id,
            name=name,
            description=description,
            forked_from_event_id=forked_from_event_id,
            forked_from_thread_id=forked_from_thread_id,
        )

        chat_thread_create.additional_properties = d
        return chat_thread_create

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

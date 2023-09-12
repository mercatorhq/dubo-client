import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatThread")


@_attrs_define
class ChatThread:
    """
    Attributes:
        id (str):
        data_source_id (str):
        created_by (str):
        created_at (datetime.datetime):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
    """

    id: str
    data_source_id: str
    created_by: str
    created_at: datetime.datetime
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        data_source_id = self.data_source_id
        created_by = self.created_by
        created_at = self.created_at.isoformat()

        name = self.name
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "data_source_id": data_source_id,
                "created_by": created_by,
                "created_at": created_at,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        data_source_id = d.pop("data_source_id")

        created_by = d.pop("created_by")

        created_at = isoparse(d.pop("created_at"))

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        chat_thread = cls(
            id=id,
            data_source_id=data_source_id,
            created_by=created_by,
            created_at=created_at,
            name=name,
            description=description,
        )

        chat_thread.additional_properties = d
        return chat_thread

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

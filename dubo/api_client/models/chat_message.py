import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.chat_role_types import ChatRoleTypes
from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatMessage")


@_attrs_define
class ChatMessage:
    """
    Attributes:
        id (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        thread_id (str):
        role (ChatRoleTypes): An enumeration.
        message (str):
        message_type (Union[Unset, str]):
        data_source_id (Union[Unset, str]):
    """

    id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    thread_id: str
    role: ChatRoleTypes
    message: str
    message_type: Union[Unset, str] = UNSET
    data_source_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        thread_id = self.thread_id
        role = self.role.value

        message = self.message
        message_type = self.message_type
        data_source_id = self.data_source_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
                "thread_id": thread_id,
                "role": role,
                "message": message,
            }
        )
        if message_type is not UNSET:
            field_dict["message_type"] = message_type
        if data_source_id is not UNSET:
            field_dict["data_source_id"] = data_source_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        thread_id = d.pop("thread_id")

        role = ChatRoleTypes(d.pop("role"))

        message = d.pop("message")

        message_type = d.pop("message_type", UNSET)

        data_source_id = d.pop("data_source_id", UNSET)

        chat_message = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            thread_id=thread_id,
            role=role,
            message=message,
            message_type=message_type,
            data_source_id=data_source_id,
        )

        chat_message.additional_properties = d
        return chat_message

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

from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chat_message_types import ChatMessageTypes
from ..models.chat_role_types import ChatRoleTypes
from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatMessageCreate")


@_attrs_define
class ChatMessageCreate:
    """
    Attributes:
        role (ChatRoleTypes): An enumeration.
        message (str):
        message_type (ChatMessageTypes): An enumeration.
        data_source_id (str):
        thread_id (Union[Unset, str]):
        prompt_table_ids (Union[Unset, List[str]]):
    """

    role: ChatRoleTypes
    message: str
    message_type: ChatMessageTypes
    data_source_id: str
    thread_id: Union[Unset, str] = UNSET
    prompt_table_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role = self.role.value

        message = self.message
        message_type = self.message_type.value

        data_source_id = self.data_source_id
        thread_id = self.thread_id
        prompt_table_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.prompt_table_ids, Unset):
            prompt_table_ids = self.prompt_table_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "message": message,
                "message_type": message_type,
                "data_source_id": data_source_id,
            }
        )
        if thread_id is not UNSET:
            field_dict["thread_id"] = thread_id
        if prompt_table_ids is not UNSET:
            field_dict["prompt_table_ids"] = prompt_table_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        role = ChatRoleTypes(d.pop("role"))

        message = d.pop("message")

        message_type = ChatMessageTypes(d.pop("message_type"))

        data_source_id = d.pop("data_source_id")

        thread_id = d.pop("thread_id", UNSET)

        prompt_table_ids = cast(List[str], d.pop("prompt_table_ids", UNSET))

        chat_message_create = cls(
            role=role,
            message=message,
            message_type=message_type,
            data_source_id=data_source_id,
            thread_id=thread_id,
            prompt_table_ids=prompt_table_ids,
        )

        chat_message_create.additional_properties = d
        return chat_message_create

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

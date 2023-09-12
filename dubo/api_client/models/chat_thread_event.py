import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.message_types import MessageTypes
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chart_execution import ChartExecution
    from ..models.chat_message import ChatMessage
    from ..models.query_execution import QueryExecution


T = TypeVar("T", bound="ChatThreadEvent")


@_attrs_define
class ChatThreadEvent:
    """
    Attributes:
        event_id (str):
        thread_id (str):
        message (Union['ChartExecution', 'ChatMessage', 'QueryExecution']):
        message_type (MessageTypes): An enumeration.
        created_at (datetime.datetime):
        hidden_at (Union[Unset, datetime.datetime]):
    """

    event_id: str
    thread_id: str
    message: Union["ChartExecution", "ChatMessage", "QueryExecution"]
    message_type: MessageTypes
    created_at: datetime.datetime
    hidden_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.chart_execution import ChartExecution
        from ..models.query_execution import QueryExecution

        event_id = self.event_id
        thread_id = self.thread_id
        message: Dict[str, Any]

        if isinstance(self.message, ChartExecution):
            message = self.message.to_dict()

        elif isinstance(self.message, QueryExecution):
            message = self.message.to_dict()

        else:
            message = self.message.to_dict()

        message_type = self.message_type.value

        created_at = self.created_at.isoformat()

        hidden_at: Union[Unset, str] = UNSET
        if not isinstance(self.hidden_at, Unset):
            hidden_at = self.hidden_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_id": event_id,
                "thread_id": thread_id,
                "message": message,
                "message_type": message_type,
                "created_at": created_at,
            }
        )
        if hidden_at is not UNSET:
            field_dict["hidden_at"] = hidden_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.chart_execution import ChartExecution
        from ..models.chat_message import ChatMessage
        from ..models.query_execution import QueryExecution

        d = src_dict.copy()
        event_id = d.pop("event_id")

        thread_id = d.pop("thread_id")

        def _parse_message(data: object) -> Union["ChartExecution", "ChatMessage", "QueryExecution"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_0 = ChartExecution.from_dict(data)

                return message_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_1 = QueryExecution.from_dict(data)

                return message_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            message_type_2 = ChatMessage.from_dict(data)

            return message_type_2

        message = _parse_message(d.pop("message"))

        message_type = MessageTypes(d.pop("message_type"))

        created_at = isoparse(d.pop("created_at"))

        _hidden_at = d.pop("hidden_at", UNSET)
        hidden_at: Union[Unset, datetime.datetime]
        if isinstance(_hidden_at, Unset):
            hidden_at = UNSET
        else:
            hidden_at = isoparse(_hidden_at)

        chat_thread_event = cls(
            event_id=event_id,
            thread_id=thread_id,
            message=message,
            message_type=message_type,
            created_at=created_at,
            hidden_at=hidden_at,
        )

        chat_thread_event.additional_properties = d
        return chat_thread_event

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

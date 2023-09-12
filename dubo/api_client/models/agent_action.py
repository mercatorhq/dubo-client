import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_payload import AgentPayload


T = TypeVar("T", bound="AgentAction")


@_attrs_define
class AgentAction:
    """
    Attributes:
        agent_payload (AgentPayload):
        id (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        agent_task_id (str):
        command_output (Union[Unset, str]):
        command_error (Union[Unset, str]):
    """

    agent_payload: "AgentPayload"
    id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    agent_task_id: str
    command_output: Union[Unset, str] = UNSET
    command_error: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        agent_payload = self.agent_payload.to_dict()

        id = self.id
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        agent_task_id = self.agent_task_id
        command_output = self.command_output
        command_error = self.command_error

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_payload": agent_payload,
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
                "agent_task_id": agent_task_id,
            }
        )
        if command_output is not UNSET:
            field_dict["command_output"] = command_output
        if command_error is not UNSET:
            field_dict["command_error"] = command_error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.agent_payload import AgentPayload

        d = src_dict.copy()
        agent_payload = AgentPayload.from_dict(d.pop("agent_payload"))

        id = d.pop("id")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        agent_task_id = d.pop("agent_task_id")

        command_output = d.pop("command_output", UNSET)

        command_error = d.pop("command_error", UNSET)

        agent_action = cls(
            agent_payload=agent_payload,
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            agent_task_id=agent_task_id,
            command_output=command_output,
            command_error=command_error,
        )

        agent_action.additional_properties = d
        return agent_action

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

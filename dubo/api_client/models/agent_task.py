import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.agent_task_status import AgentTaskStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_action import AgentAction


T = TypeVar("T", bound="AgentTask")


@_attrs_define
class AgentTask:
    """
    Attributes:
        goals (List[str]):
        data_source_id (str):
        id (str):
        created_by_user_id (str):
        status (AgentTaskStatus): An enumeration.
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        last_action (Union[Unset, AgentAction]):
        feedback (Union[Unset, str]):
    """

    goals: List[str]
    data_source_id: str
    id: str
    created_by_user_id: str
    status: AgentTaskStatus
    created_at: datetime.datetime
    updated_at: datetime.datetime
    last_action: Union[Unset, "AgentAction"] = UNSET
    feedback: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        goals = self.goals

        data_source_id = self.data_source_id
        id = self.id
        created_by_user_id = self.created_by_user_id
        status = self.status.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        last_action: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.last_action, Unset):
            last_action = self.last_action.to_dict()

        feedback = self.feedback

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "goals": goals,
                "data_source_id": data_source_id,
                "id": id,
                "created_by_user_id": created_by_user_id,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if last_action is not UNSET:
            field_dict["last_action"] = last_action
        if feedback is not UNSET:
            field_dict["feedback"] = feedback

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.agent_action import AgentAction

        d = src_dict.copy()
        goals = cast(List[str], d.pop("goals"))

        data_source_id = d.pop("data_source_id")

        id = d.pop("id")

        created_by_user_id = d.pop("created_by_user_id")

        status = AgentTaskStatus(d.pop("status"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        _last_action = d.pop("last_action", UNSET)
        last_action: Union[Unset, AgentAction]
        if isinstance(_last_action, Unset):
            last_action = UNSET
        else:
            last_action = AgentAction.from_dict(_last_action)

        feedback = d.pop("feedback", UNSET)

        agent_task = cls(
            goals=goals,
            data_source_id=data_source_id,
            id=id,
            created_by_user_id=created_by_user_id,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            last_action=last_action,
            feedback=feedback,
        )

        agent_task.additional_properties = d
        return agent_task

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

from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AgentTaskFeedback")


@_attrs_define
class AgentTaskFeedback:
    """
    Attributes:
        agent_task_id (str):
        feedback (str):
    """

    agent_task_id: str
    feedback: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        agent_task_id = self.agent_task_id
        feedback = self.feedback

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_task_id": agent_task_id,
                "feedback": feedback,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        agent_task_id = d.pop("agent_task_id")

        feedback = d.pop("feedback")

        agent_task_feedback = cls(
            agent_task_id=agent_task_id,
            feedback=feedback,
        )

        agent_task_feedback.additional_properties = d
        return agent_task_feedback

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

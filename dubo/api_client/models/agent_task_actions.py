from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_action import AgentAction
    from ..models.agent_synopsis import AgentSynopsis
    from ..models.agent_task import AgentTask


T = TypeVar("T", bound="AgentTaskActions")


@_attrs_define
class AgentTaskActions:
    """
    Attributes:
        agent_task (AgentTask):
        actions (Union[Unset, List['AgentAction']]):
        references (Union[Unset, List['AgentSynopsis']]):
    """

    agent_task: "AgentTask"
    actions: Union[Unset, List["AgentAction"]] = UNSET
    references: Union[Unset, List["AgentSynopsis"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        agent_task = self.agent_task.to_dict()

        actions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.actions, Unset):
            actions = []
            for actions_item_data in self.actions:
                actions_item = actions_item_data.to_dict()

                actions.append(actions_item)

        references: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.references, Unset):
            references = []
            for references_item_data in self.references:
                references_item = references_item_data.to_dict()

                references.append(references_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_task": agent_task,
            }
        )
        if actions is not UNSET:
            field_dict["actions"] = actions
        if references is not UNSET:
            field_dict["references"] = references

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.agent_action import AgentAction
        from ..models.agent_synopsis import AgentSynopsis
        from ..models.agent_task import AgentTask

        d = src_dict.copy()
        agent_task = AgentTask.from_dict(d.pop("agent_task"))

        actions = []
        _actions = d.pop("actions", UNSET)
        for actions_item_data in _actions or []:
            actions_item = AgentAction.from_dict(actions_item_data)

            actions.append(actions_item)

        references = []
        _references = d.pop("references", UNSET)
        for references_item_data in _references or []:
            references_item = AgentSynopsis.from_dict(references_item_data)

            references.append(references_item)

        agent_task_actions = cls(
            agent_task=agent_task,
            actions=actions,
            references=references,
        )

        agent_task_actions.additional_properties = d
        return agent_task_actions

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

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.agent_command_command_args import AgentCommandCommandArgs


T = TypeVar("T", bound="AgentCommand")


@_attrs_define
class AgentCommand:
    """
    Attributes:
        command_name (str):
        command_args (AgentCommandCommandArgs):
    """

    command_name: str
    command_args: "AgentCommandCommandArgs"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        command_name = self.command_name
        command_args = self.command_args.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "command_name": command_name,
                "command_args": command_args,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.agent_command_command_args import AgentCommandCommandArgs

        d = src_dict.copy()
        command_name = d.pop("command_name")

        command_args = AgentCommandCommandArgs.from_dict(d.pop("command_args"))

        agent_command = cls(
            command_name=command_name,
            command_args=command_args,
        )

        agent_command.additional_properties = d
        return agent_command

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

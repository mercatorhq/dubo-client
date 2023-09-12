from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_command_status import AgentCommandStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_command import AgentCommand
    from ..models.agent_payload_results import AgentPayloadResults
    from ..models.agent_thoughts import AgentThoughts


T = TypeVar("T", bound="AgentPayload")


@_attrs_define
class AgentPayload:
    """
    Attributes:
        thoughts (AgentThoughts):
        command (AgentCommand):
        status (AgentCommandStatus): An enumeration.
        results (Union[Unset, AgentPayloadResults]):
        error (Union[Unset, str]):
    """

    thoughts: "AgentThoughts"
    command: "AgentCommand"
    status: AgentCommandStatus
    results: Union[Unset, "AgentPayloadResults"] = UNSET
    error: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        thoughts = self.thoughts.to_dict()

        command = self.command.to_dict()

        status = self.status.value

        results: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.results, Unset):
            results = self.results.to_dict()

        error = self.error

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "thoughts": thoughts,
                "command": command,
                "status": status,
            }
        )
        if results is not UNSET:
            field_dict["results"] = results
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.agent_command import AgentCommand
        from ..models.agent_payload_results import AgentPayloadResults
        from ..models.agent_thoughts import AgentThoughts

        d = src_dict.copy()
        thoughts = AgentThoughts.from_dict(d.pop("thoughts"))

        command = AgentCommand.from_dict(d.pop("command"))

        status = AgentCommandStatus(d.pop("status"))

        _results = d.pop("results", UNSET)
        results: Union[Unset, AgentPayloadResults]
        if isinstance(_results, Unset):
            results = UNSET
        else:
            results = AgentPayloadResults.from_dict(_results)

        error = d.pop("error", UNSET)

        agent_payload = cls(
            thoughts=thoughts,
            command=command,
            status=status,
            results=results,
            error=error,
        )

        agent_payload.additional_properties = d
        return agent_payload

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

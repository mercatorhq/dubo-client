from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AgentThoughts")


@_attrs_define
class AgentThoughts:
    """
    Attributes:
        text (str):
        reasoning (str):
        plan (str):
        criticism (str):
        speak (str):
    """

    text: str
    reasoning: str
    plan: str
    criticism: str
    speak: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text
        reasoning = self.reasoning
        plan = self.plan
        criticism = self.criticism
        speak = self.speak

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
                "reasoning": reasoning,
                "plan": plan,
                "criticism": criticism,
                "speak": speak,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text")

        reasoning = d.pop("reasoning")

        plan = d.pop("plan")

        criticism = d.pop("criticism")

        speak = d.pop("speak")

        agent_thoughts = cls(
            text=text,
            reasoning=reasoning,
            plan=plan,
            criticism=criticism,
            speak=speak,
        )

        agent_thoughts.additional_properties = d
        return agent_thoughts

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

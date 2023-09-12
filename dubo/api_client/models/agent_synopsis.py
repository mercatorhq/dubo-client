import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentSynopsis")


@_attrs_define
class AgentSynopsis:
    """
    Attributes:
        text (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        agent_task_id (str):
        data_source_id (str):
        name (Union[Unset, str]):
        match_score (Union[Unset, float]):
    """

    text: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    agent_task_id: str
    data_source_id: str
    name: Union[Unset, str] = UNSET
    match_score: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        agent_task_id = self.agent_task_id
        data_source_id = self.data_source_id
        name = self.name
        match_score = self.match_score

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
                "created_at": created_at,
                "updated_at": updated_at,
                "agent_task_id": agent_task_id,
                "data_source_id": data_source_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if match_score is not UNSET:
            field_dict["match_score"] = match_score

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        agent_task_id = d.pop("agent_task_id")

        data_source_id = d.pop("data_source_id")

        name = d.pop("name", UNSET)

        match_score = d.pop("match_score", UNSET)

        agent_synopsis = cls(
            text=text,
            created_at=created_at,
            updated_at=updated_at,
            agent_task_id=agent_task_id,
            data_source_id=data_source_id,
            name=name,
            match_score=match_score,
        )

        agent_synopsis.additional_properties = d
        return agent_synopsis

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

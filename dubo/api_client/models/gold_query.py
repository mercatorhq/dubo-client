from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GoldQuery")


@_attrs_define
class GoldQuery:
    """
    Attributes:
        nl_query (str):
        sql_text (str):
    """

    nl_query: str
    sql_text: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nl_query = self.nl_query
        sql_text = self.sql_text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nl_query": nl_query,
                "sql_text": sql_text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        nl_query = d.pop("nl_query")

        sql_text = d.pop("sql_text")

        gold_query = cls(
            nl_query=nl_query,
            sql_text=sql_text,
        )

        gold_query.additional_properties = d
        return gold_query

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

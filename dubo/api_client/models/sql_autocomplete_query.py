from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SqlAutocompleteQuery")


@_attrs_define
class SqlAutocompleteQuery:
    """
    Attributes:
        sql_text (str):
        cursor_position (Union[Unset, int]):
    """

    sql_text: str
    cursor_position: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sql_text = self.sql_text
        cursor_position = self.cursor_position

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sql_text": sql_text,
            }
        )
        if cursor_position is not UNSET:
            field_dict["cursor_position"] = cursor_position

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sql_text = d.pop("sql_text")

        cursor_position = d.pop("cursor_position", UNSET)

        sql_autocomplete_query = cls(
            sql_text=sql_text,
            cursor_position=cursor_position,
        )

        sql_autocomplete_query.additional_properties = d
        return sql_autocomplete_query

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

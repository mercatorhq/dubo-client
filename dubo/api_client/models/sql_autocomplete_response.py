from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SqlAutocompleteResponse")


@_attrs_define
class SqlAutocompleteResponse:
    """
    Attributes:
        suggested_sql_text (str):
        full_sql_text (str):
    """

    suggested_sql_text: str
    full_sql_text: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        suggested_sql_text = self.suggested_sql_text
        full_sql_text = self.full_sql_text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "suggested_sql_text": suggested_sql_text,
                "full_sql_text": full_sql_text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        suggested_sql_text = d.pop("suggested_sql_text")

        full_sql_text = d.pop("full_sql_text")

        sql_autocomplete_response = cls(
            suggested_sql_text=suggested_sql_text,
            full_sql_text=full_sql_text,
        )

        sql_autocomplete_response.additional_properties = d
        return sql_autocomplete_response

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

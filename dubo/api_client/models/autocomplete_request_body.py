from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AutocompleteRequestBody")


@_attrs_define
class AutocompleteRequestBody:
    """
    Attributes:
        text_box (str): The current text in the SQL editor box
        cursor_position (Union[Unset, int]): The current cursor position in the SQL editor box
        user_query (Union[Unset, str]):
    """

    text_box: str
    cursor_position: Union[Unset, int] = 0
    user_query: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text_box = self.text_box
        cursor_position = self.cursor_position
        user_query = self.user_query

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text_box": text_box,
            }
        )
        if cursor_position is not UNSET:
            field_dict["cursor_position"] = cursor_position
        if user_query is not UNSET:
            field_dict["user_query"] = user_query

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text_box = d.pop("text_box")

        cursor_position = d.pop("cursor_position", UNSET)

        user_query = d.pop("user_query", UNSET)

        autocomplete_request_body = cls(
            text_box=text_box,
            cursor_position=cursor_position,
            user_query=user_query,
        )

        autocomplete_request_body.additional_properties = d
        return autocomplete_request_body

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

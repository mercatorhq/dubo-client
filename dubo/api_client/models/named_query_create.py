from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NamedQueryCreate")


@_attrs_define
class NamedQueryCreate:
    """
    Attributes:
        sql (str):
        user_id (str):
        data_source_id (str):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
    """

    sql: str
    user_id: str
    data_source_id: str
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sql = self.sql
        user_id = self.user_id
        data_source_id = self.data_source_id
        name = self.name
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sql": sql,
                "user_id": user_id,
                "data_source_id": data_source_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sql = d.pop("sql")

        user_id = d.pop("user_id")

        data_source_id = d.pop("data_source_id")

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        named_query_create = cls(
            sql=sql,
            user_id=user_id,
            data_source_id=data_source_id,
            name=name,
            description=description,
        )

        named_query_create.additional_properties = d
        return named_query_create

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

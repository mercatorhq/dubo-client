from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NamedQueryUpdate")


@_attrs_define
class NamedQueryUpdate:
    """
    Attributes:
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        sql (Union[Unset, str]):
        user_id (Union[Unset, str]):
        data_source_id (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    sql: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    data_source_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        sql = self.sql
        user_id = self.user_id
        data_source_id = self.data_source_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if sql is not UNSET:
            field_dict["sql"] = sql
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if data_source_id is not UNSET:
            field_dict["data_source_id"] = data_source_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        sql = d.pop("sql", UNSET)

        user_id = d.pop("user_id", UNSET)

        data_source_id = d.pop("data_source_id", UNSET)

        named_query_update = cls(
            name=name,
            description=description,
            sql=sql,
            user_id=user_id,
            data_source_id=data_source_id,
        )

        named_query_update.additional_properties = d
        return named_query_update

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

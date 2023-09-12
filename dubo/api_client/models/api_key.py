import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiKey")


@_attrs_define
class ApiKey:
    """
    Attributes:
        id (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        name (str):
        created_by_user_id (str):
        data_source_id (str):
        organization_id (str):
        api_key (Union[Unset, str]):
    """

    id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: str
    created_by_user_id: str
    data_source_id: str
    organization_id: str
    api_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name = self.name
        created_by_user_id = self.created_by_user_id
        data_source_id = self.data_source_id
        organization_id = self.organization_id
        api_key = self.api_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
                "name": name,
                "created_by_user_id": created_by_user_id,
                "data_source_id": data_source_id,
                "organization_id": organization_id,
            }
        )
        if api_key is not UNSET:
            field_dict["api_key"] = api_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        name = d.pop("name")

        created_by_user_id = d.pop("created_by_user_id")

        data_source_id = d.pop("data_source_id")

        organization_id = d.pop("organization_id")

        api_key = d.pop("api_key", UNSET)

        api_key = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            created_by_user_id=created_by_user_id,
            data_source_id=data_source_id,
            organization_id=organization_id,
            api_key=api_key,
        )

        api_key.additional_properties = d
        return api_key

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

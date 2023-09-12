from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RLSAsset")


@_attrs_define
class RLSAsset:
    """
    Attributes:
        id (str):
        name (str):
        organization_id (str):
        created_by_user_id (str):
    """

    id: str
    name: str
    organization_id: str
    created_by_user_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        organization_id = self.organization_id
        created_by_user_id = self.created_by_user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "organization_id": organization_id,
                "created_by_user_id": created_by_user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        created_by_user_id = d.pop("created_by_user_id")

        rls_asset = cls(
            id=id,
            name=name,
            organization_id=organization_id,
            created_by_user_id=created_by_user_id,
        )

        rls_asset.additional_properties = d
        return rls_asset

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

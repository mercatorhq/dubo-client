import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Organization")


@_attrs_define
class Organization:
    """The minimal user information.

    Attributes:
        id (str):
        email_domain (str):
        name (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        created_by_user_id (Union[Unset, str]):
    """

    id: str
    email_domain: str
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    created_by_user_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        email_domain = self.email_domain
        name = self.name
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        created_by_user_id = self.created_by_user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "email_domain": email_domain,
                "name": name,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if created_by_user_id is not UNSET:
            field_dict["created_by_user_id"] = created_by_user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        email_domain = d.pop("email_domain")

        name = d.pop("name")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        created_by_user_id = d.pop("created_by_user_id", UNSET)

        organization = cls(
            id=id,
            email_domain=email_domain,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            created_by_user_id=created_by_user_id,
        )

        organization.additional_properties = d
        return organization

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

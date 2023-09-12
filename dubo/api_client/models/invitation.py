import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.user_role import UserRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="Invitation")


@_attrs_define
class Invitation:
    """The minimal invitation information.

    Attributes:
        invited_email (str):
        user_role (UserRole): An enumeration.
        id (str):
        organization_id (str):
        invited_by_user_id (str):
        created_at (datetime.datetime):
        expires_at (datetime.datetime):
        used_at (Union[Unset, datetime.datetime]):
    """

    invited_email: str
    user_role: UserRole
    id: str
    organization_id: str
    invited_by_user_id: str
    created_at: datetime.datetime
    expires_at: datetime.datetime
    used_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invited_email = self.invited_email
        user_role = self.user_role.value

        id = self.id
        organization_id = self.organization_id
        invited_by_user_id = self.invited_by_user_id
        created_at = self.created_at.isoformat()

        expires_at = self.expires_at.isoformat()

        used_at: Union[Unset, str] = UNSET
        if not isinstance(self.used_at, Unset):
            used_at = self.used_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invited_email": invited_email,
                "user_role": user_role,
                "id": id,
                "organization_id": organization_id,
                "invited_by_user_id": invited_by_user_id,
                "created_at": created_at,
                "expires_at": expires_at,
            }
        )
        if used_at is not UNSET:
            field_dict["used_at"] = used_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invited_email = d.pop("invited_email")

        user_role = UserRole(d.pop("user_role"))

        id = d.pop("id")

        organization_id = d.pop("organization_id")

        invited_by_user_id = d.pop("invited_by_user_id")

        created_at = isoparse(d.pop("created_at"))

        expires_at = isoparse(d.pop("expires_at"))

        _used_at = d.pop("used_at", UNSET)
        used_at: Union[Unset, datetime.datetime]
        if isinstance(_used_at, Unset):
            used_at = UNSET
        else:
            used_at = isoparse(_used_at)

        invitation = cls(
            invited_email=invited_email,
            user_role=user_role,
            id=id,
            organization_id=organization_id,
            invited_by_user_id=invited_by_user_id,
            created_at=created_at,
            expires_at=expires_at,
            used_at=used_at,
        )

        invitation.additional_properties = d
        return invitation

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

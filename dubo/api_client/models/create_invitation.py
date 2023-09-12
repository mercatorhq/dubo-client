from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_role import UserRole

T = TypeVar("T", bound="CreateInvitation")


@_attrs_define
class CreateInvitation:
    """
    Attributes:
        invited_email (str):
        user_role (UserRole): An enumeration.
    """

    invited_email: str
    user_role: UserRole
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invited_email = self.invited_email
        user_role = self.user_role.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invited_email": invited_email,
                "user_role": user_role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invited_email = d.pop("invited_email")

        user_role = UserRole(d.pop("user_role"))

        create_invitation = cls(
            invited_email=invited_email,
            user_role=user_role,
        )

        create_invitation.additional_properties = d
        return create_invitation

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

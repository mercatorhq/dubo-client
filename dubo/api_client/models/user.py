from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_role import UserRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """Full user information.

    Attributes:
        id (str):
        email (str):
        sub_id (str):
        given_name (Union[Unset, str]):
        family_name (Union[Unset, str]):
        organization_id (Union[Unset, str]):
        nickname (Union[Unset, str]):
        name (Union[Unset, str]):
        locale (Union[Unset, str]):
        picture (Union[Unset, str]):
        email_verified (Union[Unset, bool]):
        role (Union[Unset, UserRole]): An enumeration.
    """

    id: str
    email: str
    sub_id: str
    given_name: Union[Unset, str] = UNSET
    family_name: Union[Unset, str] = UNSET
    organization_id: Union[Unset, str] = UNSET
    nickname: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    locale: Union[Unset, str] = UNSET
    picture: Union[Unset, str] = UNSET
    email_verified: Union[Unset, bool] = False
    role: Union[Unset, UserRole] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        email = self.email
        sub_id = self.sub_id
        given_name = self.given_name
        family_name = self.family_name
        organization_id = self.organization_id
        nickname = self.nickname
        name = self.name
        locale = self.locale
        picture = self.picture
        email_verified = self.email_verified
        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "email": email,
                "sub_id": sub_id,
            }
        )
        if given_name is not UNSET:
            field_dict["given_name"] = given_name
        if family_name is not UNSET:
            field_dict["family_name"] = family_name
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if name is not UNSET:
            field_dict["name"] = name
        if locale is not UNSET:
            field_dict["locale"] = locale
        if picture is not UNSET:
            field_dict["picture"] = picture
        if email_verified is not UNSET:
            field_dict["email_verified"] = email_verified
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        email = d.pop("email")

        sub_id = d.pop("sub_id")

        given_name = d.pop("given_name", UNSET)

        family_name = d.pop("family_name", UNSET)

        organization_id = d.pop("organization_id", UNSET)

        nickname = d.pop("nickname", UNSET)

        name = d.pop("name", UNSET)

        locale = d.pop("locale", UNSET)

        picture = d.pop("picture", UNSET)

        email_verified = d.pop("email_verified", UNSET)

        _role = d.pop("role", UNSET)
        role: Union[Unset, UserRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = UserRole(_role)

        user = cls(
            id=id,
            email=email,
            sub_id=sub_id,
            given_name=given_name,
            family_name=family_name,
            organization_id=organization_id,
            nickname=nickname,
            name=name,
            locale=locale,
            picture=picture,
            email_verified=email_verified,
            role=role,
        )

        user.additional_properties = d
        return user

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

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PhantomDataSource")


@_attrs_define
class PhantomDataSource:
    """
    Attributes:
        name (str):
        driver (str):
        updated_by_user_id (str):
        phantom_database (str):
        phantom_ddls (str):
        id (Union[Unset, str]):
        created_by_user_id (Union[Unset, str]):
    """

    name: str
    driver: str
    updated_by_user_id: str
    phantom_database: str
    phantom_ddls: str
    id: Union[Unset, str] = UNSET
    created_by_user_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        driver = self.driver
        updated_by_user_id = self.updated_by_user_id
        phantom_database = self.phantom_database
        phantom_ddls = self.phantom_ddls
        id = self.id
        created_by_user_id = self.created_by_user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "driver": driver,
                "updated_by_user_id": updated_by_user_id,
                "phantom_database": phantom_database,
                "phantom_ddls": phantom_ddls,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if created_by_user_id is not UNSET:
            field_dict["created_by_user_id"] = created_by_user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        driver = d.pop("driver")

        updated_by_user_id = d.pop("updated_by_user_id")

        phantom_database = d.pop("phantom_database")

        phantom_ddls = d.pop("phantom_ddls")

        id = d.pop("id", UNSET)

        created_by_user_id = d.pop("created_by_user_id", UNSET)

        phantom_data_source = cls(
            name=name,
            driver=driver,
            updated_by_user_id=updated_by_user_id,
            phantom_database=phantom_database,
            phantom_ddls=phantom_ddls,
            id=id,
            created_by_user_id=created_by_user_id,
        )

        phantom_data_source.additional_properties = d
        return phantom_data_source

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

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_phantom_data_source_extras import UpdatePhantomDataSourceExtras


T = TypeVar("T", bound="UpdatePhantomDataSource")


@_attrs_define
class UpdatePhantomDataSource:
    """Mixin class for extras field

    Attributes:
        id (str):
        name (str):
        driver (str):
        phantom_database (str):
        phantom_ddls (str):
        extras (Union[Unset, UpdatePhantomDataSourceExtras]):
    """

    id: str
    name: str
    driver: str
    phantom_database: str
    phantom_ddls: str
    extras: Union[Unset, "UpdatePhantomDataSourceExtras"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        driver = self.driver
        phantom_database = self.phantom_database
        phantom_ddls = self.phantom_ddls
        extras: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "driver": driver,
                "phantom_database": phantom_database,
                "phantom_ddls": phantom_ddls,
            }
        )
        if extras is not UNSET:
            field_dict["extras"] = extras

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.update_phantom_data_source_extras import UpdatePhantomDataSourceExtras

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        driver = d.pop("driver")

        phantom_database = d.pop("phantom_database")

        phantom_ddls = d.pop("phantom_ddls")

        _extras = d.pop("extras", UNSET)
        extras: Union[Unset, UpdatePhantomDataSourceExtras]
        if isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = UpdatePhantomDataSourceExtras.from_dict(_extras)

        update_phantom_data_source = cls(
            id=id,
            name=name,
            driver=driver,
            phantom_database=phantom_database,
            phantom_ddls=phantom_ddls,
            extras=extras,
        )

        update_phantom_data_source.additional_properties = d
        return update_phantom_data_source

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

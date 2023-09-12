import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.db_feature_type import DbFeatureType
from ..models.driver_type import DriverType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.public_data_source_extras import PublicDataSourceExtras


T = TypeVar("T", bound="PublicDataSource")


@_attrs_define
class PublicDataSource:
    """Mixin class for extras field

    Attributes:
        driver (DriverType): An enumeration.
        id (str):
        name (str):
        created_by_user_id (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        extras (Union[Unset, PublicDataSourceExtras]):
        features (Union[Unset, List[DbFeatureType]]):
    """

    driver: DriverType
    id: str
    name: str
    created_by_user_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    extras: Union[Unset, "PublicDataSourceExtras"] = UNSET
    features: Union[Unset, List[DbFeatureType]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        driver = self.driver.value

        id = self.id
        name = self.name
        created_by_user_id = self.created_by_user_id
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        extras: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict()

        features: Union[Unset, List[str]] = UNSET
        if not isinstance(self.features, Unset):
            features = []
            for features_item_data in self.features:
                features_item = features_item_data.value

                features.append(features_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "driver": driver,
                "id": id,
                "name": name,
                "created_by_user_id": created_by_user_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if extras is not UNSET:
            field_dict["extras"] = extras
        if features is not UNSET:
            field_dict["features"] = features

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.public_data_source_extras import PublicDataSourceExtras

        d = src_dict.copy()
        driver = DriverType(d.pop("driver"))

        id = d.pop("id")

        name = d.pop("name")

        created_by_user_id = d.pop("created_by_user_id")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        _extras = d.pop("extras", UNSET)
        extras: Union[Unset, PublicDataSourceExtras]
        if isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = PublicDataSourceExtras.from_dict(_extras)

        features = []
        _features = d.pop("features", UNSET)
        for features_item_data in _features or []:
            features_item = DbFeatureType(features_item_data)

            features.append(features_item)

        public_data_source = cls(
            driver=driver,
            id=id,
            name=name,
            created_by_user_id=created_by_user_id,
            created_at=created_at,
            updated_at=updated_at,
            extras=extras,
            features=features,
        )

        public_data_source.additional_properties = d
        return public_data_source

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

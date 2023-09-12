from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.driver_type import DriverType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_big_query_data_source_extras import UpdateBigQueryDataSourceExtras


T = TypeVar("T", bound="UpdateBigQueryDataSource")


@_attrs_define
class UpdateBigQueryDataSource:
    """Mixin class for extras field

    Attributes:
        id (str):
        name (str):
        project (str):
        dataset (str):
        credentials_base64 (str):
        extras (Union[Unset, UpdateBigQueryDataSourceExtras]):
        driver (Union[Unset, DriverType]): An enumeration. Default: DriverType.BIGQUERY.
        location (Union[Unset, str]):
    """

    id: str
    name: str
    project: str
    dataset: str
    credentials_base64: str
    extras: Union[Unset, "UpdateBigQueryDataSourceExtras"] = UNSET
    driver: Union[Unset, DriverType] = DriverType.BIGQUERY
    location: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        project = self.project
        dataset = self.dataset
        credentials_base64 = self.credentials_base64
        extras: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict()

        driver: Union[Unset, str] = UNSET
        if not isinstance(self.driver, Unset):
            driver = self.driver.value

        location = self.location

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "project": project,
                "dataset": dataset,
                "credentials_base64": credentials_base64,
            }
        )
        if extras is not UNSET:
            field_dict["extras"] = extras
        if driver is not UNSET:
            field_dict["driver"] = driver
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.update_big_query_data_source_extras import UpdateBigQueryDataSourceExtras

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        project = d.pop("project")

        dataset = d.pop("dataset")

        credentials_base64 = d.pop("credentials_base64")

        _extras = d.pop("extras", UNSET)
        extras: Union[Unset, UpdateBigQueryDataSourceExtras]
        if isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = UpdateBigQueryDataSourceExtras.from_dict(_extras)

        _driver = d.pop("driver", UNSET)
        driver: Union[Unset, DriverType]
        if isinstance(_driver, Unset):
            driver = UNSET
        else:
            driver = DriverType(_driver)

        location = d.pop("location", UNSET)

        update_big_query_data_source = cls(
            id=id,
            name=name,
            project=project,
            dataset=dataset,
            credentials_base64=credentials_base64,
            extras=extras,
            driver=driver,
            location=location,
        )

        update_big_query_data_source.additional_properties = d
        return update_big_query_data_source

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

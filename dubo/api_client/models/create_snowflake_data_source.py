from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.driver_type import DriverType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_snowflake_data_source_extras import CreateSnowflakeDataSourceExtras


T = TypeVar("T", bound="CreateSnowflakeDataSource")


@_attrs_define
class CreateSnowflakeDataSource:
    """Mixin class for extras field

    Attributes:
        name (str):
        username (str):
        password (str):
        database (str):
        account_identifier (str):
        extras (Union[Unset, CreateSnowflakeDataSourceExtras]):
        driver (Union[Unset, DriverType]): An enumeration. Default: DriverType.SNOWFLAKE.
        schema_name (Union[Unset, str]):
    """

    name: str
    username: str
    password: str
    database: str
    account_identifier: str
    extras: Union[Unset, "CreateSnowflakeDataSourceExtras"] = UNSET
    driver: Union[Unset, DriverType] = DriverType.SNOWFLAKE
    schema_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        username = self.username
        password = self.password
        database = self.database
        account_identifier = self.account_identifier
        extras: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict()

        driver: Union[Unset, str] = UNSET
        if not isinstance(self.driver, Unset):
            driver = self.driver.value

        schema_name = self.schema_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "username": username,
                "password": password,
                "database": database,
                "account_identifier": account_identifier,
            }
        )
        if extras is not UNSET:
            field_dict["extras"] = extras
        if driver is not UNSET:
            field_dict["driver"] = driver
        if schema_name is not UNSET:
            field_dict["schema_name"] = schema_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_snowflake_data_source_extras import CreateSnowflakeDataSourceExtras

        d = src_dict.copy()
        name = d.pop("name")

        username = d.pop("username")

        password = d.pop("password")

        database = d.pop("database")

        account_identifier = d.pop("account_identifier")

        _extras = d.pop("extras", UNSET)
        extras: Union[Unset, CreateSnowflakeDataSourceExtras]
        if isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = CreateSnowflakeDataSourceExtras.from_dict(_extras)

        _driver = d.pop("driver", UNSET)
        driver: Union[Unset, DriverType]
        if isinstance(_driver, Unset):
            driver = UNSET
        else:
            driver = DriverType(_driver)

        schema_name = d.pop("schema_name", UNSET)

        create_snowflake_data_source = cls(
            name=name,
            username=username,
            password=password,
            database=database,
            account_identifier=account_identifier,
            extras=extras,
            driver=driver,
            schema_name=schema_name,
        )

        create_snowflake_data_source.additional_properties = d
        return create_snowflake_data_source

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

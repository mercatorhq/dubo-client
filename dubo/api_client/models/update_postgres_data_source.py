from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.connection_auth_type import ConnectionAuthType
from ..models.driver_type import DriverType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.postgres_ssl_info import PostgresSSLInfo
    from ..models.update_postgres_data_source_extras import UpdatePostgresDataSourceExtras


T = TypeVar("T", bound="UpdatePostgresDataSource")


@_attrs_define
class UpdatePostgresDataSource:
    """Mixin class for extras field

    Attributes:
        id (str):
        name (str):
        username (str):
        host (str):
        port (int):
        database (str):
        extras (Union[Unset, UpdatePostgresDataSourceExtras]):
        driver (Union[Unset, DriverType]): An enumeration. Default: DriverType.POSTGRESQL.
        password (Union[Unset, str]):
        auth_type (Union[Unset, ConnectionAuthType]): An enumeration. Default: ConnectionAuthType.PASSWORD.
        ssl_info (Union[Unset, PostgresSSLInfo]):
    """

    id: str
    name: str
    username: str
    host: str
    port: int
    database: str
    extras: Union[Unset, "UpdatePostgresDataSourceExtras"] = UNSET
    driver: Union[Unset, DriverType] = DriverType.POSTGRESQL
    password: Union[Unset, str] = UNSET
    auth_type: Union[Unset, ConnectionAuthType] = ConnectionAuthType.PASSWORD
    ssl_info: Union[Unset, "PostgresSSLInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        username = self.username
        host = self.host
        port = self.port
        database = self.database
        extras: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict()

        driver: Union[Unset, str] = UNSET
        if not isinstance(self.driver, Unset):
            driver = self.driver.value

        password = self.password
        auth_type: Union[Unset, str] = UNSET
        if not isinstance(self.auth_type, Unset):
            auth_type = self.auth_type.value

        ssl_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ssl_info, Unset):
            ssl_info = self.ssl_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "username": username,
                "host": host,
                "port": port,
                "database": database,
            }
        )
        if extras is not UNSET:
            field_dict["extras"] = extras
        if driver is not UNSET:
            field_dict["driver"] = driver
        if password is not UNSET:
            field_dict["password"] = password
        if auth_type is not UNSET:
            field_dict["auth_type"] = auth_type
        if ssl_info is not UNSET:
            field_dict["ssl_info"] = ssl_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.postgres_ssl_info import PostgresSSLInfo
        from ..models.update_postgres_data_source_extras import UpdatePostgresDataSourceExtras

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        username = d.pop("username")

        host = d.pop("host")

        port = d.pop("port")

        database = d.pop("database")

        _extras = d.pop("extras", UNSET)
        extras: Union[Unset, UpdatePostgresDataSourceExtras]
        if isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = UpdatePostgresDataSourceExtras.from_dict(_extras)

        _driver = d.pop("driver", UNSET)
        driver: Union[Unset, DriverType]
        if isinstance(_driver, Unset):
            driver = UNSET
        else:
            driver = DriverType(_driver)

        password = d.pop("password", UNSET)

        _auth_type = d.pop("auth_type", UNSET)
        auth_type: Union[Unset, ConnectionAuthType]
        if isinstance(_auth_type, Unset):
            auth_type = UNSET
        else:
            auth_type = ConnectionAuthType(_auth_type)

        _ssl_info = d.pop("ssl_info", UNSET)
        ssl_info: Union[Unset, PostgresSSLInfo]
        if isinstance(_ssl_info, Unset):
            ssl_info = UNSET
        else:
            ssl_info = PostgresSSLInfo.from_dict(_ssl_info)

        update_postgres_data_source = cls(
            id=id,
            name=name,
            username=username,
            host=host,
            port=port,
            database=database,
            extras=extras,
            driver=driver,
            password=password,
            auth_type=auth_type,
            ssl_info=ssl_info,
        )

        update_postgres_data_source.additional_properties = d
        return update_postgres_data_source

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

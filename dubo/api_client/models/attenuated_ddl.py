from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.table_column import TableColumn


T = TypeVar("T", bound="AttenuatedDDL")


@_attrs_define
class AttenuatedDDL:
    """
    Attributes:
        cols (List['TableColumn']):
        table_name (str):
        schema_name (str):
        id (Union[Unset, str]):
        partition_columns (Union[Unset, List[str]]):
        database_name (Union[Unset, str]):
        description (Union[Unset, str]):
        foreign_keys (Union[Unset, List[str]]):
        page_rank (Union[Unset, int]):
    """

    cols: List["TableColumn"]
    table_name: str
    schema_name: str
    id: Union[Unset, str] = UNSET
    partition_columns: Union[Unset, List[str]] = UNSET
    database_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    foreign_keys: Union[Unset, List[str]] = UNSET
    page_rank: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cols = []
        for cols_item_data in self.cols:
            cols_item = cols_item_data.to_dict()

            cols.append(cols_item)

        table_name = self.table_name
        schema_name = self.schema_name
        id = self.id
        partition_columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.partition_columns, Unset):
            partition_columns = self.partition_columns

        database_name = self.database_name
        description = self.description
        foreign_keys: Union[Unset, List[str]] = UNSET
        if not isinstance(self.foreign_keys, Unset):
            foreign_keys = self.foreign_keys

        page_rank = self.page_rank

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cols": cols,
                "table_name": table_name,
                "schema_name": schema_name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if partition_columns is not UNSET:
            field_dict["partition_columns"] = partition_columns
        if database_name is not UNSET:
            field_dict["database_name"] = database_name
        if description is not UNSET:
            field_dict["description"] = description
        if foreign_keys is not UNSET:
            field_dict["foreign_keys"] = foreign_keys
        if page_rank is not UNSET:
            field_dict["page_rank"] = page_rank

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.table_column import TableColumn

        d = src_dict.copy()
        cols = []
        _cols = d.pop("cols")
        for cols_item_data in _cols:
            cols_item = TableColumn.from_dict(cols_item_data)

            cols.append(cols_item)

        table_name = d.pop("table_name")

        schema_name = d.pop("schema_name")

        id = d.pop("id", UNSET)

        partition_columns = cast(List[str], d.pop("partition_columns", UNSET))

        database_name = d.pop("database_name", UNSET)

        description = d.pop("description", UNSET)

        foreign_keys = cast(List[str], d.pop("foreign_keys", UNSET))

        page_rank = d.pop("page_rank", UNSET)

        attenuated_ddl = cls(
            cols=cols,
            table_name=table_name,
            schema_name=schema_name,
            id=id,
            partition_columns=partition_columns,
            database_name=database_name,
            description=description,
            foreign_keys=foreign_keys,
            page_rank=page_rank,
        )

        attenuated_ddl.additional_properties = d
        return attenuated_ddl

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

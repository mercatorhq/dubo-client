from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TableColumn")


@_attrs_define
class TableColumn:
    """
    Attributes:
        column_name (str):
        data_type (str):
        is_nullable (bool):
        table_name (str):
        schema_name (str):
        is_partitioning_column (Union[Unset, str]):
    """

    column_name: str
    data_type: str
    is_nullable: bool
    table_name: str
    schema_name: str
    is_partitioning_column: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        column_name = self.column_name
        data_type = self.data_type
        is_nullable = self.is_nullable
        table_name = self.table_name
        schema_name = self.schema_name
        is_partitioning_column = self.is_partitioning_column

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "column_name": column_name,
                "data_type": data_type,
                "is_nullable": is_nullable,
                "table_name": table_name,
                "schema_name": schema_name,
            }
        )
        if is_partitioning_column is not UNSET:
            field_dict["is_partitioning_column"] = is_partitioning_column

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        column_name = d.pop("column_name")

        data_type = d.pop("data_type")

        is_nullable = d.pop("is_nullable")

        table_name = d.pop("table_name")

        schema_name = d.pop("schema_name")

        is_partitioning_column = d.pop("is_partitioning_column", UNSET)

        table_column = cls(
            column_name=column_name,
            data_type=data_type,
            is_nullable=is_nullable,
            table_name=table_name,
            schema_name=schema_name,
            is_partitioning_column=is_partitioning_column,
        )

        table_column.additional_properties = d
        return table_column

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

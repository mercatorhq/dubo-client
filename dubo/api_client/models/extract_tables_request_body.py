from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExtractTablesRequestBody")


@_attrs_define
class ExtractTablesRequestBody:
    """
    Attributes:
        sql_text (str):
        data_source_id (str):
    """

    sql_text: str
    data_source_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sql_text = self.sql_text
        data_source_id = self.data_source_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sql_text": sql_text,
                "data_source_id": data_source_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sql_text = d.pop("sql_text")

        data_source_id = d.pop("data_source_id")

        extract_tables_request_body = cls(
            sql_text=sql_text,
            data_source_id=data_source_id,
        )

        extract_tables_request_body.additional_properties = d
        return extract_tables_request_body

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

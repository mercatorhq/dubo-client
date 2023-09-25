import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="DataSourceDocument")


@_attrs_define
class DataSourceDocument:
    """
    Attributes:
        id (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        file_name (str):
        data_source_id (str):
        organization_id (str):
    """

    id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    file_name: str
    data_source_id: str
    organization_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        file_name = self.file_name
        data_source_id = self.data_source_id
        organization_id = self.organization_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
                "file_name": file_name,
                "data_source_id": data_source_id,
                "organization_id": organization_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        file_name = d.pop("file_name")

        data_source_id = d.pop("data_source_id")

        organization_id = d.pop("organization_id")

        data_source_document = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            file_name=file_name,
            data_source_id=data_source_id,
            organization_id=organization_id,
        )

        data_source_document.additional_properties = d
        return data_source_document

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

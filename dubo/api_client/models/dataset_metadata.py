import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatasetMetadata")


@_attrs_define
class DatasetMetadata:
    """
    Attributes:
        id (str):
        hash_id (str):
        name (str):
        filetype (str):
        created_at (datetime.datetime):
        description (Union[Unset, str]):
        created_by_user_id (Union[Unset, str]):
    """

    id: str
    hash_id: str
    name: str
    filetype: str
    created_at: datetime.datetime
    description: Union[Unset, str] = UNSET
    created_by_user_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        hash_id = self.hash_id
        name = self.name
        filetype = self.filetype
        created_at = self.created_at.isoformat()

        description = self.description
        created_by_user_id = self.created_by_user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "hash_id": hash_id,
                "name": name,
                "filetype": filetype,
                "created_at": created_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if created_by_user_id is not UNSET:
            field_dict["created_by_user_id"] = created_by_user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        hash_id = d.pop("hash_id")

        name = d.pop("name")

        filetype = d.pop("filetype")

        created_at = isoparse(d.pop("created_at"))

        description = d.pop("description", UNSET)

        created_by_user_id = d.pop("created_by_user_id", UNSET)

        dataset_metadata = cls(
            id=id,
            hash_id=hash_id,
            name=name,
            filetype=filetype,
            created_at=created_at,
            description=description,
            created_by_user_id=created_by_user_id,
        )

        dataset_metadata.additional_properties = d
        return dataset_metadata

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

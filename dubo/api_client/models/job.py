import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.job_status import JobStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Job")


@_attrs_define
class Job:
    """
    Attributes:
        name (str):
        status (JobStatus): An enumeration.
        job_type (str):
        id (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        message (Union[Unset, str]):
        organization_id (Union[Unset, str]):
        data_source_id (Union[Unset, str]):
    """

    name: str
    status: JobStatus
    job_type: str
    id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    message: Union[Unset, str] = UNSET
    organization_id: Union[Unset, str] = UNSET
    data_source_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        status = self.status.value

        job_type = self.job_type
        id = self.id
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        message = self.message
        organization_id = self.organization_id
        data_source_id = self.data_source_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
                "job_type": job_type,
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if data_source_id is not UNSET:
            field_dict["data_source_id"] = data_source_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        status = JobStatus(d.pop("status"))

        job_type = d.pop("job_type")

        id = d.pop("id")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        message = d.pop("message", UNSET)

        organization_id = d.pop("organization_id", UNSET)

        data_source_id = d.pop("data_source_id", UNSET)

        job = cls(
            name=name,
            status=status,
            job_type=job_type,
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            message=message,
            organization_id=organization_id,
            data_source_id=data_source_id,
        )

        job.additional_properties = d
        return job

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

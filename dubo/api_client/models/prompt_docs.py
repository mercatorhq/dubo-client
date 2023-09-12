import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attenuated_ddl import AttenuatedDDL
    from ..models.gold_query import GoldQuery


T = TypeVar("T", bound="PromptDocs")


@_attrs_define
class PromptDocs:
    """
    Attributes:
        id (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        exemplars (Union[Unset, List['GoldQuery']]):
        ddls (Union[Unset, List['AttenuatedDDL']]):
        documentation (Union[Unset, str]):
        data_source_id (Union[Unset, str]):
    """

    id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    exemplars: Union[Unset, List["GoldQuery"]] = UNSET
    ddls: Union[Unset, List["AttenuatedDDL"]] = UNSET
    documentation: Union[Unset, str] = UNSET
    data_source_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        exemplars: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.exemplars, Unset):
            exemplars = []
            for exemplars_item_data in self.exemplars:
                exemplars_item = exemplars_item_data.to_dict()

                exemplars.append(exemplars_item)

        ddls: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ddls, Unset):
            ddls = []
            for ddls_item_data in self.ddls:
                ddls_item = ddls_item_data.to_dict()

                ddls.append(ddls_item)

        documentation = self.documentation
        data_source_id = self.data_source_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if exemplars is not UNSET:
            field_dict["exemplars"] = exemplars
        if ddls is not UNSET:
            field_dict["ddls"] = ddls
        if documentation is not UNSET:
            field_dict["documentation"] = documentation
        if data_source_id is not UNSET:
            field_dict["data_source_id"] = data_source_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attenuated_ddl import AttenuatedDDL
        from ..models.gold_query import GoldQuery

        d = src_dict.copy()
        id = d.pop("id")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        exemplars = []
        _exemplars = d.pop("exemplars", UNSET)
        for exemplars_item_data in _exemplars or []:
            exemplars_item = GoldQuery.from_dict(exemplars_item_data)

            exemplars.append(exemplars_item)

        ddls = []
        _ddls = d.pop("ddls", UNSET)
        for ddls_item_data in _ddls or []:
            ddls_item = AttenuatedDDL.from_dict(ddls_item_data)

            ddls.append(ddls_item)

        documentation = d.pop("documentation", UNSET)

        data_source_id = d.pop("data_source_id", UNSET)

        prompt_docs = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            exemplars=exemplars,
            ddls=ddls,
            documentation=documentation,
            data_source_id=data_source_id,
        )

        prompt_docs.additional_properties = d
        return prompt_docs

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

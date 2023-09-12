from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attenuated_ddl import AttenuatedDDL
    from ..models.gold_query import GoldQuery


T = TypeVar("T", bound="PromptDocsCreate")


@_attrs_define
class PromptDocsCreate:
    """
    Attributes:
        data_source_id (str):
        ddls (Union[Unset, List['AttenuatedDDL']]):
        documentation (Union[Unset, str]):
        exemplars (Union[Unset, List['GoldQuery']]):
    """

    data_source_id: str
    ddls: Union[Unset, List["AttenuatedDDL"]] = UNSET
    documentation: Union[Unset, str] = UNSET
    exemplars: Union[Unset, List["GoldQuery"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_source_id = self.data_source_id
        ddls: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ddls, Unset):
            ddls = []
            for ddls_item_data in self.ddls:
                ddls_item = ddls_item_data.to_dict()

                ddls.append(ddls_item)

        documentation = self.documentation
        exemplars: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.exemplars, Unset):
            exemplars = []
            for exemplars_item_data in self.exemplars:
                exemplars_item = exemplars_item_data.to_dict()

                exemplars.append(exemplars_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data_source_id": data_source_id,
            }
        )
        if ddls is not UNSET:
            field_dict["ddls"] = ddls
        if documentation is not UNSET:
            field_dict["documentation"] = documentation
        if exemplars is not UNSET:
            field_dict["exemplars"] = exemplars

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attenuated_ddl import AttenuatedDDL
        from ..models.gold_query import GoldQuery

        d = src_dict.copy()
        data_source_id = d.pop("data_source_id")

        ddls = []
        _ddls = d.pop("ddls", UNSET)
        for ddls_item_data in _ddls or []:
            ddls_item = AttenuatedDDL.from_dict(ddls_item_data)

            ddls.append(ddls_item)

        documentation = d.pop("documentation", UNSET)

        exemplars = []
        _exemplars = d.pop("exemplars", UNSET)
        for exemplars_item_data in _exemplars or []:
            exemplars_item = GoldQuery.from_dict(exemplars_item_data)

            exemplars.append(exemplars_item)

        prompt_docs_create = cls(
            data_source_id=data_source_id,
            ddls=ddls,
            documentation=documentation,
            exemplars=exemplars,
        )

        prompt_docs_create.additional_properties = d
        return prompt_docs_create

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

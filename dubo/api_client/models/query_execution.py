import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.query_status import QueryStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_execution_db_query_info import QueryExecutionDbQueryInfo
    from ..models.query_execution_results_set_item import QueryExecutionResultsSetItem


T = TypeVar("T", bound="QueryExecution")


@_attrs_define
class QueryExecution:
    """
    Attributes:
        start_time (datetime.datetime):
        user_id (str):
        data_source_id (str):
        id (str):
        end_time (Union[Unset, datetime.datetime]):
        status (Union[Unset, QueryStatus]): An enumeration.
        error_message (Union[Unset, str]):
        user_query (Union[Unset, str]):
        sql_text (Union[Unset, str]):
        thread_id (Union[Unset, str]):
        results_set (Union[Unset, List['QueryExecutionResultsSetItem']]):
        row_count (Union[Unset, int]):
        db_query_info (Union[Unset, QueryExecutionDbQueryInfo]):
    """

    start_time: datetime.datetime
    user_id: str
    data_source_id: str
    id: str
    end_time: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, QueryStatus] = UNSET
    error_message: Union[Unset, str] = UNSET
    user_query: Union[Unset, str] = UNSET
    sql_text: Union[Unset, str] = UNSET
    thread_id: Union[Unset, str] = UNSET
    results_set: Union[Unset, List["QueryExecutionResultsSetItem"]] = UNSET
    row_count: Union[Unset, int] = UNSET
    db_query_info: Union[Unset, "QueryExecutionDbQueryInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_time = self.start_time.isoformat()

        user_id = self.user_id
        data_source_id = self.data_source_id
        id = self.id
        end_time: Union[Unset, str] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        error_message = self.error_message
        user_query = self.user_query
        sql_text = self.sql_text
        thread_id = self.thread_id
        results_set: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.results_set, Unset):
            results_set = []
            for results_set_item_data in self.results_set:
                results_set_item = results_set_item_data.to_dict()

                results_set.append(results_set_item)

        row_count = self.row_count
        db_query_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.db_query_info, Unset):
            db_query_info = self.db_query_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start_time": start_time,
                "user_id": user_id,
                "data_source_id": data_source_id,
                "id": id,
            }
        )
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if status is not UNSET:
            field_dict["status"] = status
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if user_query is not UNSET:
            field_dict["user_query"] = user_query
        if sql_text is not UNSET:
            field_dict["sql_text"] = sql_text
        if thread_id is not UNSET:
            field_dict["thread_id"] = thread_id
        if results_set is not UNSET:
            field_dict["results_set"] = results_set
        if row_count is not UNSET:
            field_dict["row_count"] = row_count
        if db_query_info is not UNSET:
            field_dict["db_query_info"] = db_query_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.query_execution_db_query_info import QueryExecutionDbQueryInfo
        from ..models.query_execution_results_set_item import QueryExecutionResultsSetItem

        d = src_dict.copy()
        start_time = isoparse(d.pop("start_time"))

        user_id = d.pop("user_id")

        data_source_id = d.pop("data_source_id")

        id = d.pop("id")

        _end_time = d.pop("end_time", UNSET)
        end_time: Union[Unset, datetime.datetime]
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        _status = d.pop("status", UNSET)
        status: Union[Unset, QueryStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = QueryStatus(_status)

        error_message = d.pop("error_message", UNSET)

        user_query = d.pop("user_query", UNSET)

        sql_text = d.pop("sql_text", UNSET)

        thread_id = d.pop("thread_id", UNSET)

        results_set = []
        _results_set = d.pop("results_set", UNSET)
        for results_set_item_data in _results_set or []:
            results_set_item = QueryExecutionResultsSetItem.from_dict(results_set_item_data)

            results_set.append(results_set_item)

        row_count = d.pop("row_count", UNSET)

        _db_query_info = d.pop("db_query_info", UNSET)
        db_query_info: Union[Unset, QueryExecutionDbQueryInfo]
        if isinstance(_db_query_info, Unset):
            db_query_info = UNSET
        else:
            db_query_info = QueryExecutionDbQueryInfo.from_dict(_db_query_info)

        query_execution = cls(
            start_time=start_time,
            user_id=user_id,
            data_source_id=data_source_id,
            id=id,
            end_time=end_time,
            status=status,
            error_message=error_message,
            user_query=user_query,
            sql_text=sql_text,
            thread_id=thread_id,
            results_set=results_set,
            row_count=row_count,
            db_query_info=db_query_info,
        )

        query_execution.additional_properties = d
        return query_execution

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

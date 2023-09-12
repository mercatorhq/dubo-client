from enum import Enum


class JobStatus(str, Enum):
    AWAITING_USER_REVIEW = "awaiting_user_review"
    CANCELED = "canceled"
    COMPLETED = "completed"
    ERROR = "error"
    LABELING = "labeling"
    RANKING_QUERY_TABLES = "ranking_query_tables"
    READING_PAST_QUERIES = "reading_past_queries"
    SAVING_DDLS = "saving_ddls"
    SAVING_LABELS = "saving_labels"
    SAVING_PAST_QUERIES = "saving_past_queries"
    SCRAPING = "scraping"
    STARTING = "starting"

    def __str__(self) -> str:
        return str(self.value)

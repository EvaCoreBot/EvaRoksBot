"""Handlers for EvaRoksBot."""

from .doc_handler import handle_doc
from .risk_handler import handle_risk
from .review_handler import handle_review
from .prompt_handler import handle_prompt
from .generate_handler import handle_generate
from .history_handler import handle_history

__all__ = [
    "handle_doc",
    "handle_risk",
    "handle_review",
    "handle_prompt",
    "handle_generate",
    "handle_history",
]

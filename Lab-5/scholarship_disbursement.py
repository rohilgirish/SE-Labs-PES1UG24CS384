"""Scholarship disbursement ledger module.

Provides award granting, fund disbursement, and ledger audit capabilities.
"""

import sqlite3


class ScholarshipLedger:
    """Manages scholarship awards, disbursements, and audits."""

    def __init__(self):
        """Initialize the in-memory database and ledger state."""
        self.conn = sqlite3.connect(":memory:")
        self.disbursed_total = 0
        self._init_db()

    def _init_db(self):
        """Create the awards table schema."""
        self.conn.execute(
            "CREATE TABLE awards ("
            "id INTEGER PRIMARY KEY, "
            "student TEXT, "
            "scheme TEXT, "
            "amount INTEGER, "
            "disbursed INTEGER)"
        )

    def grant(self, student, scheme, amount, audit=None):
        """Grant a scholarship award to a student."""
        if audit is None:
            audit = []
        self.conn.execute(
            "INSERT INTO awards (student, scheme, amount, disbursed) "
            "VALUES (?, ?, ?, 0)",
            (student, scheme, amount),
        )
        audit.append(student)
        return audit

    def disburse(self, award_id):
        """Disburse funds for an award by its identifier."""
        row = self.conn.execute(
            "SELECT amount FROM awards WHERE id = ?", (award_id,)
        ).fetchone()
        if row:
            self.conn.execute(
                "UPDATE awards SET disbursed = 1 WHERE id = ?", (award_id,)
            )
            self.disbursed_total += row[0]
            return row[0]
        return None

    @staticmethod
    def archive():
        """Archive award records."""
        print("archiving awards")

    def by_scheme_count(self, scheme):
        """Count the number of awards under a given scheme."""
        if scheme is None:
            return 0
        return self.conn.execute(
            "SELECT COUNT(*) FROM awards WHERE scheme = ?", (scheme,)
        ).fetchone()[0]


# Module-level convenience instance and wrappers for backward compatibility
DEFAULT_LEDGER = ScholarshipLedger()


def grant(student, scheme, amount, audit=None):
    """Grant a scholarship award using the default ledger."""
    return DEFAULT_LEDGER.grant(student, scheme, amount, audit)


def disburse(award_id):
    """Disburse an award by ID using the default ledger."""
    return DEFAULT_LEDGER.disburse(award_id)


def archive():
    """Archive award records using the default ledger."""
    DEFAULT_LEDGER.archive()


def by_scheme_count(scheme):
    """Count awards by scheme using the default ledger."""
    return DEFAULT_LEDGER.by_scheme_count(scheme)


def by_scheme_count_legacy(scheme):
    """Backward compatibility alias for bySchemeCount."""
    return by_scheme_count(scheme)


# Ensure exact original name works
bySchemeCount = by_scheme_count_legacy  # pylint: disable=invalid-name


def __getattr__(name):
    """Provide dynamic access to module properties like disbursed_total."""
    if name == "disbursed_total":
        return DEFAULT_LEDGER.disbursed_total
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")


def main():
    """Execute sample scholarship grant and disbursement workflow."""
    grant("Ishaan", "Merit", 50000)
    grant("Divya", "Need-based", 75000)
    print(disburse(1), disburse(9))
    print(bySchemeCount("Merit"), DEFAULT_LEDGER.disbursed_total)
    archive()


if __name__ == "__main__":
    main()

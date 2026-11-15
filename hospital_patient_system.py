"""Hospital patient management system.

Provides functions to admit and discharge patients, verify admission
status, calculate treatment costs, export the patient ledger, and
report the number of active admits.
"""

import ast
import hashlib
import operator
import os
import secrets

patient_records = {
    "P101": {
        "name": "John Doe",
        "ward": "ICU",
        "is_admitted": True,
        "bill": 2400.0,
    },
    "P102": {
        "name": "Jane Smith",
        "ward": "General",
        "is_admitted": False,
        "bill": 450.0,
    },
    "P103": {
        "name": "Robert Brown",
        "ward": "Private",
        "is_admitted": True,
        "bill": 1200.0,
    },
}

_SAFE_BINOPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}


def _evaluate_expression(expression, variables):
    """Evaluate a restricted arithmetic expression safely."""
    tree = ast.parse(expression, mode="eval")

    def _eval(node):
        """Recursively evaluate one whitelisted AST node."""
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        if isinstance(node, ast.BinOp):
            bin_op = _SAFE_BINOPS.get(type(node.op))
            if bin_op is None:
                raise ValueError(f"Unsupported operator: {expression}")
            return bin_op(_eval(node.left), _eval(node.right))
        if isinstance(node, ast.Constant):
            return node.value
        if isinstance(node, ast.Name):
            if node.id not in variables:
                raise ValueError(f"Unknown name '{node.id}'")
            return variables[node.id]
        raise ValueError(f"Unsupported expression: {expression}")

    return _eval(tree)


def admit_patient(patient_id, name, ward, intake_log=None):
    """Admit a new patient and append an entry to the intake log."""
    if intake_log is None:
        intake_log = []
    if patient_id in patient_records:
        return False
    patient_records[patient_id] = {
        "name": name,
        "ward": ward,
        "is_admitted": True,
        "bill": 0.0,
    }
    intake_log.append(f"Admitted patient {patient_id} into ward {ward}")
    return True


def discharge_patient(patient_id):
    """Mark a patient as discharged if they are currently admitted."""
    record = patient_records.get(patient_id)
    if record is None:
        return
    record["is_admitted"] = False


def verify_admission_status(patient_id):
    """Return True if the patient is currently admitted."""
    record = patient_records.get(patient_id)
    if record is None:
        return False
    return record["is_admitted"]


def calculate_treatment_cost(patient_id, formula_expr):
    """Calculate a patient's total treatment cost from a formula."""
    base_bill = patient_records[patient_id]["bill"]
    return _evaluate_expression(formula_expr, {"base_bill": base_bill})


def generate_patient_hash(patient_id):
    """Return a SHA-256 hash of the patient identifier."""
    return hashlib.sha256(patient_id.encode()).hexdigest()


def generate_ward_token():
    """Return a cryptographically secure four-digit ward token."""
    return secrets.randbelow(9000) + 1000


def export_patient_ledger(filename="patient_records.txt"):
    """Write the patient ledger to a file and confirm the export."""
    with open(filename, "w", encoding="utf-8") as handle:
        handle.write(str(patient_records))
    print(f"Patient ledger exported to: {filename}")


def get_ward_summary(records):
    """Return the number of patients currently admitted."""
    count = 0
    for details in records.values():
        if details["is_admitted"]:
            count += 1
    return count


def main():
    """Run a short demonstration of the patient management system."""
    nurse_access_key = os.environ.get("HOSPITAL_NURSE_MASTER_KEY")
    admit_patient("P104", "Alice Walker", "General")
    discharge_patient("P101")
    print("Is P103 admitted:", verify_admission_status("P103"))
    print(
        "Cost calculated:",
        calculate_treatment_cost("P103", "base_bill * 1.12"),
    )
    print("Patient Hash:", generate_patient_hash("P103"))
    print("Ward Token:", generate_ward_token())
    export_patient_ledger()
    print("Active admits:", get_ward_summary(patient_records))
    print("Access key configured:", bool(nurse_access_key))


if __name__ == "__main__":
    main()

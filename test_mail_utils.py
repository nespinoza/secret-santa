import pytest

from mail_utils import assign_partner


emails = [
    {
        "name": "Rodolfo Ferro",
        "email": "ferro@cimat.mx"
    },
    {
        "name": "Ricardo Mirón",
        "email": "ricardomirontorres@gmail.com"
    },
    {
        "name": "Ivan Gonzalez",
        "email": "me@ivgo.me"
    }
]


def _test_valid_emails(emails):
    assigned = set()

    for mail in emails:
        assert mail.get('assigned', None) is not None  # not empty assignment
        assert mail['name'] != mail['assigned']  # no self assignment

        assigned.add(mail['assigned'])

    assert len(assigned) == len(emails)  # all have assignment


def test_assign_partner():
    global emails

    with pytest.raises(ValueError):
        assign_partner([])

    with pytest.raises(ValueError):
        assign_partner([0])

    n = 10  # reasonable number of tests for a stochastic process
    for _ in range(n):
        assigned_emails = assign_partner(emails.copy())
        _test_valid_emails(assigned_emails)

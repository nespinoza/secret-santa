import unittest
from mail_utils import assign_partner

class TestMailUtils(unittest.TestCase):
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

    def _test_valid_emails(self, emails):
        assigned = set()

        for mail in emails:
            self.assertIn('assigned', mail) # not empty assignment
            self.assertIsNotNone(mail['assigned']) 
            self.assertNotEqual(mail['name'], mail['assigned']) # no self assignment

            assigned.add(mail['assigned'])

        self.assertEqual(len(assigned), len(emails)) # all have assignment

    def test_assign_partner(self):
        with self.assertRaises(ValueError):
            assign_partner([])
            assign_partner([0])

        n = 10 # reasonable number of tests for a stochastic process
        for _ in range(n): 
            emails = assign_partner(self.emails)
            self._test_valid_emails(emails)
from odoo.tests import tagged
from odoo.tests.common import Form

from odoo.addons.account.tests.common import AccountTestInvoicingCommon


@tagged("post_install", "-at_install")
class TestAccountMoveTWZ(AccountTestInvoicingCommon):
    @classmethod
    def setUpClass(cls, chart_template_ref=None):
        super().setUpClass(chart_template_ref=chart_template_ref)
        cls.invoice = cls.init_invoice("in_invoice", products=cls.product_a + cls.product_b)

    def test_invoice_is_under_complain(self):
        with Form(self.invoice) as move_form:
            move_form.is_under_complain = True
        move_form.save()
        self.assertTrue(all(self.invoice.line_ids.mapped("blocked")))

        with Form(self.invoice) as move_form:
            move_form.is_under_complain = False
        move_form.save()
        self.assertTrue(not any(self.invoice.line_ids.mapped("blocked")))

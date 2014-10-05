from datetime import date

__author__ = 'ceasaro'


class FinancialYearMixin(object):

    def financial_year(self):
        """
        The financial year bound to the request as 'request.financial_year'
        return: the financial year form to request GET params if not found the current year is returned.
        """
        this_year = date.today().year
        financial_year = int(self.request.GET.get('year', this_year))
        self.request.financial_year = financial_year
        self.request.financial_years = range(this_year-5, this_year+1)
        return financial_year
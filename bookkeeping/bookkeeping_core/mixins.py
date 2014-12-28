from datetime import date

__author__ = 'ceasaro'


class FinancialYearMixin(object):

    def financial_year(self):
        """
        The financial year bound to the request as 'request.financial_year'
        return: the financial year form to request GET params if not found the current year is returned.
        """
        this_year = date.today().year
        requested_year = self.request.GET.get('year', None)
        if requested_year:
            requested_year = int(requested_year)
            self.request.session['financial_year'] = requested_year
            financial_year = requested_year
        else:
            session_year = self.request.session['financial_year']
            financial_year = session_year if session_year else int(this_year)

        self.request.financial_year = financial_year
        self.request.financial_years = range(this_year-6, this_year+1)
        return financial_year
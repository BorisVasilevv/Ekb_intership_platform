

class CompanyWithCategoryData:
    id: int
    name: str
    logotype: str
    short_description: str
    url: str
    accreditation: bool
    phone: str
    telegram: str
    email: str
    categories: []
    subcategories: []

    def __init__(self, company_id, company_name, company_logotype,
                 company_short_description, company_url, categories, subcategories,
                 phone, telegram, accreditation, email):
        self.id = company_id
        self.name = company_name
        self.logotype = company_logotype
        self.short_description = company_short_description
        self.url = company_url
        self.categories = categories
        self.subcategories = subcategories
        self.phone = phone
        self.telegram = telegram
        self.accreditation = accreditation
        self.email = email

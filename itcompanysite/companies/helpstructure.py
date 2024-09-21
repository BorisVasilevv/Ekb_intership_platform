from .models import Company, Tag


class CompanyFullData:
    id: int
    name: str
    logotype: str
    short_description: str
    url: str
    is_favorite: bool
    accreditation: bool
    phone: str
    telegram: str
    email: str
    categories: []
    subcategories: []
    tags: []

    def __init__(self, company: Company, company_is_favorite, categories, subcategories, tags):
        self.id = company.id
        self.name = company.name
        self.logotype = company.logotype
        self.short_description = company.short_description
        self.url = company.url
        self.phone = company.phone
        self.telegram = company.telegram
        self.accreditation = company.accreditation
        self.email = company.email
        self.is_favorite = company_is_favorite
        self.categories = categories
        self.subcategories = subcategories
        self.tags = tags


class TagWithCheckFlag:
    id: int
    name: str
    is_checked: bool

    def __init__(self, tag: Tag, is_checked: bool):
        self.id = tag.id
        self.name = tag.name
        self.is_checked = is_checked

class CategoryWithSubcategories:
    id: int
    category_name: str
    style_name: str
    description: str
    subcategories = []

    def __init__(self, categor_id, categor_name, categor_color, categor_description):
        self.id = categor_id
        self.category_name = categor_name
        self.color = categor_color
        self.description = categor_description


class CompanyWithAddress:
    id: int
    name: str
    color: str
    address: str
    coordinate_x: float
    coordinate_y: float

    def __init__(self, company_id, company_name, company_color, company_address,
                 company_coordinate_x, company_coordinate_y):

        self.id = company_id
        self.name = company_name
        self.color = company_color
        self.address = company_address
        self.coordinate_x = company_coordinate_x
        self.coordinate_y = company_coordinate_y



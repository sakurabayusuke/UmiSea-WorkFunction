from marshmallow import Schema, fields, post_load


class Attribute:
    def __init__(self, 海底地形名, かな, Undersea_Feature_Name, 属名, 水深, 呼称の由来, 由来_En, 会議名, JCUFN_approved, SCUFN_approved):
        self.海底地形名 = 海底地形名
        self.かな = かな
        self.Undersea_Feature_Name = Undersea_Feature_Name
        self.属名 = 属名
        self.水深 = 水深
        self.呼称の由来 = 呼称の由来
        self.由来_En = 由来_En
        self.会議名 = 会議名
        self.JCUFN_approved = JCUFN_approved
        self.SCUFN_approved = SCUFN_approved


class AttributeSchema(Schema):
    海底地形名 = fields.Str()
    かな = fields.Str()
    Undersea_Feature_Name = fields.Str()
    属名 = fields.Str()
    水深 = fields.Int(allow_none=True)
    呼称の由来 = fields.Str(allow_none=True)
    由来_En = fields.Str(allow_none=True)
    会議名 = fields.Str(allow_none=True)
    JCUFN_approved = fields.Int(allow_none=True)
    SCUFN_approved = fields.Int(allow_none=True)

    @post_load
    def make_attribute(self, data, **kwargs):
        return Attribute(**data)
